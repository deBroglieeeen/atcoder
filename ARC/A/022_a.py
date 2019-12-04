import re
s = input().lower()
target = "ict"
match = re.findall(r"\w*(i)\w*(c)\w*(t)\w*",s)
if match == []:
  print("NO")
elif "".join(match[0]) == target:
  print("YES")
else:
  print("NO")