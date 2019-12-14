n,s,t = map(int,input().split())
w = 0
A = [int(input()) for _ in range(n)]
ans = 0
for i in range(0,n):
  w += A[i]
  if s <= w <= t:
    ans += 1
print(ans)