n = int(input())
S = input()
ans = 0
x = 0
for s in S:
  if s == "I":
    x += 1
    ans = max(ans,x)
  elif s == "D":
    x -= 1
print(ans)