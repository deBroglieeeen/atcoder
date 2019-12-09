h,w = map(int,input().split())
A = [input() for _ in range(h)]
for i in range(h):
  #print(A[i])
  A[i] =  "#" + A[i] +"#"
  #print(A[i])
for i in range(h + 2):
  if i == 0:
    print("#"*(w + 2))
  elif i == h + 1:
    print("#"*(w + 2))
  else:
    print(A[i - 1])