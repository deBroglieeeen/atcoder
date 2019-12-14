a,b,x = map(int,input().split())
ans = 0
def get_mul(n,x):
  if n == -1:
    return 0
  else:
    return n // x + 1
if b == 0:
  print(1)
else:
  print(get_mul(b,x) - get_mul(a - 1,x))