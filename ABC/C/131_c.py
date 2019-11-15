# 方針はb以下の条件にあったものからa - 1以下の条件にあったものを引く
# 最小公倍数を使って引きすぎたものを置換

# greatest common divisor
# gcd はユークリッドの互除法をつかって再帰の形で求められる
def gcd(x,y):
  if y == 0: return x
  return gcd(y,x%y)

# least common multiple
# // を使った除算で小数点を省ける
def lcm(e,f):
  return e * f // gcd(e,f)
a,b,c,d = map(int,input().split())

all = b - (b // c) - (b // d) + (b // lcm(c,d))
to_a = (a - 1) - ((a - 1) // c) - ((a - 1) // d) + ((a - 1) // lcm(c,d))
print(str(all - to_a))
