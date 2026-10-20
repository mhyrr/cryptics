"""Freeze a target protocol only after both complete, independently verified gates.

python3 -I freeze_protocol.py
No solver is invoked. Existing protocol/target records are never overwritten.
"""
import importlib.util
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent


def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    loaded=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded)
    return loaded


def main():
    protocol_path=HERE / "protocol.json"
    if protocol_path.exists(): raise SystemExit("protocol already exists; do not overwrite a frozen protocol")
    run=module("blume26_protocol_driver",HERE / "run.py")
    plan=json.loads((HERE / "control-plan.json").read_text())
    if (HERE / "results" / (plan["target_tag"]+".jsonl")).exists():
        raise SystemExit("target records already exist without this new freeze")
    run.check_plan("isolated_tag",plan["isolated_tag"])
    run.check_plan("control_tag",plan["control_tag"])
    run.gate(plan["isolated_tag"],True)
    run.gate(plan["control_tag"],False)
    inputs={"isolated":HERE / "results" / (plan["isolated_tag"]+".jsonl"),
            "controls":HERE / "results" / (plan["control_tag"]+".jsonl")}
    digests={name:run.sha(path) for name,path in inputs.items()}
    verifier=module("blume26_protocol_verifier",HERE / "verify_results.py")
    report=verifier.verify()
    assert "PASS: isolated gate; 50/50" in report
    assert "PASS: pipeline gate; 40/40" in report
    assert all(run.sha(inputs[name])==digest and f"snapshot SHA256 {digest}" in report
               for name,digest in digests.items()),"control bytes changed during verification"
    protocol=dict(date=plan["date"],build=run.check_build(),target_tag=plan["target_tag"],
                  control_plan_sha256=run.sha(HERE / "control-plan.json"),
                  isolated=dict(tag=plan["isolated_tag"],sha256=digests["isolated"]),
                  controls=dict(tag=plan["control_tag"],sha256=digests["controls"]),
                  target=plan["target"],scope="Conditional literary-proxy calibration; exploratory T1 test; one shuffle.")
    (HERE / "results/pre-target-verification.txt").write_text(report)
    with protocol_path.open("x") as f:
        f.write(json.dumps(protocol,indent=1)+"\n")
    print("Both complete gates independently verified; protocol.json frozen. No target run started.")


if __name__=="__main__": main()
