n = int(input())
al = []
if n == 0:
  print("0")
else:
  while n:
    if n % 2 != 0:
      n -= 1
      al.append("1")
    else:
      al.append("0")
    n /= -2
  al.reverse()
  print("".join(al))