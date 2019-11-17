import sys
n = int(input())
s = input()
a = ""
b = ""
if n % 2 != 0:
  print("No")
  sys.exit()
else:
  for i in range(n):
    if i <= n / 2 - 1:
      a += s[i]
    else:
      b += s[i]
if a == b:
  print("Yes")
else:
  print("No")