n = int(input())
t,a = map(int,input().split())
H = list(map(int,input().split()))
def get_temp(x):
  return t - x * 0.006
best = a + 10000
ans = 0
for i in range(n):
  cur_dif = abs(get_temp(H[i]) - a)
  if cur_dif < best:
    best = cur_dif
    ans = i + 1
print(ans)