n = int(input())
l = [None] * 87
l[0] = 2
l[1] = 1
for i in range(2,n + 1):
  l[i] = l[i - 2] + l[i - 1]
print(l[n])