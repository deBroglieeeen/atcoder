n = int(input())
w = list(map(int,input().split()))
sum_w = sum(w)
ans = float('inf')
s1 = []
for i in range(n):
  s1.append(w[i])
  ans = min(ans,abs(sum(s1)- (sum_w - sum(s1))))
print(ans)