n = int(input())
A = [int(input()) for _ in range(n)]
A = sorted(set(A))
print(A[-2])