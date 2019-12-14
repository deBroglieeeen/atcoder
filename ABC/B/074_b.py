n = int(input())
k = int(input())
X = list(map(int,input().split()))
dist = []
for x in X:
  dist.append(min(abs(k - x) * 2,abs(0 - x) * 2))
print(sum(dist))