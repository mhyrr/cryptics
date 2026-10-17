#!/bin/zsh
# pre-registered control A2 (README), after the frontier pilots of chain 7
cd "$(dirname "$0")"
until grep -q chain7-done out/k2r.log 2>/dev/null; do sleep 5; done
python3 -I run21.py solve ctlA2 es 615 "12-15x17" 10 3 budget=50000000 climb=1 idp=1 k1climb=0
echo ctlA2-done
