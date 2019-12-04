candy = list(map(int,input().split()))
if max(candy) == sum(candy) - max(candy):
  print("Yes")
else:
  print("No")