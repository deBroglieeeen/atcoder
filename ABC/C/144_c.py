import sys
from collections import deque
import math


# ans = 0
n = int(input())
#h = math.ceil(n/2)
dists = []
h = math.ceil(math.sqrt(n))
# i <= jとする
for i in range(1,h + 1):
    if n % i != 0:
      continue
    j = int(n / i)
    dists.append(i + j - 2)
print(min(dists))


# h = math.ceil(n/2)
# board1 = [[0]*h/2 for _ in range(h/2)]
# board2 = [[0]*h/2 for _ in range(h/2)]
# for i in range(1,h/2 + 1):
#   for j in range(1,h/2 + 1):
#     board1[i - 1][j - 1] = i * j
# for i in range(h/2 + 1,h + 1):
#   for j in range(h/2 + 1,h + 1):
#     board2[i - (h/2 + 1)][j - (h/2 + 1)] = i * j
# sx = 1
# sy = 1
# gx = 0
# gy = 0
# dist1 = [[-1]*h/2 for _ in range(h/2)]
# dist2 = [[-1]*h/2 for _ in range(h/2)]
# que = deque([(sy - 1,sx - 1)])
# dist1[sy - 1][sx - 1] = 0
# while que:
#   y,x = que.popleft()
#   if board1[y][x] == n:
#     ans = dist1[y][x]
#     break
#   for y1,x1 in [(y + 1,x),(y, x + 1)]:
#     if y1 < 0 or x1 < 0 or x1 >= h/2:
#       continue
#     if y1 >= h/2:
#       sy = y1
#       sx = x1
#       gy = y
#       gx = x
#       break
#     if dist1[y1][x1] != -1:
#       continue
#     if dist1[y1][x1] == -1:
#       dist1[y1][x1] = dist1[y][x] + 1
#       que.append((y1,x1))
# que = deque([sy,sx])
# dist2[sy][sx] = 0
# while que:
#   y,x = que.popleft()
#   if board2[y][x] == n:
#     ans = dist1[gy][gx] + dist2[y][x]
#     break
#   for y1,x1 in [(y + 1,x),(y, x + 1)]:
#     if y1 < 0 or x1 < 0 or x1 >= h/2:
#       continue
#     if y1 >= h/2:
#       sy = y1
#       sx = x1
#       break
#     if dist2[y1][x1] != -1:
#       continue
#     if dist2[y1][x1] == -1:
#       dist2[y1][x1] = dist2[y][x] + 1
#       que.append((y1,x1))
# print(ans)