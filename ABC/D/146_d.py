import numpy as np
import sys
sys.setrecursionlimit(10**7)
n = int(input())
edge = [tuple(map(int,input().split()))for _ in range(n - 1)]
T = [[] for _ in range(n)]
for i,(a,b) in enumerate(edge):
  # 木といいつつ有向グラフのように処理
  T[a -1].append([b - 1,i])
  #T[b - 1].append([a - 1,i])
ans = [None] * (n - 1)
def rec(cur,color):
  cnt = 1
  for (to,j) in T[cur]:
    if cnt == color:
      cnt += 1
    ans[j] = cnt
    rec(to,cnt)
    cnt += 1
rec(0,0)
print(max(ans))
[print(a) for a in ans]