n = int(input())
a = list(map(int,input().split()))
ans = 0
for key_i, i in enumerate(a):
  if a[i - 1] == key_i + 1:
    ans += 1
print(ans//2)