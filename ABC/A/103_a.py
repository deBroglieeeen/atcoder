A =  sorted(list(map(int,input().split())),reverse=True)
ans = 0
for i in range(len(A) - 1):
  ans += abs(A[i] - A[i + 1])
print(ans)