import math
n = int(input())
R = [int(input()) for _ in range(n)]
R = sorted(R,reverse = True)
ans = 0
for i in range(n):
  if i % 2 == 0:
    ans += R[i] ** 2
  else:
    ans  -= R[i] ** 2
ans *= math.pi
print(ans)