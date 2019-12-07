n = int(input())
ans = []
ans.append(1)
cnt = 1
for i in range(5):
  if sum(ans) == n:
    break
  else:
    ans.append(2)
    cnt += 1
print(cnt)
for a in ans:
  print(a)