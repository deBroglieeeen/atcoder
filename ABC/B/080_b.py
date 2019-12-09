n = int(input())
sn = sum(list(map(int,list(str(n)))))
if n % sn == 0:
  print("Yes")
else:
  print("No")