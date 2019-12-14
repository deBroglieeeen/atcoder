n = int(input())
T = tuple(map(int,input().split()))
m = int(input())
drinks = [list(map(int,input().split())) for _ in range(m)]
ans_list = []
# python はmutable objectは参照渡しにimutable object(tuple等)は値渡しになる
def swap(p,x):
  # Tのコピーのリストが渡される
  temp = list(T)
  temp[p - 1] = x
  return temp
for i in range(m):
  p,x = drinks[i][0],drinks[i][1]
  new = swap(p,x)
  ans_list.append(sum(new))
for ans in ans_list:
  print(ans)