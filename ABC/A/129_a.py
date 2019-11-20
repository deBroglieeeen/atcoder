import itertools
#p,q,r = map(int,input().split())
times = map(int,input().split())
ans = 900
for time in itertools.combinations(times,2):
  ans = min(ans,time[0] + time[1])
print(ans)