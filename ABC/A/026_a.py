a = int(input())
ans = 0
for i in range(100):
  for j in range(100):
    if i + j == a:
      ans = max(ans,i*j)
print(ans)