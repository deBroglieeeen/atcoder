a,b,c,k = map(int,input().split())
s,t = map(int,input().split())
total = s + t
disc = 0
if total >= k:
  disc = total * c
print(a * s + b * t - disc)