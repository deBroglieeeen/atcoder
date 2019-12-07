n = int(input())
k = int(input())
x = int(input())
y = int(input())
ans = 0
if n > k:
  ans += x * k
  ans += y * (n - k)
else:
  ans += x * n
print(ans)