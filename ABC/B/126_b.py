s = input()
sl = int(s[0:2])
sr = int(s[2:4])
if 1<= sl <= 12:
  if 1 <= sr <= 12:
    print("AMBIGUOUS")
  else:
    print("MMYY")
else:
  if 1 <= sr <= 12:
    print("YYMM")
  else:
    print("NA")