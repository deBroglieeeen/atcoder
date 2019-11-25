upper = list(input())
lower = list(input())
ans = "YES"
for i in range(3):
  if upper[i] != lower[-i-1]:
    ans = "NO"
print(ans)