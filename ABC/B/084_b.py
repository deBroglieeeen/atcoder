a,b = map(int,input().split())
s = list(input())
ans = "No"
if not "-" in s[0:a] and s[a] == "-" and not "-"  in s[a+1:]:
  ans = "Yes"
print(ans)