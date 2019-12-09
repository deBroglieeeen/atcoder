import heapq
n = int(input())
A = list(map(lambda x: int(x)*(-1),input().split()))
heapq.heapify(A)
# even if you heapfied your list the type is still list
#print(type(A))
al = []
bo = []
for i in range(n):
  if i % 2 == 0:
    al.append(heapq.heappop(A)*(-1))
  else:
    bo.append(heapq.heappop(A)*(-1))
print(sum(al)-sum(bo))