S = input()
T = input()
lose = "You will lose"
ans = "You can win"
wild = ["a","t","c","o","d","e","r"]
for s,t in zip(S,T):
  if s != t:
    if s != "@" and t != "@":
      ans = lose
    elif s == "@" and not t in wild:
      ans = lose
    elif t == "@" and not s in wild:
      ans = lose
print(ans)