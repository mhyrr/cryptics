#!/bin/zsh
# basin probes along w1 (pilots): is the basin radius set by the rows of K1?
cd "$(dirname "$0")"
until grep -q chain4-done out/k2q.log 2>/dev/null; do sleep 5; done
P="nclimb=5 nbasin=8 bmax=8 climb=1 idp=1"
python3 -I run21.py probe pr_es615_6x20 es 615 6 20 3 3 ptag=P_es615_6x20 ${=P}
python3 -I run21.py probe pr_es615_10x20 es 615 10 20 3 3 ptag=P_es615_10x20 ${=P}
python3 -I run21.py probe pr_es615_13x17 es 615 13 17 3 3 ptag=P_es615_13x17 ${=P}
echo chain5-done
