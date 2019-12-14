n,x = map(int,input().split())
products = list(map(int,input().split()))
ans_l = []
for i in range(n):
  if x >> i & 1:
    ans_l.append(products[i])
print(sum(ans_l))