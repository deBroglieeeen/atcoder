S = input()
t = int(input())
move = {"L":(-1,0),"R":(1,0),"U":(0,1),"D":(0,-1)}
X = 0
Y = 0
u_cnt = 0
for s in S:
  # ?は最後に処理しないとどちらに動くのが最適かわからない
  if s == "?":
    u_cnt += 1
  else:
    x,y = move[s]
    X += x
    Y += y
for i in range(u_cnt):
    if t == 1:
      if abs(X + 1) > abs(X - 1):
        X += 1
      else:
        X -= 1
    else:
      if X == 0:
        if abs(Y + 1) < abs(Y - 1):
          Y += 1
        else:
          Y -= 1
      elif abs(X + 1) < abs(X - 1):
        X += 1
      elif abs(X + 1) > abs(X - 1):
        X -= 1
print(abs(X) + abs(Y))