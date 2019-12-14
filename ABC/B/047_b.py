# https://atcoder.jp/contests/abc047/submissions/8775121 のコードが秀逸
w,h,n = map(int,input().split())
mans = [list(map(int,input().split())) for _ in range(n)]
X = [i for i in range(w + 1)]
Y = [i for i in range(h + 1)]
def flatten(nested_list):
  return [e for inner_list in nested_list for e in inner_list]
remove_X = []
remove_Y = []
for i in range(n):
  x = mans[i][0]
  y = mans[i][1]
  a = mans[i][2]
  if a == 1:
    remove_X.append(X[:x])
  elif a == 2:
    remove_X.append(X[x + 1:])
  elif a== 3:
    remove_Y.append(Y[:y])
  else:
    remove_Y.append(Y[y + 1:])
dis_X = set(flatten(remove_X))
dis_Y = set(flatten(remove_Y))
for x in dis_X:
  X.remove(x)
for y in dis_Y:
  Y.remove(y)
if len(X) == 0 or len(Y) == 0:
  print(0)
else:
  print((max(X) - min(X)) * (max(Y) - min(Y)))