import numpy as np
n = int(input())
ans = 0
field = [map(int,input().split()) for _ in range(n)]
x,y,z = 0,0,0
# 1つ前の値のみわかればよいので
# aにはa,a,aがbには
for a,b,c in field:
  #x,y,zは毎回入れ替わるので活動は連続しない
  x,y,z = max(y,z) + a,max(x,z) + b,max(x,y) + c

print(max(x,y,z))