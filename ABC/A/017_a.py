assign = [list(map(int,input().split())) for _ in range(3)]
ans = 0
for i in range(3):
  ans += assign[i][0] * assign[i][1]//10
print(ans)