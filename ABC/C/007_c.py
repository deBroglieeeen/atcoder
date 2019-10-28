from collections import deque
r,c = map(int,input().split())
sy,sx = map(int,input().split())
gy,gx = map(int,input().split())
maze = [input() for _ in range(r)]
que = deque([(sx - 1,sy - 1)])
dist = [[-1]*c for _ in range(r)]
dist[sy - 1][sx - 1] = 0

def check(x,y):
  if x < 0 or y < 0 or x >= c or y >= r:
    return 0
  if maze[y][x] == "#":
    return 0

  return 1


while len(que) != 0:
  x,y = que.popleft()
  if check(x + 1,y):
    dist[y][x + 1] = dist[y][x] + 1
    que.append((x + 1,y))
  if check(x - 1,y):
    dist[y][x - 1] = dist[y][x] + 1
    que.append((x - 1,y))
  if check(x,y + 1):
    dist[y + 1][x] = dist[y][x] + 1
    que.append((x,y + 1))
  if check(x,y - 1):
    dist[y - 1][x] = dist[y][x] + 1
    que.append((x,y - 1))

print(dist[gy - 1][gx - 1])