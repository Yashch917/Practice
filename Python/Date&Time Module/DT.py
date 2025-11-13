import datetime,pytz
now = datetime.datetime.now()
print("Current date and time: ", now)

today = datetime.date.today()
print("Today's date: ", today)

d=datetime.date(2005,1,8)
print("My birthdate :",d)

print("year: ",today.year)
print("month: ",today.month)
print("day: ",today.day)

print(now.strftime("%Y-%m-%d"))
print(now.strftime("%d/%m/%Y"))
print(now.strftime("%A"))

now=datetime.datetime.now(pytz.timezone("Asia/Kolkata"))
now1=datetime.datetime.now(pytz.timezone("Asia/Hong_Kong"))
print("Time in India:",now)
print("Time in Hong Kong:",now1)