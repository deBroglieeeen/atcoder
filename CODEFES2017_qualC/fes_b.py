n = int(input())
a = list(map(int,input().split()))
count = 0
for i in a:
  if i % 2 == 0:
    count += 1
print(3**n-2**count)