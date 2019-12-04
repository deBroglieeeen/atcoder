s = list(input())
n = len(s) - 1
b_count = s.count("B")
ans = 0
for i in range(len(s)):
  if s[i] == "B":
    ans += n - i
print(ans-((b_count - 1)*(b_count)//2))