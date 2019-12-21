N,A,B,C = map(int,input().split())
L = [int(input()) for _ in range(N)]
INF = 10 ** 9
def dfs(depth,a,b,c):
  if depth == N:
    return abs(a - A) + abs(b - B) + abs(c - C) if min(a,b,c) > 0 else INF
  ret0 = dfs(depth+1,a,b,c)
  # 最初の一本目は合体コストがないことに注意する
  ret1 = dfs(depth+1,a+L[depth],b,c) + 10 if a else dfs(depth+1,a+L[depth],b,c)
  ret2 = dfs(depth+1,a,b+L[depth],c) + 10 if b else dfs(depth+1,a,b+L[depth],c)
  ret3 = dfs(depth+1,a,b,c+L[depth]) + 10 if c else dfs(depth+1,a,b,c+L[depth])
  return min(ret0,ret1,ret2,ret3)
print(dfs(0,0,0,0))