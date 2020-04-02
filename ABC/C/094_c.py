n = int(input())
X = list(map(int,input().split()))
X_sorted = sorted(X)
L = X_sorted[n // 2 - 1]
R = X_sorted[n // 2]
for x in X:
  print(L if x >= R else R)