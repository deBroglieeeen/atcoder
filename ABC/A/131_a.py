s = list(input())
pre = ""
ans = "Good"
for i in s:
  if pre == i:
    ans = "Bad"
  pre = i
print(ans)