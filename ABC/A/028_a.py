n = int(input())
if n <= 59:
  print("Bad")
elif 60 <= n <= 89:
  print("Good")
elif 90 <= n <= 99:
  print("Great")
elif n == 100:
  print("Perfect")