n = int(input())
h = list(map(int,input().split()))
pre = h[-1]
ans = "Yes"
flag = False
count = 0
# 右のマスから調べていく
for i in range(-2,-n,-1):
  # if flag and pre - h[i] > 0:
  #   count += 1
  # if pre - h[i] > 0 and flag and count > 1:
  #   ans = "No"
  # elif pre - h[i] > 1:
  #   ans = "No"
  # if pre - h[i] < -1:
  #   flag = True
  if h[i] - pre == 1:
    h[i] = h[i] - 1
  elif h[i] - pre > 1:
    ans = "No"
  pre = h[i]
print(ans)