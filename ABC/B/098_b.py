n = int(input())
s = input()
ans = 0
for i in range(n - 1):
  cnt = 0
  X = s[0:i + 1]
  Y = s[i + 1:]
  X = set(X)
  Y = set(Y)
  for x in X:
    if x in Y:
      cnt += 1
  ans = max(ans,cnt)
print(ans)