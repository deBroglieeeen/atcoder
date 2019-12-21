n,q = map(int,input().split())
s = input()
questions = [tuple(map(int,input().split())) for _ in range(q)]
A_Flag = False
t = [0]*(n + 1)
for i in range(0,n):
  if s[i:i+2] == "AC":
    t[i + 1] = t[i] + 1
  else:
    t[i + 1] = t[i]
for i in range(q):
  l,r = questions[i]
  print(t[r - 1] - t[l - 1])