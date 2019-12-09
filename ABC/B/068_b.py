n = int(input())
ans = 1
bcnt = 0
for i in range(1,n + 1):
  cnt = 0
  #print(i)
  a = i
  while a % 2 == 0:
    cnt += 1
    a = a // 2
  if cnt > bcnt:
    ans = i
    bcnt = cnt
    #print(i)
print(ans)