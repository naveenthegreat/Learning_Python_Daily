# Tkinter

import tkinter as tx

window = tx.Tk()

window.title("Girte Sitaare")

window.geometry("700x500")

welcome_label = tx.Label(window,text = "Girte Sitaare",font=("Arial",18,"bold"),bg="#9ed4e2")
welcome_label.pack()

pokemon_label = tx.Label(window,text="A Great Novel By N.K.Nayak", font=("Arial",10),bg="#e6f2ff")
pokemon_label.pack(pady=10)

name_label = tx.Label(window, text="Created by Naveen", font=("Arial", 12),bg="#e6f2ff")
name_label.pack()

date_label = tx.Label(window, text="Date: 2025-07-01", font=("Arial", 12),bg="#e6f2ff")
date_label.pack()

window.configure(bg="#e6f2ff")

window.mainloop()