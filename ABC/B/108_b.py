x1,y1,x2,y2 = map(int,input().split())
a = x2 - x1
b = y2 - y1
x3,y3 = x2 - b,y2 + a
x4,y4 = x3 - a,y3 - b
print(str(x3) + " " + str(y3) + " " + str(x4) + " " + str(y4))