h,w = map(int,input().split())
maze = [list(input()) for _ in range(h)]
is_reached = [[0]*w for _ in range(h)]


def dfs(x,y):
  #print(str(x)+str(y))
  if 0 > x or 0 > y  or y > h -  1 or x > w - 1:
    #print(str(x)+str(y))
    return
  if maze[y][x] == "#":
    return
  #if maze[x][y] == "d":
  if is_reached[y][x] == 1:
    return
  # if maze[y][x] == "g":
  #   print("Yes")
  #   sys.exit()
  #maze[x][y] == "d"
  is_reached[y][x] == 1
  dfs(x + 1, y)   # 右方向に移動
  dfs(x - 1, y)   # 左方向に移動
  dfs(x, y + 1)   # 下方向に移動
  dfs(x, y - 1)   # 上方向に移動

#start_i = 0
#start_j = 0

#goal_i = 0
#goal_j = 0

s_position = [0,0]
g_position = [0,0]

for i in range(h):
  if "g" in maze[i]:
    g_position = [i,maze[i].index("g")]
for i in range(h):
  if "s" in maze[i]:
    s_position = [i,maze[i].index("s")]

# def getS():
#   for i in range(h):
#     for j in range(w):
#       if maze[i][j] == "s":
#         start_i = i
#         start_j = j
#         return
# getS()
#dfs(start_i,start_j)
dfs(s_position[0],s_position[1])
if is_reached[g_position[0]][g_position[1]]:
  print("Yes")
else:
  print("No")