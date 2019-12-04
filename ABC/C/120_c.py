s = input()
n = len(s)
red_cnt = 0
for i in s:
  if i == "0":
    red_cnt += 1
print(min(red_cnt,n-red_cnt)*2)