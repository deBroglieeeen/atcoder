n,k = map(int,input().split())
def gcd(a,b):
  if b == 0:
    return a
  return gcd(b,a % b)
def lcm(a,b):
  return a * b // gcd(a,b)
if k % 2 != 0:
  elements = n // k
  print(elements**3)
else:
  a = n // k
  b = (n + (k//2)) // k
  print(a**3 + b ** 3)