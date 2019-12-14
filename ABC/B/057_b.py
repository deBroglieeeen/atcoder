n,m = map(int,input().split())
students = [list(map(int,input().split())) for _ in range(n)]
points = [list(map(int,input().split())) for _ in range(m)]
distinations = []
for i in range(n):
  point = -1
  dist = float("INF")
  x1 = students[i][0]
  y1 = students[i][1]
  for j in range(m):
    x2 = points[j][0]
    y2 = points[j][1]
    temp_dist = abs(x1 - x2) + abs(y1 - y2)
    if temp_dist < dist:
      dist = temp_dist
      point = j + 1
  distinations.append(point)
for d in distinations:
  print(d)