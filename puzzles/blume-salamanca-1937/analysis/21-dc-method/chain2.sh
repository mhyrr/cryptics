#!/bin/zsh
# probe chain 2 (pilots, not pre-registered): alignment oracle, PMI table, closing link, language, geometry, length
cd "$(dirname "$0")"
until [ -z "$(pgrep -f 'run21.py probe pr_en599_21x23')" ]; do sleep 5; done
P="nclimb=5 nbasin=8 bmax=4 climb=1"
python3 -I run21.py probe pr_es615_16x18_or es 615 16 18 3 3 ptag=P_es615_16x18 oracle=1 ${=P}
python3 -I run21.py probe pr_es615_16x18_pmi es 615 16 18 3 3 ptag=P_es615_16x18 pmi=1 ${=P}
python3 -I run21.py probe pr_es615_16x18_i1 es 615 16 18 3 3 ptag=P_es615_16x18 idp=1 ${=P}
python3 -I run21.py probe pr_en615_16x18_c1 en 615 16 18 3 3 ptag=P_en615_16x18 ${=P}
python3 -I run21.py probe pr_es612_16x18_c1 es 612 16 18 3 3 ptag=P_es612_16x18 ${=P}
python3 -I run21.py probe pr_es608_16x18_c1 es 608 16 18 3 3 ptag=P_es608_16x18 ${=P}
python3 -I run21.py probe pr_en1000_19x20_c1 en 1000 19 20 3 3 ptag=P_en1000_19x20 ${=P}
echo chain2-done
