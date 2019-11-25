import sys
a,b,x = map(int,input().split())
limit = 10**9
ans = 0
for d in range(1,10):
  n = (x - (b * d)) // a
  #if n <= limit and len(str(n)) == d:
    #ans = max(ans,n)
  #elif n > limit:
    #ans = limit
  # nが求まることとxが求まることは別物
  if 10**(d - 1) <= n < 10**d:
    ans = n
  elif n >= 10**d:
    # なぜ10**9-1は条件を満たすといいきれる？
    ans = 10**d-1
if x>=a*limit + b*10:
  ans = limit
print(ans)