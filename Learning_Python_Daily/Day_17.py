# Tkinter  
'''
Tkinter is python's standard library for creating simple and interactive GUI applications.

'''
import tkinter as tk

# Step 1: Create the main app window
window = tk.Tk()

# Step 2: Set the title of the window
window.title("Habit Tracker")

# Step 3: Set the size of the window (width x height)
window.geometry("600x400")

# Step 4: Add a welcome label
welcome_label = tk.Label(window, text="Welcome to Your Daily Habit Tracker!", font=("Arial", 16))
welcome_label.pack(pady=20)  # Padding on y-axis

# Step 5: Start the GUI loop
window.mainloop()
