board = [input() for _ in range(4)]
for i in range(1,5):
  print(board[-i][::-1])