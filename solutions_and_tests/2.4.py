from datetime import timedelta, datetime

date_my = input()
days = int(input())
data = datetime.strptime(date_my, "%Y %m %d")
delta = timedelta(days=days)
data += delta
print("{} {} {}".format(data.year, data.month, data.day))