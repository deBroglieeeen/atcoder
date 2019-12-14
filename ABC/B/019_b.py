S = input()
pre = S[0]
ans = ""
cnt = 1
for i in range(1,len(S)):
  if pre == S[i]:
    cnt += 1
  else:
    ans = ans + pre + str(cnt)
    pre = S[i]
    cnt = 1
  if i == len(S) - 1:
    ans = ans + S[i] + str(cnt)
print(ans)