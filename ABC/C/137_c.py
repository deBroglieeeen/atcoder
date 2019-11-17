import collections
n = int(input())
s = ["".join(sorted(input())) for _ in range(n)]
#values = []
combs = 0
c = collections.Counter(s)
# このfor文を削減するためにcollections.Counter()を使用
# for i in set(s):
#   if s.count(i) > 1:
#     values.append(s.count(i))
for i in c.values():
  combs+=i*(i-1)//2
print(combs)