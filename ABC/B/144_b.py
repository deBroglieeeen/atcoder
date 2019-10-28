import sys
n = int(input())
ans = "No"
if n > 81:
  print("No")
else:
  for i in range(1,10):
    for j in range(1,10):
      if i * j == n:
        ans = "Yes"
  print(ans)