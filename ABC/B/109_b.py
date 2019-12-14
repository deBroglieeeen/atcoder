n = int(input())
W = [input() for _ in range(n)]
ans = "Yes"
if len(W) != len(set(W)):
  print("No")
else:
  for i in range(n - 1):
    if W[i][-1] != W[i + 1][0]:
      ans = "No"
  print(ans)