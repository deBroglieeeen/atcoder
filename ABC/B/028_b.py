S = input()
al = [[] for _ in range(6)]
for s in S:
  if s == "A":
    al[0].append("A")
  elif s == "B":
    al[1].append("B")
  elif s == "C":
    al[2].append("C")
  elif s == "D":
    al[3].append("D")
  elif s == "E":
    al[4].append("E")
  elif s == "F":
    al[5].append("F")
for i in range(len(al)):
  if i == len(al) - 1:
    print(str(len(al[i])))
  else:
    print(str(len(al[i])),end=" ")