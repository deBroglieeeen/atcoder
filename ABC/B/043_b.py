from collections import deque
s = deque(list(input()))
editor = deque()
while s:
  x = s.popleft()
  if x == "0":
    editor.append("0")
  elif x == "1":
    editor.append("1")
  elif x == "B" and len(editor) != 0:
    editor.pop()
print("".join(editor))