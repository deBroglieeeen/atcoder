n = int(input())
A = list(map(int,input().split()))
A_l = [0,0]
A_l[1:1] = A
D = 0
for i in range(len(A_l) - 1):
  D += abs(A_l[i] - A_l[i + 1])
for i in range(n):
  print(D - abs(A_l[i] - A_l[i + 1])- abs(A_l[i + 1] - A_l[i + 2]) + abs(A_l[i] - A_l[i + 2]))