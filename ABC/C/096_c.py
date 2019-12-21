H,W = map(int,input().split())
black_count = 0
board = []
got_start = False
ans = "Yes"
#　注意[[False]*W]*Hだと行ごとに参照渡しになる！！
#reached = [[False]*W for _ in range(H)]
start_point = None
for h in range(H):
  row = tuple(input())
  if "#" in row:
    index = row.index("#")
    if got_start == False:
      start_point = (h,index)
      got_start = True
  board.append(row)

def check(y,x):
  if y >= H or y < 0 or x >= W or x < 0:
    return 0
  if board[y][x] == "#":
    return 1

for i in range(H):
  for j in range(W):
    y,x = i,j
    if board[i][j] == ".":
      continue
    is_adjacent = False
    if check(y + 1,x):
      is_adjacent = True
    if check(y - 1,x):
      is_adjacent = True
    if check(y, x + 1):
      is_adjacent = True
    if check(y,x - 1):
      is_adjacent = True
    if is_adjacent == False:
      ans = "No"
print(ans)