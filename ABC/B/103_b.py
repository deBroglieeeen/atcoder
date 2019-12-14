s = input()
t = input()
ans = "No"
for i in range(len(s)):
  a = s[:-1]
  z = s[-1]
  s = z + a
  if s == t:
    ans = "Yes"
print(ans)