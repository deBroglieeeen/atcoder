S = input()
K = int(input())
s = set()
for L in range(1,K + 1):
  for j in range(len(S)):
    s.add(S[j:L + j])
ss = sorted(list(s))
print(ss[K - 1])