n = int(input())
A = list(map(int,input().split()))
def gcd(a,b):
  if b == 0:
    return a
  return gcd(b,a % b)
cur = A[0]
for i in range(1,len(A)):
  cur = gcd(cur,A[i])
print(cur)