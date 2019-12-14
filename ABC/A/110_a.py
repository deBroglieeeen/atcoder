a,b,c = sorted(input().split(),reverse=True)
print(max(eval(a + "+" + b + c),eval(a + b + "+" + c)))