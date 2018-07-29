import datetime
year_now = datetime.date.today().year
month_now = datetime.date.today().month
day_now = datetime.date.today().day
d = datetime.date(year_now, month_now, day_now)
day = int(input("Your day of birth: "))
month = int(input("Your month of birth: "))
year = int(input("Your year of birth: "))
date_of_birth = datetime.date(year, month, day)
days = (d - date_of_birth).days
print("Your bday was %i ~ seconds ago" %(days*86400))