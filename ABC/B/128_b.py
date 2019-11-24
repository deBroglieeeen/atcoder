n = int(input())
def int_or_st(i):
  if str.isnumeric(i):
    return int(i)
  else:
    return i
res = [list(map(int_or_st,input().split())) for _ in range(n)]
sorted_res = sorted(res,reverse=True,key=lambda x:x[1])
sorted_res.sort(key=lambda x:x[0])
for i in sorted_res:
  print(res.index(i)+1)