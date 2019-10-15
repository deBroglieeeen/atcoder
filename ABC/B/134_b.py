n,d = map(int,input().split())
k = d + 1
ans = 0
isnegetive = False
while isnegetive == False:
  ans += 1
  x = n - (k + d)
  k = k + d + 1 + d
  if x <= 0:
    isnegetive = True
  
print(ans)

# 別解
# 1人の監視員を配置すると連続した2D+1本の木を監視できる
# つまり答えはNを2D+1で割った切り上げ
# 一般的に整数A,Bに対してA/Bの切り上げはA+B-1/Bの商と等しい
# つまり今回はN+2D/2D+1が答え
# よって実装はこうなる
n,d = map(int,input().split())
print((n+2*d)/(2*d+1))