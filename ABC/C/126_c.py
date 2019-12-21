n,k = map(int,input().split())
win = 0
for i in range(1,n + 1):
  cnt = 0
  point = i
  while point < k:
    point *= 2
    cnt += 1
  win += (1 / 2) ** cnt
print(win / n)