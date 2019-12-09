n = int(input())
chair = [list(map(int,input().split())) for _ in range(n)]
ans = 0
for i in range(n):
  left = chair[i][0]
  right = chair[i][1]
  ans += right - left + 1
print(ans)