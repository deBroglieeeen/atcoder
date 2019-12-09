n = int(input())
A = sorted(set(list(map(int,input().split()))))
ans = 0
for i in range(len(A)-1):
  ans += abs(A[i] - A[i + 1])
print(ans)