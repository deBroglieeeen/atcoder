import itertools
anthena = [int(input())for _ in range(5)]
k = int(input())
ans = "Yay!"
for i,j in itertools.combinations(anthena,2):
  if abs(i - j) > k:
    ans = ":("
print(ans)