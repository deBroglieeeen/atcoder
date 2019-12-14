import math
n = int(input())
A = list(map(int,input().split()))
no_bug = A.count(0)
print(math.ceil(sum(A) / (n - no_bug)))