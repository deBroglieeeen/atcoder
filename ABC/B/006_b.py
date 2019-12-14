from collections import deque
n = int(input())
mod = 10007
tori_list = deque()
# def toribonatti(a):
#   if a == 1 or a == 2:
#     return 0
#   elif a == 3:
#     return 1
#   return toribonatti(a - 3) % mod + toribonatti(a - 2) % mod + toribonatti(a - 1) % mod
for i in range(n):
  if i == 0 or i == 1:
    tori_list.append(0)
  elif i == 2:
    tori_list.append(1)
  else:
    tori_list.append((tori_list[0]+tori_list[1]+tori_list[2])%mod)
    tori_list.popleft()
# print(toribonatti(n))
# print(toribonatti(n) % mod)
print(tori_list[-1])