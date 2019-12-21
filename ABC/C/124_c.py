S = list(input())
pre = S[0]
ans = 0
for i in range(1,len(S)):
  if pre == S[i]:
    if S[i] == "0":
      S[i] =  "1"
    else:
      S[i] = "0"
    ans += 1
  pre = S[i]
print(ans)