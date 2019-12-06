s = input()
k = int(input())
if s[0] != "1":
  print(s[0])
else:
  # print(list(set(s[0:k]))[0])
  # print(set(s[0:k]))
  # print(len(s[0:k]))
  if list(set(s[0:k]))[0] == "1" and len(set(s[0:k])) == 1:
    print(1)
  else:
    for s_s in s:
      if s_s != "1":
        print(s_s)
        break
