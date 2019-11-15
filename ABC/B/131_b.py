n,l = map(int,input().split())
apple = []
for i in range(1,n + 1):
  apple.append(l + i -1)
abs_apple = [abs(a) for a in apple]
index = abs_apple.index(min(abs_apple))
apple.pop(index)
print(sum(apple))