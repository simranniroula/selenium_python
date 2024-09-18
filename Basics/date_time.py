import datetime

current_date = datetime.datetime.today().date()
current_time = datetime.datetime.today().time()
print(current_date)
print(current_time)

current_datetime = datetime.datetime.today()
print(current_datetime)

filename = current_datetime.strftime('%Y-%m-%d-%H-%M-%S-%f')
print(filename)

