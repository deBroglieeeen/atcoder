n = int(input())
if len(str(n)) == 1:
  print(n)
elif len(str(n)) == 2:
  print(9)
elif len(str(n)) == 3:
  print(9+(n-100+1))
elif len(str(n)) == 4:
  print(9+900)
elif len(str(n)) == 5:
  print(909+(n-10000+1))
elif len(str(n)) == 6:
  print(90909)