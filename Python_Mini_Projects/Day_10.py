#Habit Streak & Tracker

import datetime
from datetime import timedelta

start=datetime.datetime.now()
date_=input("Enter the last date: ")
par=datetime.datetime.strptime(date_,"%d-%m-%y")
last=par.date()

today=datetime.date.today()
format=today.strftime("%A, %d %B %y")
print("\nToday: ",format)

Last_study=par.strftime("%A, %d %B %y")
print("Last Studied: ",Last_study)

yesterday = (today-par.date()).days
print("Days: ",yesterday)


end=datetime.datetime.now()

duration = (end - start).total_seconds()
print(f"\n🕒 You took {duration:.1f} seconds to respond.")