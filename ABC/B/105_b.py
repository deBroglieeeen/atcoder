n = int(input())
# if n % 4 == 0 or n % 7 == 0:
#   print("Yes")
# elif n % (4 + 7) == 0:
#   print("Yes")
# elif n % 4 % 7 == 0 or n % 7 % 4 == 0:
#   print("Yes")
# else:
#   print("No")
ans = "No"
for i in range(0,n//4 + 1):
  for j in range(0,n//7 + 1):
    if 4 * i + 7 * j == n:
      ans = "Yes"
print(ans)