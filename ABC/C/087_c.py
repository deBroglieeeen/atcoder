n = int(input())
A = [list(map(int,input().split())) for _ in range(2)]
ans = []
l = 0
for i in range(n):
  l += sum(A[0][0:i + 1])
  l += sum(A[1][i:])
  ans.append(l)
  l = 0
print(max(ans))