n = int(input())
d = list(map(int,input().split()))
k = 0
half = n / 2
half = int(half)
d = sorted(d)
print(d[half] - d[half - 1])