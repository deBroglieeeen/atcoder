l,h = map(int,input().split())
n = int(input())
A = [int(input()) for _ in range(n)]
for i in range(n):
  if l <= A[i] <= h:
    print(0)
  elif A[i] < l:
    print(l - A[i])
  elif h < A[i]:
    print(-1)