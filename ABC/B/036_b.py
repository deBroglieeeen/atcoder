n = int(input())
board = [input() for _ in range(n)]
rotated = []
for i in range(n):
  for j in range(n):
    rotated.append(board[-j - 1][i])
for i in range(n):
  print("".join(rotated[i * n:n * (i + 1)]))