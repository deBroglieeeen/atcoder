n = int(input())
p = list(map(int,input().split()))
ans = 0
for i in range(1,n - 1):
  target = p[i]
  sort_list = [p[i - 1],p[i],p[i + 1]]
  sort_list = sorted(sort_list)
  if sort_list[-2] == target:
    ans += 1
print(ans)