import datetime
t = int(input())
h = t // 3600
if t > 3599:
  m = t % 3600 // 60
else:
  m = t // 60
s = t - h * 3600 - m * 60
ad = datetime.time(hour=h,minute=m,second=s)
print(ad)