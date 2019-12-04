n = int(input())
a = [int(input())for _ in range(n)]
ans = 0
num = 1
for i in range(n + 1):
  ans += 1
  if a[num - 1] == 2:
    break
  else:
    num = a[num - 1]
  if i == n:
    ans = -1
print(ans)