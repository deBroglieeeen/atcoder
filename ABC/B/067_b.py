n,k = map(int,input().split())
L = sorted(list(map(int,input().split())))
nl = []
for i in range(k):
  nl.append(L[-i - 1])
print(sum(nl))