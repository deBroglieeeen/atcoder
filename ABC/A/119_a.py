from datetime import datetime as dt
heisei = dt.strptime("2019/04/30",'%Y/%m/%d')
s = input()
sdate = dt.strptime(s,'%Y/%m/%d')
if sdate <= heisei:
  print("Heisei")
else:
  print("TBD")