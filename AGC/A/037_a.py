import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# 長さ3以上は使わないとしてよい

S = "$$" + read().rstrip().decode("utf-8")

# 最後の長さ　-> 文字列の個数
N = len(S)
INF = 10 ** 9
one = [-INF] * N; one[1] = 0
two = [-INF] * N; two[1] = 0
for i in range(2,N):
  x = two[i - 1] + 1

  if S[i] != S[i - 1]:
    y = one[i - 1] + 1
    if x < y:
      x = y
  one[i] = x
  x = one[i - 2] + 1
  if S[i - 1:i + 1] != S[i - 3:i - 1]:
    y = two[i - 2] + 1
    if x < y:
      x = y
  two[i] = x
answer = max(one[-1],two[-1])
print(answer)