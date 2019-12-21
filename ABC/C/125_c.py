n = int(input())
A = list(map(int,input().split()))
def gcd(a,b):
  if b == 0:
    return a
  return gcd(b,a%b)
L = [1]*n
R = [1]*n
L[0] = A[0]
R[n - 1] = A[-1]
for i in range(1,n):
  L[i] = gcd(L[i - 1],A[i])
  R[n - i - 1] = gcd(R[n - i],A[-1 - i])
m = 1
for i in range(0,n-2):
  m = max(m,gcd(L[i],R[i + 2]))
print(max(L[n - 2],m,R[1]))