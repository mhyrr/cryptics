#!/bin/zsh
# frontier K2 pilots (not pre-registered): 10 x 18 on two workers beside control A's last trial, then 16 x 17
cd "$(dirname "$0")"
K="budget=8000000 climb=1 idp=1"
python3 -I run21.py k2 k2r_10x18 es 615 "10x18" 6 2 ${=K}
until grep -q ctlA-done out/ctlA.log 2>/dev/null; do sleep 5; done
python3 -I run21.py k2 k2r_16x17 es 615 "16x17" 6 3 ${=K}
echo chain7-done
