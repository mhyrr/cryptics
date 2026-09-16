#!/usr/bin/env python3
"""Run the three experiments and tests, optionally checking byte reproduction."""
import argparse
import hashlib
import os
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ANALYSIS = HERE.parent
EXPERIMENTS = ('02-frame-model', '03-fragment-transfer', '04-local-recurrence')
OUTPUTS = [HERE/'manifest.json', ANALYSIS.parent/'STRESS-TESTS.md'] + [
    ANALYSIS/name/output for name in EXPERIMENTS for output in ('results.json','RESULTS.md')]


def hashes():
    return {str(path.relative_to(ANALYSIS.parent)): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in OUTPUTS}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Fail if any generated artifact changes.')
    args = parser.parse_args()
    before = hashes() if args.check else None
    env = dict(os.environ, PYTHONHASHSEED='271828' if args.check else '314159')
    def run(*arguments):
        subprocess.run([sys.executable, *map(str, arguments)], check=True, env=env)
    run(HERE/'common.py')
    for name in EXPERIMENTS:
        run(ANALYSIS/name/'run.py')
    run(HERE/'summarize.py')
    run('-m','unittest','discover','-s',HERE,'-p','test_*.py','-v')
    run('-m','unittest','discover','-s',ANALYSIS/'01-mathers-structure','-p','test_*.py','-v')
    if before is not None:
        after = hashes()
        changed = [name for name in before if before[name] != after[name]]
        if changed:
            raise SystemExit('Reproduction failed: ' + ', '.join(changed))
        print(f'Reproduction passed: {len(OUTPUTS)} artifacts identical under a different Python hash seed.')


if __name__ == '__main__':
    main()
