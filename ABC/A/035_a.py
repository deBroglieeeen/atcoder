w,h = map(int,input().split())
def gcd(a,b):
  if b == 0:
    return a
  return gcd(b,a%b)
div = gcd(w,h)
if div == 1:
  print(str(w)+":"+str(h))
else:
  print(str(w//div)+":"+str(h//div))