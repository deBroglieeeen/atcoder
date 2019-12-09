import math
n = int(input())
for i in range(n * 5000):
  if i * i == n:
    print(i**2)
    break
  elif i * i > n:
    print((i-1) ** 2)
    break