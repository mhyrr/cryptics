"""Freeze target protocol after the complete independently verified control gate.

No solver is invoked. Existing protocol/target records cannot be overwritten.
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
    if protocol_path.exists(): raise SystemExit("protocol already exists")
    run=module("blume27_protocol_driver",HERE / "run.py")
    plan=json.loads((HERE / "control-plan.json").read_text())
    if (HERE / "results" / (plan["target_tag"]+".jsonl")).exists():
        raise SystemExit("target records already exist without this freeze")
    run.check_plan("control_tag",plan["control_tag"])
    run.gate(plan["control_tag"])
    controls=HERE / "results" / (plan["control_tag"]+".jsonl")
    digest=run.sha(controls)
    verifier=module("blume27_protocol_verifier",HERE / "verify_results.py")
    report=verifier.verify()
    assert "PASS: pipeline gate; 40/40" in report
    assert run.sha(controls)==digest and f"snapshot SHA256 {digest}" in report
    protocol=dict(date=plan["date"],build=run.check_build(),target_tag=plan["target_tag"],
                  control_plan_sha256=run.sha(HERE / "control-plan.json"),
                  controls=dict(tag=plan["control_tag"],sha256=digest),
                  target=plan["target"],scope="Conditional literary-proxy calibration; finite T1 phrase search; one shuffle.")
    (HERE / "results/pre-target-verification.txt").write_text(report)
    with protocol_path.open("x") as f: f.write(json.dumps(protocol,indent=1)+"\n")
    print("Complete control gate independently verified; target protocol frozen. No target started.")


if __name__=="__main__": main()
