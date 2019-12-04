n = int(input())
a = list(map(int,input().split()))
# ペアの数だけsetで消されるからn-len(s)で差を取るとペアの数がとってこれる
# sortedとset({}で表される)がキーになっている
s = {tuple(sorted([a[i],i+1]))for i in range(n)}
print(n-len(s))