import copy
n,k = map(int,input().split())
s = input()
ls = list(s)
min_s = sorted(s)
ans = copy.deepcopy(s)
dif = 0
#t = sorted(ls)
def get_dif(t):
  return sum(x != y for x,y in zip(s,t)) <= k
def swap(i,j,ls):
  s_2 = copy.deepcopy(ls)
  s_2[i],s_2[j] = s_2[j],s_2[i]
  return s_2
for i in range(n):
  b = i
  for j in range(i + 1,n):
    # 現状の文字よりもっと小さい文字がありかつ入れ替えた結果がイカナライレカエル
    if ls[b] > ls[j] and get_dif(swap(i,j,ls)):
      b = j
  ls = swap(i,b,ls)
  # print(min_s)
  # for m in min_s:
  #   index = ans.index(m)
  #   ans[index] = ans[i]
  #   ans[i] = m
  #   for a,b in zip(s,ans):
  #     if a != b:
  #       dif += 1
  #   if dif > k:
  #     ans[i] = ans[index]
  #     ans[index] = m
  #     dif = 0
  #   else:
  #     dif = 0
  #     min_s.remove(m)
  #     break
print("".join(ls))