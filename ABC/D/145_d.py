from operator import mul
from functools import reduce
import sys
x,y = map(float,input().split())
m = (2*x - y)/3
n = (y - m)/2
if not (m.is_integer() and n.is_integer()):
  print(0)
  sys.exit()
if n < 0 or m < 0:
  print(0)
  sys.exit()
m = int(m)
n = int(n)
mod = 10**9 + 7
def cmb(h, r):
    if h - r < r: r = h - r
    if r == 0: return 1
    if r == 1: return h
    r = int(r)

    humerator = [h - r + k + 1 for k in range(r)]
    dehominator = [k + 1 for k in range(r)]

    for p in range(2,r+1):
        pivot = dehominator[p - 1]
        if pivot > 1:
            offset = (h - r) % p
            for k in range(p-1,r,p):
                k = int(k)
                offset = int(offset)
                humerator[k - offset] /= pivot
                dehominator[k] /= pivot

    result = 1
    for k in range(r):
        if humerator[k] > 1:
            result *= int(humerator[k])

    return result
if (x + y) % 3 != 0:
  print(0)
else:
  print(cmb(n + m,n)%mod)