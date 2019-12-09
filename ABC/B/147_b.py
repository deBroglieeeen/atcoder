S = list(input())
left = S[0:len(S)//2]
right = S[len(S)//2:]
right.reverse()
cnt = 0
for l,r in zip(left,right):
  if l != r:
    cnt += 1
print(cnt)