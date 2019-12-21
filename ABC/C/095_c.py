A,B,C,X,Y = map(int,input().split())
if C * 2 > A + B:
  print(A * X + B * Y)
elif C * 2 <= A and C * 2 <= B:
  print(C * 2 * max(X,Y) )
# elif C * 2 <= A + B and C * 2 > B:
#   if X >= Y:
#     print(C * 2 * X)
#   else:
#     print(C * 2 * X + B * (Y - X))
# elif C * 2 > A + B and C * 2 <= B:
#   if Y >= X:
#     print(C *2 * Y)
#   else:
#     print(C * 2 * Y + A * (X - Y))

elif C * 2 <= A + B:
  if X >= Y:
    print(C * 2 * Y + A * (X - Y))
  else:
    print(C * 2 * X + B * (Y - X))