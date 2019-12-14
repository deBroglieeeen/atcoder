n = int(input())
def to_i(x):
  if x.isnumeric():
    return int(x)
  return x
towns = [list(map(to_i,input().split())) for _ in range(n)]
population = [t[1] for t in towns]
if max(population) > sum(population) / 2:
  index = population.index(max(population))
  print(towns[index][0])
else:
  print("atcoder")