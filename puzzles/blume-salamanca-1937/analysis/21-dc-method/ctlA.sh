#!/bin/zsh
# pre-registered control A (README): runs after the basin probes of chain 5
cd "$(dirname "$0")"
until grep -q chain5-done out/probes5.log 2>/dev/null; do sleep 5; done
python3 -I run21.py solve ctlA es 615 "2-15x16-17" 10 3 budget=50000000 climb=1 idp=1 k1climb=0
echo ctlA-done
