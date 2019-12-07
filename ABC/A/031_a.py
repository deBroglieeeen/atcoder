a,d = map(int,input().split())
attack = (a + 1) * d
deffence = (d + 1) * a
if attack > deffence:
  print(attack)
else:
  print(deffence)