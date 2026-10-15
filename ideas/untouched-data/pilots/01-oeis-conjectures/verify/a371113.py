# Third check, main thread: Hasler's OEIS Python program for A371113, ported line for line,
# with a set mirroring the list for membership (same logic, faster). Checks Conjecture 3.
import sys
N = int(sys.argv[1])
T, U, least = [], set(), 0
while len(T) < N:
    if len(T) % 3 < 2:
        x = least
        T.append(x); U.add(x)
        while x + 1 in U: x += 1
        least = x + 1
    else:
        suffix = (str(T[-2]) + str(T[-1]))[::-1]
        for i in range(1, len(suffix) + 1):
            if suffix[-i] != '0' and (s := suffix[:-i-1:-1] + suffix) == s[::-1] and (x := int(suffix[-i:])) not in U: break
        else:
            x = int('1' + suffix); assert x not in U
        T.append(x); U.add(x); assert x > least
data = [0,1,10,2,3,32,4,5,54,6,7,76,8,9,98,11,12,111,13,14,131,15,16,151,17]
assert T[:len(data)] == data, "does not reproduce %S"
bad = [k for k in range(N // 3) if T[3*k+1] - T[3*k] not in (1, 2)]
print("terms", N, "first violations k:", bad[:5], "count", len(bad))
for k in bad[:2]:
    print(f"k={k}: a({3*k})={T[3*k]}, a({3*k+1})={T[3*k+1]}, a({3*k+2})={T[3*k+2]}; "
          f"between: {[(v, T.index(v)) for v in range(T[3*k]+1, T[3*k+1])]}")
