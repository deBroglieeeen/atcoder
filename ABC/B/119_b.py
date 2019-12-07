n = int(input())
btc = 380000.0
def is_float(s):
  try:
    float(s)
  except:
    return False
  return True
def get_f(a):
  if is_float(a):
    return float(a)
  else:
    return(a)
fortune = [list(map(get_f,input().split())) for _ in range(n)]
jpy = [f[0] for f in fortune if f[1] == "JPY"]
bit = [f[0] for f in fortune if f[1] == "BTC"]
bit = list(map(lambda x:x*btc,bit))
print(sum(jpy)+sum(bit))