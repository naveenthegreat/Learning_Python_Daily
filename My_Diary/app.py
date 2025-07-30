import tkinter as tk
import os
from tkinter import messagebox
import json

# Window Setup
window = tk.Tk()
window.title("📝 My Diary")
window.geometry("500x400")
window.config(bg="#19170b")

# Labels
window_label = tk.Label(window, text="My Diary", font=("Times New Roman", 30, "bold"), fg="#fffffe", bg="#19170b")
window_label.grid(row=0, column=0, columnspan=2, pady=10)

window_label1 = tk.Label(window, text="Welcome!!!", font=("Times New Roman", 15, "bold"), fg="#fffffe", bg="#19170b")
window_label1.grid(row=1, column=0, columnspan=20)

label = tk.Label(window, text="Enter Your Name: ", font=("Arial", 15), fg="#fffffe", bg="#19170b")
label.grid(row=2, column=0, padx=5,pady=5, sticky="e")

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

# Run the App
window.mainloop()