"""Independent re-decrypt (criterion 3): uses only transpo.py (pure Python), never the C solver.
Usage: python3 verify.py CT_FILE K1 K2 CONV   (keys as comma-separated ranks)"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "../01-solver"))
import transpo
ct = "".join(c for c in open(sys.argv[1]).read().upper() if c.isalpha())
k1 = [int(x) for x in sys.argv[2].split(",")]; k2 = [int(x) for x in sys.argv[3].split(",")]
print(transpo.double_dec(ct, k1, k2, sys.argv[4]))
