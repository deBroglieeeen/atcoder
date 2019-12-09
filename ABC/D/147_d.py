n = int(input())
A = list(map(int,input().split()))
mod = 10**9 + 7
ans = 0
# for i in range(n - 1):
#   for j in range(i + 1,n):
#     ans += A[i] ^ A[j]
for i in range(n):
  ans += sum(A) ^ A[0]
print(ans)
print(ans%mod)
print(2^3)