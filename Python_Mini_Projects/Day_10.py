#Habit Streak & Tracker

import datetime
from datetime import timedelta

start=datetime.datetime.now()

date_=input("When did you last study Python? (DD-MM-YY): ")
par=datetime.datetime.strptime(date_,"%d-%m-%y")
last=par.date()

today=datetime.date.today()
format=today.strftime("%A, %d %B %y")
print("\n📅 Today: ",format)

Last_study=par.strftime("%A, %d %B %y")
print("🧠 Last Studied: ",Last_study)

days_gap = (today-par.date()).days
print("Days: ",days_gap)

if days_gap==0:
    print("\n✅ You're on a track")

elif days_gap==1:
    print("\n🔥 Your Streak Is Alive")

else:
    print(f"\n⏳ It has been {days_gap} day(s) since your last study session.")
    print("⛔ Streak broken!")

end=datetime.datetime.now()

duration = (end - start).total_seconds()
print(f"\n🕒 You took {duration:.1f} seconds to respond.")