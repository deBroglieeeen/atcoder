import sys
a,b,x = map(int,input().split())
limit = 1000000000
ans = 0
for d in range(10,0,-1):
  n = (x - (b * d)) // a
  if n <= limit and len(str(n)) == d:
    ans = max(ans,n)
  elif n > limit:
    ans = limit
print(ans)