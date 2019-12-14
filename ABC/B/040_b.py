n = int(input())
ans = float("INF")
for i in range(1,int(n ** 0.5) + 1):
    ans = min(ans,abs(n - n//i * i + abs(n // i - i)))
print(ans)