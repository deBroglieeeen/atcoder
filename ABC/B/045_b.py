from collections import deque
A = deque(list(input()))
B = deque(list(input()))
C = deque(list(input()))
card = "a"
while True:
  if card == "a":
    if len(A) == 0:
      print("A")
      break
    card = A.popleft()
  elif card == "b":
    if len(B) == 0:
      print("B")
      break
    card = B.popleft()
  else:
    if len(C) == 0:
      print("C")
      break
    card = C.popleft()