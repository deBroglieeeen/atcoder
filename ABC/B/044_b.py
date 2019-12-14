import collections
w = list(input())
cnt_w = collections.Counter(w)
ans = "Yes"
for v in cnt_w.values():
  if v % 2 != 0:
    ans = "No"
print(ans)