import datetime
D = datetime.date(*list(map(int,input().split("/"))))

while True:
  if D.year / D.month % D.day == 0:
    print(D.strftime("%Y/%m/%d"))
    break
  D += datetime.timedelta(days=1)