n = int(input())
h = list(map(int,input().split()))
max_move = 0
pre = h[0]
move = 0
for i in range(1,n):
  if pre < h[i]:
    max_move = max(max_move,move)
    move = 0
    pre = h[i]
  else:
    move += 1
    pre = h[i]
max_move = max(max_move,move)
print(str(max_move))