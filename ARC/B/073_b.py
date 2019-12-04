# A%B,2A%B,3A%B.....
#(k + b)a % b = (k * a + b * a) % b = k * a % b
a,b,c = map(int,input().split())
ans = "NO"
for i in range(a,a*b,a):
  if i % b == c:
    ans = "YES"
print(ans)