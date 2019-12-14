n = int(input())
s = input()
y = "b"
for i in range(n):
  if s == "b":
    print(0)
    break
  if s[i] != "a" and s[i] != "b" and s[i] != "c":
    print(-1)
    break
  if (i + 1) % 3 == 1:
    new = list("ac")
    new[1:-1] = y
    y = "".join(new)
  elif (i + 1) % 3 == 2:
    new = list("ca")
    new[1:-1] = y
    y = "".join(new)
  else:
    new = list("bb")
    new[1:-1] = y
    y = "".join(new)
  if s == y:
    print(i + 1)
    break
  if i == n - 1:
    print(-1)