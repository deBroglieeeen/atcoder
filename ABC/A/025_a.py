s = input()
n = int(input())
cnt = 0
for i in range(len(s)):
  for j in range(len(s)):
    cnt += 1
    if cnt == n:
      print(s[i]+s[j])