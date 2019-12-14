# findとrfindの使い方
s = input()
a = 0
z = 0
while True:
  a = s.find("A")
  z = s.rfind("Z")
  if s[a:z+1][0] == "A" and s[a:z+1][-1] == "Z":
    break
print(z - a + 1)