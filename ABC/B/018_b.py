S = input()
n = int(input())
operates = [ map(int,input().split()) for _ in range(n) ]
for i in range(n):
  l,r = operates[i]
  rev = S[l - 1:r]
  rev = rev[::-1]
  S = S[0:l - 1] + rev + S[r:]
print(S)