h,w = map(int,input().split())
board = [list(input()) for _ in range(h)]
x = (-1,0,1,0,-1,1,-1,1)
y = (0,-1,0,1,-1,-1,1,1)
for i in range(h):
  for j in range(w):
    if board[i][j] == "#":
      continue
    else:
      cnt = 0
      for k in range(8):
        if 0 > i + y[k] or i + y[k] >= h or 0 > j + x[k] or j + x[k] >= w:
          continue
        else:
          if board[i + y[k]][j + x[k]] == "#":
            cnt += 1
      board[i][j] = str(cnt)
for i in range(h):
  print("".join(board[i]))