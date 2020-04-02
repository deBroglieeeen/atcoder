from scipy.sparse.csgraph import dijkstra
# 2部グラフの最大流問題で解く
N = int(input())
NN = N * 2
XY = [[int(x) for x in input().split()] for _ in range(NN)]
# なぜ2倍大きなグラフを用意する？
graph = [[0] * (NN+2) for _ in range(NN+2)]
start = NN
goal = NN + 1

for i,(a,b) in enumerate(XY[:N]):
  for j,(c,d) in enumerate(XY[N:],N):
    if a < c and b < d:
      graph[i][j] = 1

for i in range(N):
  graph[start][i] = 1
for i in range(N,NN):
  graph[i][goal] = 1

INF = 10 ** 9

def max_flow(graph):
  dist,pred = dijkstra(graph,indices = start,return_predecessors = True)
  if dist[goal] > INF:
    return 0
  y = goal
  while y != start:
    x = pred[y]
    graph[x][y] -= 1
    graph[y][x] += 1
    y = x
  return 1 + max_flow(graph)

answer = max_flow(graph)
print(answer)