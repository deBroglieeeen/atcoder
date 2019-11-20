n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
ans = 0
pre = -100
for i in range(n):
  ans += b[a[i] - 1]
  if pre == a[i] - 1:
    ans += c[pre - 1]
  pre = a[i]
print(ans)