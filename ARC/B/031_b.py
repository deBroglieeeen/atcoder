# pythonではそのまま代入すると参照がわたされてしまう
import copy
chart = [list(input()) for _ in range(10)]
model = [["x"]*10 for _ in range(10)]
ans = "NO"

def check(x,y,reached):
  if x < 0 or y < 0 or x >= 10 or y >= 10:
    return 0
  if reached[y][x] == "x":
    return 0
  reached[y][x] = "x"
  return 1

for t in range(10):
  for u in range(10):
    # pythonではそのまま代入すると参照がわたされてしまう
    reached = copy.deepcopy(chart)
    # シンプルにoをつけたところから始めれば良い
    stack = [[t,u]]
    while len(stack) != 0:
      # popすることによって再帰関数で実現していたグラフを戻るということがスタックによっても実現できる
      x,y = stack.pop()
      # 今回はグリッドなので4方向だがグラフであればまた数や方向が変わるかも
      # 右
      if check(x + 1, y,reached):
        stack.append([x + 1, y])
      # 左
      if check(x - 1, y,reached):
        stack.append([x - 1, y])
      # 下
      if check(x, y + 1,reached):
        stack.append([x, y + 1])
      # 上
      if check(x, y - 1,reached):
        stack.append([x, y - 1])
    # 全てをxにできたら埋めたてられたということ
    if reached == model:
      ans = "YES"

print(ans)