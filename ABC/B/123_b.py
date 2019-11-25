import math
time = [int(input()) for _ in range(5)]
bad = 9
def swap(i):
  time[i],time[-1] = time[-1],time[i]
for i in time:
  if i % 10 == 0:
    continue
  else:
    if bad % 10 > i % 10:
      bad = i
if bad in time:
  index = time.index(bad)
  swap(index)
for i in range(4):
  if time[i] % 10 != 0:
    time[i] = time[i] + (10 - time[i] % 10)
print(sum(time))