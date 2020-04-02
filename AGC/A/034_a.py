N,A,B,C,D = map(int,input().split())
S = list(input())
ans = "Yes"
is_reversed = False
flag = False
if D < C:
  is_reversed = True
for i in range(A,max(C,D) -1):
  if S[i] == S[i + 1] == "#":
    ans = "No"
if is_reversed == True:
  for i in range(B - 2,D - 1):
    if S[i] == S[i + 1] == S[i + 2] == ".":
      flag = True
  if flag == False:
    ans = "No"
print(ans)