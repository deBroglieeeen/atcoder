s = list(input())
imagine = 0
for i in s:
  if i == "+":
    imagine += 1
  else:
    imagine -= 1
print(imagine)