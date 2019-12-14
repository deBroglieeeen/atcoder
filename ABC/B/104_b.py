s = input()
l = s.find("C")
r = s.rfind("C")
a = s[1:]
a = a.replace("C","")
if s[0] != "A" or s[-1] == "C" or l != r or 2 > l or not a.islower():
  print("WA")
else:
  print("AC")