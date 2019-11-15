import numpy as np
n = int(input())
a = list(map(int,input().split()))
line = np.ndarray((n,2),np.int64)
for i in range(n):
  line[i][0] = i + 1
  line[i][1] = a[i]

s = sorted(line,key=lambda x:x[1])
for i in range(n):
  print(s[i][0])