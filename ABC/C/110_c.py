from collections import defaultdict
S = input()
T = input()
ans = "Yes"
s_dict = defaultdict(str)
t_dict = defaultdict(str)
# SとTが互いに単射であればYesそうでなければNo
for s,t in zip(S,T):
  if s_dict[t] != "" and s_dict[t] != s:
    ans = "No"
    break
  elif t_dict[s] != "" and t_dict[s] != t:
    ans = "No"
    break
  s_dict[t] = s
  t_dict[s] = t
print(ans)