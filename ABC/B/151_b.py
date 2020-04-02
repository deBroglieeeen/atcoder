n,k,m = map(int,input().split())
A = list(map(int,input().split()))
x = n * m - sum(A)
if x <= 0:
  print(0)
elif x > k:
  print(-1)
else:
  print(x)