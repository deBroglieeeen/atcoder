s = list(input())
ac = 0
bc = 0
cc = 0
for i in s:
  if i == "a":
    ac += 1
  elif i == "b":
    bc += 1
  elif i == "c":
    cc += 1
if ac == 1 and bc == 1 and cc == 1:
  print("Yes")
else:
  print("No")