from functools import reduce
n = int(input())
a = list(map(int,input().split()))
ans = 0
def gcd(a,b):
  if (b == 0):
    return a
  return gcd(b,a%b)

def lcm(a,b):
  return a * b // gcd(a,b)

def get_lcm(numbers):
  return reduce(lcm,numbers)
l = get_lcm(a) - 1
for i in range(n):
  ans += l % a[i]
print(ans)