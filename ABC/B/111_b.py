n = input()
if len(set(n)) == 1:
  print(n)
else:
  x = n[0]
  if int(n) < int(x*3):
    print(x*3)
  else:
    print(str(int(n[0]) + 1)*3)