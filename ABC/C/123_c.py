import math
n = int(input())
transportation = [int(input()) for _ in range(5)]
print(math.ceil(n/min(transportation)) - 1 + 5 )