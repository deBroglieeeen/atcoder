import math
import i
a,b,c = map(int,input().split())
formula = ""

print(max(eval(f"{a}{b}+{c}"),eval(f"{a}+{b}{c}")))
