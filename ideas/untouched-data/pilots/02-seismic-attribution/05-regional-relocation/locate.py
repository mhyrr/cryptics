"""Exp 05: locate a source from 1-5 Hz envelopes at regional stations (back-projection).

Method v1, fixed before any run on Poli's residual:
  stations   BHZ/HHZ within 5 degrees of the search centre, EarthScope FDSN, at most 60 nearest
  record     [T-300 s, T+600 s] around a rough time T
  envelope   |bandpass 1-5 Hz|, 10 s running mean, 1 sample/s, divided by its own maximum
  keep       stations whose peak is >= 5x the median of the first 200 s
  grid       0.1 degree nodes within 4 degrees of the search centre
  stack      mean over stations of envelope(t0 + distance / 3.3 km/s); maximise over node and t0
Outputs the best node, its stack value, the number of stations kept, and the stack value at
the second-best node more than 100 km away (a contrast measure).
"""
import math, sys, warnings

import numpy as np
from obspy import UTCDateTime
from obspy.clients.fdsn import Client

warnings.filterwarnings("ignore")
V, PRE, POST, RAD_DEG, STEP = 3.3, 300, 600, 4.0, 0.1
_client = None


def client():
    global _client
    if _client is None:
        _client = Client("EARTHSCOPE", timeout=120)
    return _client


def hav(lat1, lon1, lat2, lon2):
    p1, p2 = np.radians(lat1), np.radians(lat2)
    a = np.sin((p2 - p1) / 2) ** 2 + np.cos(p1) * np.cos(p2) * np.sin(np.radians(lon2 - lon1) / 2) ** 2
    return 6371.0 * 2 * np.arcsin(np.sqrt(a))


def envelopes(clat, clon, T):
    T = UTCDateTime(T)
    try:
        inv = client().get_stations(latitude=clat, longitude=clon, maxradius=5.0, channel="BHZ,HHZ", level="station",
                                    starttime=T - PRE, endtime=T + POST)
    except Exception:
        return []
    sta = {(n.code, s.code): (s.latitude, s.longitude) for n in inv for s in n}
    near = sorted(sta, key=lambda k: hav(clat, clon, *sta[k]))[:60]
    try:
        st = client().get_waveforms_bulk([(n, s, "*", "BHZ,HHZ", T - PRE, T + POST) for n, s in near])
    except Exception:
        return []
    out, seen = [], set()
    n_s = PRE + POST
    for tr in st:
        key = (tr.stats.network, tr.stats.station)
        if key in seen or key not in sta:
            continue
        try:
            tr.detrend("demean"); tr.taper(0.02); tr.filter("bandpass", freqmin=1, freqmax=5)
        except Exception:
            continue
        sr = tr.stats.sampling_rate
        off = int(round((tr.stats.starttime - (T - PRE))))
        w = int(10 * sr)
        if tr.stats.npts < 0.9 * n_s * sr or w < 1:
            continue
        sm = np.convolve(np.abs(tr.data), np.ones(w) / w, "same")
        sec = sm[: int(len(sm) // sr * sr)].reshape(-1, int(sr)).mean(axis=1) if float(sr).is_integer() else sm[:: int(round(sr))]
        env = np.zeros(n_s); m = min(n_s - max(off, 0), len(sec))
        if m <= 0:
            continue
        env[max(off, 0): max(off, 0) + m] = sec[:m]
        noise = np.median(env[:200]) or 1e-12
        if env.max() / noise < 5:
            continue
        seen.add(key)
        out.append((sta[key][0], sta[key][1], env / env.max()))
    return out


def locate(clat, clon, T):
    envs = envelopes(clat, clon, T)
    if len(envs) < 5:
        return dict(nsta=len(envs))
    slat = np.array([e[0] for e in envs]); slon = np.array([e[1] for e in envs]); E = np.stack([e[2] for e in envs])
    n_t = E.shape[1]
    t0s = np.arange(0, n_t - 200)
    lats = np.arange(clat - RAD_DEG, clat + RAD_DEG + 1e-9, STEP)
    lons = np.arange(clon - RAD_DEG / max(math.cos(math.radians(clat)), 0.2), clon + RAD_DEG / max(math.cos(math.radians(clat)), 0.2) + 1e-9,
                     STEP / max(math.cos(math.radians(clat)), 0.2))
    best = np.zeros((len(lats), len(lons))); bt = np.zeros_like(best)
    rows = np.arange(len(envs))[:, None]
    for i, la in enumerate(lats):
        for j, lo in enumerate(lons):
            sh = np.rint(hav(la, lo, slat, slon) / V).astype(int)
            idx = t0s[None, :] + sh[:, None]
            ok = idx < n_t
            s = (E[rows, np.minimum(idx, n_t - 1)] * ok).mean(axis=0)
            k = s.argmax(); best[i, j] = s[k]; bt[i, j] = t0s[k]
    i, j = np.unravel_index(best.argmax(), best.shape)
    d = hav(lats[i], lons[j], lats[:, None], lons[None, :])
    second = best[d > 100].max() if (d > 100).any() else float("nan")
    return dict(nsta=len(envs), lat=float(lats[i]), lon=float(lons[j]), stack=float(best[i, j]), contrast=float(best[i, j] - second),
                t0=str(UTCDateTime(T) - PRE + float(bt[i, j])), near_km=float(hav(lats[i], lons[j], slat, slon).min()))


if __name__ == "__main__":
    print(locate(float(sys.argv[1]), float(sys.argv[2]), sys.argv[3]))
