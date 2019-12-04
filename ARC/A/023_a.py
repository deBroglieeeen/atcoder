import datetime
y = int(input())
m = int(input())
d = int(input())
dt1 = datetime.datetime(year=2014,month=5,day=17)
dt2 = datetime.datetime(year=y,month=m,day=d)
td = dt1 - dt2
print(td.days)