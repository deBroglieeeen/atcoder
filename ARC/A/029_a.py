n = int(input())
t = [int(input()) for i in range(n)]
ans = float('inf')
devicesum = sum(t)
for i in range(2**n):
  devicea = []
  asum = 0
  deviceb = 0
  group = ["a"]*n
  for j in range(n):
    if i >> j & 1:
      group[j] = "b"
  for k in range(n):
    if group[k] == "a":
      devicea.append(t[k])
  asum = sum(devicea)
  if asum <= devicesum / 2 and devicesum - asum < ans:
    ans = devicesum - asum
  elif asum > devicesum / 2 and asum < ans:
    ans = asum
print(ans)