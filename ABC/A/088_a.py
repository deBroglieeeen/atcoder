n = int(input())
a = int(input())
ans = "No"
if n <= a:
  ans = "Yes"
elif n % 500 <= a:
  ans = "Yes"
print(ans)