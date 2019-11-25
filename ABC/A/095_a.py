s = list(input())
topping = 0
for i in s:
  if i == "o":
    topping += 1
print(700 + (100 * topping))