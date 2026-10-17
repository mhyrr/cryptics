#!/bin/zsh
# K2-stage pilots (not pre-registered): hit rates along w1 at w2 = 20, a 01 calibration point, and Lasry's setting
cd "$(dirname "$0")"
until grep -q chain2-done out/probes2.log 2>/dev/null; do sleep 5; done
K="budget=8000000 climb=1 idp=1"
python3 -I run21.py k2 k2p_es615_6x20 es 615 "6x20" 3 3 ${=K}
python3 -I run21.py k2 k2p_es615_10x20 es 615 "10x20" 3 3 ${=K}
python3 -I run21.py k2 k2p_es615_13x17 es 615 "13x17" 3 3 ${=K}
python3 -I run21.py k2 k2p_es615_13x20 es 615 "13x20" 3 3 ${=K}
python3 -I run21.py k2 k2p_en599_18x19 en 599 "18x19" 3 3 ${=K}
python3 -I run21.py k2 k2p_en599_19x20 en 599 "19x20" 3 3 ${=K}
echo chain3-done
