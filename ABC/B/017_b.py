X = input()
ans = "YES"
for i in range(len(X)):
  if X[i] != "o" and X[i] != "k" and X[i] != "u" and X[i] != "c" and X[i] != "h":
    ans = "NO"
  elif X[i] == "c" and i == len(X) - 1:
    ans = "NO"
  elif X[i] == "h" and i == 0:
    ans = "NO"
  elif X[i] == "c":
    if X[i + 1] != "h":
      ans = "NO"
  elif X[i] == "h":
    if X[i - 1] != "c":
      ans = "NO"
print(ans)