x,a,b = map(int,input().split())
if a >= b:
  print("delicious")
elif x >= abs(a-b):
  print("safe")
elif x < abs(a-b):
  print("dangerous")