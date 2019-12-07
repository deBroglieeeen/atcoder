a = int(input())
b = int(input())
n = int(input())
def gcd(a,b):
  if b == 0:
    return a
  return gcd(b,a%b)
def lcm(a,b):
  return a * b // gcd(a,b)
l_c = lcm(a,b)
if n % l_c == 0:
  print((n // l_c) * l_c)
else:
  print((n // l_c + 1) * l_c)