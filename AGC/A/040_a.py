S = list(input())
l = [0]*(len(S) + 1)
for i in range(len(S)):
  if S[i] == "<":
    l[i + 1] = l[i] + 1
for i in range(len(S)):
  if S[-i - 1] == ">" and l[-i - 2] <= l[-i -1]:
    l[-i -2] = l[-i - 1] + 1
print(sum(l))