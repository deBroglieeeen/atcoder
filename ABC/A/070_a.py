n = list(input())
ans = "Yes"
for i in range(3):
  if n[i] != n[-i -1]:
    ans = "No"
print(ans)