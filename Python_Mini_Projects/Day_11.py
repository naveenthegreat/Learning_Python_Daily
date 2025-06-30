import json
import datetime
import random
import os

FILENAME = "birthdays.json"

# Function to load data
def load_birthdays():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return json.load(file)
    return {}

# Function to save data
def save_birthdays(birthdays):
    with open(FILENAME, "w") as file:
        json.dump(birthdays, file, indent=4)

# Function to add a new birthday
def add_birthday():
    name = input("Enter name: ")
    bday = input("Enter birthday (YYYY-MM-DD): ")
    birthdays[name] = bday
    save_birthdays(birthdays)
    print("🎉 Birthday saved!")

# Function to check for today’s birthdays
def check_today():
    today = datetime.date.today().strftime("%Y-%m-%d")
    for name, date in birthdays.items():
        if date == today:
            print(f"🎈 Today is {name}'s birthday!")
            print(f"🔮 Lucky Number for {name}: {random.randint(1, 100)}")
            return
    print("😶 No birthdays today.")

# Load existing data
birthdays = load_birthdays()

# Menu
while True:
    print("\n🎂 Birthday Reminder App")
    print("1. Add Birthday")
    print("2. Check Today's Birthdays")
    print("3. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_birthday()
    elif choice == "2":
        check_today()
    elif choice == "3":
        print("👋 Goodbye!")
        break
    else:
        print("❗Invalid choice.")
