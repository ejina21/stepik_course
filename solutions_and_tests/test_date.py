import datetime
timezone_offset = -8  # Pacific Standard Time (UTC−08:00)
tzinfo = datetime.timezone(datetime.timedelta(hours=timezone_offset))
print(datetime.datetime.now(tzinfo))