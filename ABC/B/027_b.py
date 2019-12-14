n = int(input())
A = list(map(int,input().split()))
ans = 0
if sum(A) % n != 0:
  print(-1)
else:
  mean = sum(A) // n
  for i in range(len(A)):
    left = sum(A[:i + 1])
    need = mean * (i + 1)
    if left != need:
      ans += 1
  print(ans)