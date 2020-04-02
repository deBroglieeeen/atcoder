N = int(input())
lack = 2025 - N
for i in range(1,10):
  for j in range(1,10):
    if i * j == lack:
      print(str(i) + " x " + str(j) )