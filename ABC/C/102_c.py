import statistics
n = int(input())
A = list(map(int,input().split()))
al = []
for i in range(n):
  al.append(A[i] - i + 1)
b = statistics.median(al)
ans = 0
for a in al:
  ans += abs(a - b)
print(int(ans))