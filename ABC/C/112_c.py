import sys
N = int(input())
pyramids = [tuple(map(int,input().split())) for _ in range(N)]
for i in range(101):
  for j in range(101):
    H_set = set()
    keep = []
    for k in range(len(pyramids)):
      x,y,h = pyramids[k]
      if h == 0:
        keep.append((x,y))
        continue
      H_set.add(h + abs(x - j) + abs(y - i))
    if len(H_set) == 1:
      if len(keep) != 0:
        is_suitable = True
        for x,y in keep:
          if list(H_set)[0] - abs(j - x) - abs(i - y) > 0:
            is_suitable = False
            break
        if is_suitable:
          print(j,i,list(H_set)[0])
          sys.exit()
        else:
          continue
      else:
        print(j,i,list(H_set)[0])
        sys.exit()