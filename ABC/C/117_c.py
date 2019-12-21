from collections import deque
n,m = map(int,input().split())
X = sorted(list(map(int,input().split())))
diffs = deque()
if m <= n:
  print(0)
else:
  for i in range(m - 1):
    diffs.append(X[i + 1] - X[i])
  diffs = deque(sorted(diffs,reverse = True))
  for i in range(n - 1):
    diffs.popleft()
  print(sum(diffs))