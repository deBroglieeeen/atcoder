#import re
n = int(input())
s = input()
ans = 1

for i in range(1,len(s)):
  if s[i] != s[i-1]:
    ans += 1

print(ans)

# またはa-zまで正規表現をかます
# for i in range(26):
#   ans = re.sub("([a-z])\\1","\\1",ans)
# print(len(ans))
