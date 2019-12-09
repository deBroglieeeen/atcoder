O = input()
E = input()
al = ""
for o,e in zip(O,E):
  al += o
  al += e
if len(O) > len(E):
  #print(len(O) - len(E))
  for i in range(abs(len(O) - len(E)),0,-1):
    al += O[-i]
elif len(E) > len(O):
  for i in range(abs(len(O) - len(E)),0,-1):
    al += E[-i]
# for i in range(1,len(O) + len(E) + 1):
#   if i % 2 == 1:
#     al += O[i]
#   else:
#     al += E[i]
print(al)