n = int(input())
P = [int(input()) for _ in range(n)]
p_m = max(P)
print(sum(P) - p_m + p_m//2)