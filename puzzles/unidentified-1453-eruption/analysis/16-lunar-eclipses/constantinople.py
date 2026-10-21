"""Geometry of the 22 May 1453 (Julian) partial lunar eclipse as seen from Constantinople,
to compare with Barbaro's account (moon rose 'like a three-day moon' at about one hour
of night, stayed so about four hours, round again by six hours of night).

Usage: python3 -I constantinople.py data/LE1401-1500.html > results/constantinople_1453.txt

Approximations (stated, not hidden): sub-lunar point from the NASA catalog at greatest
eclipse, moved west at 14.49 deg/h; the Sun is taken as antipodal to the Moon (true to
~1 deg at an eclipse); refraction and lunar parallax ignored (each < 1 deg).
Italian/Venetian hours of the night are counted from sunset (some usage counts from
~30 min after sunset; both are shown).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from eclipses import ROW, RATE, alt  # noqa: E402

LAT, LON = 41.01, 28.98


def hm(x):
    m = round(x * 60) % 1440
    return f"{m // 60:02d}:{m % 60:02d}"


def main(path):
    html = open(path, encoding="latin-1").read()
    for m in ROW.finditer(html):
        g = m.groups()
        if (g[1], g[2], g[3]) != ("1453", "May", "22"):
            continue
        td = int(g[4]) + int(g[5]) / 60 + int(g[6]) / 3600
        ut = td - int(g[7]) / 3600
        pen, par = float(g[15]) / 60, float(g[16]) / 60
        slat = int(g[18]) * (1 if g[19] == "N" else -1)
        slon = int(g[20]) * (1 if g[21] == "E" else -1)
        off = LON / 15
        contacts = {"P1": ut - pen / 2, "U1": ut - par / 2, "Greatest": ut, "U4": ut + par / 2, "P4": ut + pen / 2}

        def a(t):
            return alt(LAT, LON, slat, slon - RATE * (t - ut))

        t = ut - 3
        while a(t) < 0:
            t += 1 / 600
        moonrise = t
        print(f"Eclipse 1453 May 22 (Julian), umbral mag {g[14]}, greatest {hm(ut)} UT")
        print(f"Constantinople LMT = UT + {off * 60:.0f} min")
        print(f"Moonrise (geometric, Sun antipodal => ~sunset): {hm(moonrise + off)} LMT")
        for k, v in contacts.items():
            print(f"{k:9s} {hm(v + off)} LMT  moon alt {a(v):5.1f} deg  hours after moonrise/sunset {v - moonrise:+.2f}")
        print()
        print("Barbaro: crescent-like at moonrise ('one hour of night'), lasting ~4 h, round by 6 h of night.")
        print(f"Computed: umbral phase ends {contacts['U4'] - moonrise:.2f} h after moonrise; "
              f"penumbral phase ends {contacts['P4'] - moonrise:.2f} h after moonrise.")
        print(f"Barbaro's 'round by 6 h of night' = {hm(moonrise + 6 + off)} LMT (from sunset) "
              f"or {hm(moonrise + 6.5 + off)} LMT (from sunset + 30 min).")


if __name__ == "__main__":
    main(sys.argv[1])
