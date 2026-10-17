#!/bin/zsh
# K2-stage pilots (not pre-registered): 01's climb (climb=0 idp=0) against Lasry's (climb=1 idp=1) on shared plants
cd "$(dirname "$0")"
until grep -q chain3-done out/k2p.log 2>/dev/null; do sleep 5; done
B="budget=8000000"
python3 -I run21.py k2 k2q_10x20_c0 es 615 "10x20" 6 3 ptag=Q_10x20 climb=0 idp=0 $B
python3 -I run21.py k2 k2q_10x20_c1 es 615 "10x20" 6 3 ptag=Q_10x20 climb=1 idp=1 $B
python3 -I run21.py k2 k2q_13x17_c0 es 615 "13x17" 6 3 ptag=Q_13x17 climb=0 idp=0 $B
python3 -I run21.py k2 k2q_13x17_c1 es 615 "13x17" 6 3 ptag=Q_13x17 climb=1 idp=1 $B
echo chain4-done
