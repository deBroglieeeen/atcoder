x,y = map(int,input().split())
a = [4,6,9,11]
b = [1,3,5,7,8,10,12]
ans = "No"
if x in a and y in a:
  ans = "Yes"
elif x in b and y in b:
  ans = "Yes"
elif x == y == 2:
  ans = "Yes"
print(ans)