a,b = map(int,input().split())
dif = b - a
west = (dif - 1) * dif // 2
east = dif * (dif + 1) // 2
print(west - a)