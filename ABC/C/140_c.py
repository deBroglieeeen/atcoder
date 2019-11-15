n = int(input())
b = list(map(int,input().split()))
a = []
pre = b[0]
for i in range(n):
  if i == n - 1:
    a.append(b[-1])
    break
  # 同じならそのまま
  if pre == b[i]:
    a.append(pre)
  # 上がったら1個前のを
  elif pre < b[i]:
    a.append(pre)
    pre = b[i]
  # 下がったらその都度下げる
  elif pre > b[i]:
    a.append(b[i])
    pre = b[i]
print(str(sum(a)))