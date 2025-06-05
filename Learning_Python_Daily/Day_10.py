#Python datetime Module

'''
Why You Need datetime:

Python’s datetime module lets you:

    -Get current date & time
    -Do date math (yesterday, next week, etc.)
    -Format and parse date strings
    -Measure time durations (like how long you studied)
    -Schedule deadlines, countdowns, or reminders


1. Importing datetime:

    First install module using "pip" For ex.: pip install datetime
    Then import: "import datetime"

2. Get current date and time:

    today=datetime.date.today()
    now=datetime.datetime.now()
    print(today)                       # 2025-06-05
    print(now)                         # 2025-06-05 16:47:23.220545

3. Access Data Components: 

    print(today.month)                 # 6
    print(today.day)                   # 5
    print(today.year)                  # 2025

4. Formats Dates as Strings:

formatted = today.strftime("%d-%m-%Y")   # "17-05-2025"

Code         |        Output          |             Meaning
             |                        |
%Y and %y    |    2025 and 25         |    4 digit and 2 digit
%m           |         06             |           Month   
%d           |         05             |           Day
%A           |      Monday            |       Full Weekday
%H and %I    |    14 and 02           |      24 hr and 12 hr   
%p           |        PM              |          AM/PM

5. Time Differences (timedelta):

    import datetime
    from datetime import timedelta

    yesterday = today - timedelta(days=1)
    next_week = today + timedelta(days=7)

    print(yesterday)                     # 2025-06-04
    print(next_week)                     # 2025-06-12

 6. Parse Date Strings to datetime:

 Convert string → datetime using strptime():

 import datetime
 date_string = "2025-05-6"
 parsed = datetime.datetime.strptime(date_string, "%Y-%m-%d")
 print(parsed.date())

 
 7. Timing How Long Something Takes:

 start=datetime.datetime.now()
 end=datetime.datetime.now()

 duration = end - start
 print("Took: ",duration )
'''
