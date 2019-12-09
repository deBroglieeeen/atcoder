n,m,x = map(int,input().split())
A = list(map(int,input().split()))
# xより小さい料金所と大きい料金所の数をかぞえたら終了
left = 0
right = 0
for a in A:
  if a < x:
    left += 1
  else:
    right += 1
print(min(left,right))