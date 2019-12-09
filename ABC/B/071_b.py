s = sorted(set(input()))
t = "abcdefghijklmnopqrstuvwxyz"
ans = "None"
for tt in t:
  if not tt in s:
    ans = tt
    break
print(ans)