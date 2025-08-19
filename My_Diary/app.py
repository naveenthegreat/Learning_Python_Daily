import tkinter as tk
import os
from tkinter import messagebox
from tkinter import font
from tkcalendar import DateEntry
from tkinter import scrolledtext
import json

# Window Setup
window = tk.Tk()
window.title("📝 My Diary")
window.geometry("700x550")
window.config(bg="#19170b")

# Labels
window_label = tk.Label(window, text="My Diary", font=("Times New Roman", 30, "bold"), fg="#fffffe", bg="#19170b")
window_label.grid(row=0, column=0, columnspan=2, pady=10)

window_label1 = tk.Label(window, text="Welcome!!!", font=("Times New Roman", 15, "bold"), fg="#fffffe", bg="#19170b")
window_label1.grid(row=1, column=0, columnspan=20)

# Name Entry
name_frame = tk.Frame(window, bg="#1e1e1e")
name_frame.grid(row=2, column=0, padx=5, pady=10, sticky="w")

entry = tk.Entry(name_frame, font=("Arial", 15), fg="#fffffe", bg="#19170b")
entry.pack(side=tk.LEFT, padx=5)


# Entry widget for input
entry = tk.Entry(window, font=("Arial", 15), fg="#fffffe", bg="#19170b")
entry.grid(row=2, column=1, padx=5)

def login():
    name=entry.get().strip()
    if name:
        os.makedirs("data",exist_ok=True)
        with open("data/user.json","w") as f:
            json.dump({"username":name},f) 

        messagebox.showinfo("Welcome",f"Hello {name}, your login is saved ")
        entry.delete(0,tk.END)

    else:
        messagebox.showwarning("Oops!!!","Enter your name again")

btn=tk.Button(window,text="Login",font=("Arial",15),bg="#2ae734",command=login)
btn.grid(row=3,column=0,columnspan=2,pady=20)

# View-past entries
view_frme=tk.LabelFrame(window,text="View Past Entry",bg="#1e1e1e",fg="#ffffff",font=("Arial",10))
view_frme.grid(row=4, column=0, columnspan=2, pady=5)


calendar=DateEntry(view_frme,width=15,font=("Arial",11),background="darkblue",foreground="white",borderwidth=2)
calendar.pack(pady=5)

diary_text = scrolledtext.ScrolledText(view_frme, width=50, height=10, font=("Arial", 12), bg="#2c2c2c", fg="#FAF4D3")
diary_text.pack(pady=10)

def load_entry():
    selectedate=calendar.get_date().strftime("%Y-%m-%d")
    filepath=f"data/{selectedate}.json"

    if os.path.exists(filepath):
        with open(filepath,"r") as f:
            data=json.load(f)
        diary_text.delete("1.0",tk.END)
        mood=data.get("mood","😊")
        entry=data.get("entry","")
        diary_text.insert(tk.END,f"🟡 Mood:{mood}\n\n{entry}")

    else:
        diary_text.delete("1.0",tk.END)
        diary_text.insert(tk.END,"No Entry Found")

load_btn=tk.Button(view_frme,text="View Entry",font=("Arial",10),bg="#0984e8",fg="#ffffff",command=load_entry)
load_btn.pack(pady=5)

# Run the App
window.mainloop()