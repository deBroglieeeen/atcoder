n,x = map(int,input().split())
# gcdは結合法則が成り立つ つまりどこから計算をはじめても同じ
X = tuple(map(int,input().split()))
def gcd(a,b):
  if b == 0:
    return a
  return gcd(b,a % b)
diff_gcd = abs(x - X[0])
for i in range(n - 1):
  diff_gcd = gcd(diff_gcd,abs(X[i + 1] - X[i]))
print(diff_gcd)