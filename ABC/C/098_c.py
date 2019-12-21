n = int(input())
s = input()
e_counts = [0] * (n + 1)
w_counts = [0] * (n + 1)
e_counts[0] = 0
w_counts[0] = 0
ans = float("inf")
for i in range(n):
  if s[i] == "E":
    e_counts[i + 1] = e_counts[i] + 1
    w_counts[i + 1] = w_counts[i]
  else:
    e_counts[i + 1] = e_counts[i]
    w_counts[i + 1] = w_counts[i] + 1
for i in range(n):
  ans = min(ans,e_counts[n] - e_counts[i + 1] + w_counts[i])
print(ans)