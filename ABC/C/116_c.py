n = int(input())
H = list(map(int,input().split()))
ans = 0
while H.count(0) != len(H):
  l,r = -1,-1
  for i in range(len(H)):
    if l == -1 and H[i] != 0:
      l = i
      r = l
    elif H[i] != 0:
      r = i
    elif l != -1 and H[i] == 0:
      break
  selected = [ h - 1 for h in H[l:r+1]]
  H[l:r+1] = selected
  ans += 1
print(ans)