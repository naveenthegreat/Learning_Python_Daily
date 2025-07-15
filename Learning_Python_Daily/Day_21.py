# Required tools for streak :
'''
Tools :    datetime,json and streak.json(separate file to store streak count)

Step-by-step:

1. Load past checl-in
    with open("checkin_date.json") as f:
        data = json.load(f)                    #This gives us all previous dates

        
2. Sort the dates
    Converts keys (which are strings) to date.time objects

Ex.: 
    from datetime import datetime, timedelta

    date = [datetime.strptime(date,%y-%m-%d).date() for date in data.keys()]
    date.sort()
    
'''