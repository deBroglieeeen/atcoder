n = int(input())
L = list(map(int,input().split()))
m_l = max(L)
if m_l < sum(L) - m_l:
  print("Yes")
else:
  print("No")