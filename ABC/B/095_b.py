n,x = map(int,input().split())
M = [int(input()) for _ in range(n)]
rest = x - sum(M)
cnt = rest // min(M)
print(n + cnt)