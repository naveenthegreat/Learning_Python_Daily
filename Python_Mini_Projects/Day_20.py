import tkinter as tk
from tkinter import messagebox
import json
from datetime import datetime
import os

# Create window
app = tk.Tk()
app.title("Habit Tracker - Check-In")
app.geometry("400x350")

# Input fields
tk.Label(app, text="What did you learn today?").grid(row=0, column=0, padx=5, pady=10, sticky="e")
entry_topic = tk.Entry(app, width=30)
entry_topic.grid(row=0, column=1)

tk.Label(app, text="Why did you skip?").grid(row=1, column=0, padx=5, sticky="e")
entry_reason = tk.Entry(app, width=30)
entry_reason.grid(row=1, column=1)

tk.Label(app, text="Minutes studied:").grid(row=2, column=0, padx=5, sticky="e")
entry_minutes = tk.Entry(app, width=30)
entry_minutes.grid(row=2, column=1)

# JSON file path
file_path = "checkin_data.json"

# Submit function
def submit_checkin():
    topic = entry_topic.get()
    reason = entry_reason.get()
    minutes = entry_minutes.get()

    if not topic and not reason and not minutes:
        messagebox.showwarning("Missing Data", "❌ Please fill at least one field.")
        return

    # Format today's date
    today = datetime.today().strftime("%Y-%m-%d")

    # Data to save
    data_to_save = {
        "topic": topic,
        "reason": reason,
        "minutes": minutes
    }

    # Load existing data
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            existing_data = json.load(file)
    else:
        existing_data = {}

    # Add or update today's entry
    existing_data[today] = data_to_save

    # Save back to file
    with open(file_path, "w") as file:
        json.dump(existing_data, file, indent=4)

    messagebox.showinfo("Success", f"✅ Check-in saved for {today}!")

    # Clear fields
    entry_topic.delete(0, tk.END)
    entry_reason.delete(0, tk.END)
    entry_minutes.delete(0, tk.END)

# Submit button
tk.Button(app, text="Submit", command=submit_checkin).grid(row=3, column=0, columnspan=2, pady=20)

app.mainloop()
