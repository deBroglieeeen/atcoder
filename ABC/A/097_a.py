a,b,c,d = map(int,input().split())
ans = "No"
if abs(b - a) <= d and abs(c - b) <= d:
  ans = "Yes"
elif abs(c - a) <= d:
  ans = "Yes"
print(ans)