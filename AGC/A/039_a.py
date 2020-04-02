S = input()
K = int(input())
cnt = 0
pre = S[0]
for i in range(1,len(S)):
  if pre == S[i]:
    cnt += 1
  else:
    pre = S[i]

if S[0] == S[-1]:
  cnt += K - 1
