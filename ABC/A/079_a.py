n = list(input())
ans = "No"
pre = n[0]
length = 1
for i in range(1,4):
  if pre == n[i]:
    length += 1
  else:
    length = 1
  pre = n[i]
  if length >= 3:
    ans = "Yes"
print(ans)