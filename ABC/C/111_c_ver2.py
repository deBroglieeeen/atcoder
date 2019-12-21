import itertools
from collections import Counter
N = int(input())
V = list(map(int,input().split()))
even_counter = Counter(V[::2])
odd_counter = Counter(V[1::2])
even_counter[-1] = 0
odd_counter[-1] = 0
even = even_counter.most_common(2)
odd = odd_counter.most_common(2)
ans = N
for (k1,v1),(k2,v2) in itertools.product(even,odd):
  if k1 == k2:
    continue
  ans = min(ans,N - v1 - v2)
print(ans)