#!/bin/zsh
# pilots, not pre-registered: K1-consistent IDP (idp=2, binary out/dcm2), then frontier K2 pilots.
# The first probe runs on one worker while control A's last two trials finish (3 processes in all).
cd "$(dirname "$0")"
P="nclimb=5 nbasin=8 bmax=6 climb=1 bin=dcm2"
python3 -I run21.py probe pr_es615_16x18_i2 es 615 16 18 3 1 ptag=P_es615_16x18 idp=2 ${=P}
until grep -q ctlA-done out/ctlA.log 2>/dev/null; do sleep 5; done
python3 -I run21.py probe pr_es615_10x20_i2 es 615 10 20 3 3 ptag=P_es615_10x20 idp=2 ${=P}
echo probes-i2-done
K="budget=8000000 climb=1"
python3 -I run21.py k2 k2q_10x20_i2 es 615 "10x20" 6 3 ptag=Q_10x20 idp=2 bin=dcm2 ${=K}
python3 -I run21.py k2 k2r_10x18 es 615 "10x18" 6 3 idp=1 ${=K}
python3 -I run21.py k2 k2r_16x17 es 615 "16x17" 6 3 idp=1 ${=K}
echo chain6-done
