# 部分文字列をはじめる場所をkという0 <= k <= s-t の変数を使って補助してあげる考え方
# greedyというのはkを決定する際に大きい方からきめていくことがgreedyなのか
# いや16行目の部分か
# pythonはindexでstringの文字を変更できない
s = list(input())
t = list(input())
x = 0
ans = []
gotk = False

# pythonて関数にするとスコープの外の変数参照できないんだっけ？

# 0 <= k <= s - t
def match(k):
  for i in range(len(t)):
    if s[i + k] != t[i] and s[i + k] != "?":
      return False
  return True

def construct(k,s):
  for i in range(len(t)):
    s[i + k] = t[i]
  for i in range(len(s)):
    if s[i] == "?":
      s[i] = "a"
  return s

# 大きいkから探せば良い(今回逆順にしてるためrangeの第二引数が直前まで処理されることに注意！)
for i in range(len(s) - len(t),-1,-1):
  if match(i):
    x = i
    gotk = True
    break

if gotk == True:
  ans = construct(x,s)
  print("".join(ans))
else:
  print("UNRESTORABLE")