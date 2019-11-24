n,k = map(int,input().split())
s = list(input())
for i in range(k):
  s[k-1] = s[k-1].lower()
print("".join(s))