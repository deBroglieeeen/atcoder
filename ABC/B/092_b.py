n = int(input())
d,x = map(int,input().split())
A = [int(input()) for _ in range(n)]
ans = 0
for i in range(n):
  cnt = 0
  for j in range(d):
    if A[i] * j + 1 <= d:
      ans += 1
    else:
      break
print(ans + x)