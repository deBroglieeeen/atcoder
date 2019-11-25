s = list(input())
gene = ["A","T","G","C"]
ans = 0
length = 0
for i in range(len(s)):
  if s[i] in gene:
    length += 1
    ans = max(ans,length)
  else:
    length = 0
print(ans)