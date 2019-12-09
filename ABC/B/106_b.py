n = int(input())
n_cnt = 0
for i in range(1,n + 1,2):
  cnt = 0
  for j in range(1,n + 1):
    if i % j == 0:
      cnt += 1
    if j == n and cnt == 8:
      n_cnt += 1
print(n_cnt)