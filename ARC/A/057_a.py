a,k =map(int,input().split())
target = 2 * 10**12
ans = 0
total = a
if k == 0:
  ans = target - a
  print(ans)
else:
  while total < target:
    total += total * k + 1
    ans += 1
  print(ans)