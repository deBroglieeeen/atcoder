#import copy
# 最大値が2つ以上あるものと1つしかないもので場合分けをする
n = int(input())
a = [int(input()) for _ in range(n)]
b = sorted(a)
if b[-1] == b[-2]:
  for i in range(n):
    print(b[-1])
else:
  p = a.index(b[-1])
  for i in range(n):
    if i == p:
      print(b[-2])
    else:
      print(b[-1])
#deepcopy is so slow!!
# ex_a = []
# for i in range(n):
#   ex_a = copy.deepcopy(a)
#   ex_a[i] = -1
#   print(max(ex_a))