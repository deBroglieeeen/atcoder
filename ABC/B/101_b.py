n = list(input())
i_n = int("".join(n))
s = list(map(int,n))
if i_n % sum(s) == 0:
  print("Yes")
else:
  print("No")