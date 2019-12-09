n,m = map(int,input().split())
tree = [[] for _ in range(n)]
for i in range(m):
  start,to = map(int,input().split())
  tree[start - 1].append(to - 1)
  tree[to - 1].append(start - 1)
for i in range(n):
  print(len(tree[i]))