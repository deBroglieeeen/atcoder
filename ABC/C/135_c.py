n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
ans = 0
if a[0] >= b[0]:
  ans += b[0]
  a[0] -= a[0] - b[0]
  b[0] = 0
else:
  ans += a[0]
  a[0] = 0
  b[0] -= a[0]
for i in range(1,n):
  # if a[i] >= b[i]:
  #   ans += b[i]
  # else:
  #   ans += a[i]
  #   b[i] -= a[i]
  if b[i - 1] != 0:
    if a[i] >= b[i - 1]:
      ans += b[i - 1]
      a[i] -= a[i] - b[i - 1]
      b[i - 1] = 0
      if a[i] >= b[i]:
        ans += b[i]
        a[i] -= a[i] - b[i]
        b[i] = 0
      else:
        ans += a[i]
        a[i] = 0
        b[i] -= a[i]
    else:
      ans +=  a[i]
      a[i] = 0
      b[i - 1] -= a[i]
  else:
    if a[i] >= b[i]:
      ans += b[i]
      a[i] -= a[i] - b[i]
      b[i] = 0
    else:
      ans += a[i]
      a[i] = 0
      b[i] -= a[i]