a,b,c = sorted(map(int,input().split()))
k = int(input())
for i in range(k):
  c *= 2
print(a + b + c)