s = list(input())
ans = 0
for i in range(1,len(s)):
  if i % 2 != 0:
    s.pop()
    continue
  else:
    s.pop()
    s1 = s[0:(len(s)//2)]
    s2 = s[(len(s)// 2) :]
    if s1 == s2:
      ans = len(s)
      break
print(ans)