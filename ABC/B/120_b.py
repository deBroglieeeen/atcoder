a,b,k = map(int,input().split())
divs = []
for i in range(1,101):
  if a % i == 0 and b % i == 0:
    divs.append(i)
print(divs[-k])