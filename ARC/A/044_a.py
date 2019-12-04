n = int(input())
if n == 2 or n == 3 or n == 5:
  print("Prime")
elif n == 1:
  print("Not Prime")
elif n % 2 != 0 and n % 3 != 0 and n % 5 != 0:
  print("Prime")
else:
  print("Not Prime")