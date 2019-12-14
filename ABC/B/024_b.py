n,t = map(int,input().split())
A = [int(input()) for _ in range(n)]
ans = t
for i in range(1,n):
  ans += min(t,A[i] - A[i - 1])
print(ans)