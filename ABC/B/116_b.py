s = int(input())
al = [s]
def modify(n):
  if n % 2 == 0:
    return n // 2
  else:
    return 3 * n + 1
for i in range(2,10 ** 6 + 1):
  a = modify(al[i - 2])
  if a in al:
    print(i)
    break
  else:
    al.append(a)