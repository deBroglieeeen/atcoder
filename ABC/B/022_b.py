n = int(input())
A = [ int(input()) for _ in range(n) ]
pollen = set()
ans = 0
for i in range(n):
  if A[i] in pollen:
    ans += 1
  pollen.add(A[i])
print(ans)