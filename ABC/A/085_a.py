s = list(input())
for i in range(len(s)):
  if i == 3:
    s[i] = "8"
print("".join(s))