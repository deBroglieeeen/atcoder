a,b = map(int,input().split())
ans = []
ans.append(a+b)
ans.append(a-b)
ans.append(a*b)

print(max(ans))