n = int(input())
member = sorted(list(map(int,input().split())))
rest = member[n:]
represent = []
for i in range(0,2 * n,2):
  represent.append(rest[i])
print(sum(represent))