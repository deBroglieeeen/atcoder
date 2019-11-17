import numpy as np
import math
import itertools
values = []
n = int(input())
towns = [list(map(int,input().split())) for _ in range(n)]
num_root = math.factorial(n)
for root in itertools.permutations(towns):
  for i in range(n - 1):
    level = (root[i][0] - root[i + 1][0])**2 + (root[i][1] - root[i + 1][1])**2
    values.append(math.sqrt(level))
print(sum(values)/num_root)