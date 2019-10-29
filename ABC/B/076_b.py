# 貪欲法で解く貪欲法とは次の状態の値を最適にすることだけを考えること
n = int(input())
k = int(input())
shown = 1
def manA(x):
  return 2 * x

def manB(x):
  return k + x

for _ in range(n):
  shown = min(manA(shown),manB(shown))

print(shown)