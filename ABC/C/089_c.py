import itertools
n = int(input())
S = [input() for _ in range(n)]
M,A,R,C,H = 0,0,0,0,0
ans = 0
for s in S:
  if s[0] == "M":
    M += 1
  elif s[0] == "A":
    A += 1
  elif s[0] == "R":
    R += 1
  elif s[0] == "C":
    C += 1
  elif s[0] == "H":
    H += 1
U = [M,A,R,C,H]
for x,y,z in itertools.combinations(U,3):
  ans += x * y * z
print(ans)