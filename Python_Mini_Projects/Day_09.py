#Python Learning Log (with File Handling)

import datetime
import json
import os

today=datetime.date.today().strftime("%Y-%m-%d")

status=input("Did you study python today (Yes/No): ").strip().lower()

log_entry={}
if status=="yes":
    topic=input("What topic learn: ")
    log_entry={
        "status":"Yes",
        "topic": topic
    }

elif status=="no":
    reason=input("Give reason why not you study? ")
    log_entry={
        "status":"No",
        "reason":reason
    }

else:
    print("You enter the invalid! Please enter Yes or No")
    exit

print(f"\n Log of {today}")
print(log_entry)

filename="learning_log.json"

if os.path.exists(filename):
    with open(filename,"r") as f:
        data=json.load(f)

else:
    data={}

data[today]=log_entry

with open(filename,"w") as f:
    json.dump(data,f,indent=5)

print("\n Log Saved Successfully to learning_log.json")


