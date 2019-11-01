import numpy as np
n,k = map(int,input().split())
field = np.array(input().split(),np.int64)
dp = np.zeros(n,np.int64)
# numpyのブロードキャストとスライスを組み合わせることで1重のfor文で済ますという変態的なことをしてる
# ただ計算量がO(N)になっているかは謎
for i in range(1,n):
  left = max(0,i - k)
  dp[i] = (dp[left:i] + abs(field[left:i] - field[i])).min()
print(dp[-1])