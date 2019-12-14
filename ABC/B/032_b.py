s = input()
k = int(input())
candidates = set()
for i in range(len(s) - k + 1):
  candidates.add(s[i:i + k])
print(len(candidates))