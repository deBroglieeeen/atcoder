n = int(input())
#map(int,input().split())
s = list(input())
alpha = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
for i in range(len(s)):
  index = alpha.index(s[i])
  index += n
  if index > 25:
    index -= 26
    s[i] = alpha[index]
  else:
    s[i] = alpha[index]
print("".join(s))