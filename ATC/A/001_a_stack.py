h,w = map(int,input().split())
maze = [input() for _ in range(h)]
reached = [[0] * w  for i in range(h)]

s_position = [0,0]
g_position = [0,0]

for i in range(h):
  if "s" in maze[i]:
    # y
    s_position[1] = i
    # x
    s_position[0] = maze[i].index("s")
  if "g" in maze[i]:
    # y
    g_position[1] = i
    # x
    g_position[0] = maze[i].index("g")

stack = [[s_position[0],s_position[1]]]

def check(x,y):
  if x < 0 or x > w - 1 or y < 0 or y > h - 1:
    return 0
  if maze[y][x] == "#":
    return 0
  if reached[y][x] == 1:
    return 0
  return 1

while len(stack) != 0:
  x,y = stack.pop()
  reached[y][x] = 1
  # ４方向を探索

  # 右
  if check(x + 1, y):
    stack.append([x + 1, y])
  # 左
  if check(x - 1, y):
    stack.append([x - 1, y])
  if check(x, y + 1):
  # 下
    stack.append([x, y + 1])
  # 上
  if check(x, y - 1):
    stack.append([x, y - 1])

if reached[g_position[1]][g_position[0]] == 1:
  print("Yes")
else:
  print("No")