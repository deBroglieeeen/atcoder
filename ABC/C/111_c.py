from collections import Counter
n = int(input())
V = list(map(int,input().split()))
if len(set(V)) == 1:
  print(n//2)
else:
  odd = []
  even = []
  for i in range(len(V)):
    if i % 2 == 0:
      even.append(V[i])
    else:
      odd.append(V[i])
  max_even,max_e_count = Counter(even).most_common(1)[0]
  max_odd,max_o_count = Counter(odd).most_common(1)[0]
  if max_even == max_odd:
    sec_even,sec_e_count = Counter(even).most_common(2)[1]
    sec_odd,sec_o_count = Counter(odd).most_common(2)[1]
    even_rank2 = len(odd) - max_o_count + len(even) - sec_e_count
    odd_rank2 = len(odd) - sec_o_count + len(even) - max_e_count
    print(min(even_rank2,odd_rank2))
  else:
    print(len(odd) - max_o_count + len(even) - max_e_count)