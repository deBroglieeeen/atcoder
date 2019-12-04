board = [list(input().split()) for _ in range(4)]
def swap():
  board[0],board[1],board[2],board[3] = board[3],board[2],board[1],board[0]
  for i in range(4):
    board[i][0],board[i][1],board[i][2],board[i][3] = board[i][3],board[i][2],board[i][1],board[i][0]
  return board
swapped = swap()
for i in range(4):
  print(" ".join(board[i]))