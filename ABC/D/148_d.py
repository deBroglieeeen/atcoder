N = int(input())
A = list(map(int,input().split()))
if not 1 in A:
  print(-1)
else:
  rest = 1
  pre = A.index(1)
  for i in range(2,N + 1):
    while i in A:
      index = A.index(i)
      if index > pre:
        rest += 1
        pre = index
      A = A[index + 1:]
  print(N - rest)