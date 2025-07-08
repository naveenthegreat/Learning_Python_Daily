
import tkinter as t
from tkinter import messagebox

#creating window
app = t.Tk()
app.title("Habit Tracker")
app.geometry("400x300")

#Entry fields 
t.Label(app, text="What did you learn today").grid(row=0,column=0,padx=5,pady=0)
entry_topic=t.Entry(app,width=30)
entry_topic.grid(row=0,column=1,padx=5)

t.Label(app,text="How many minutes did you study?").grid(row=1,column=0,padx=5,pady=0)
entry_reason=t.Entry(app,width=30)
entry_reason.grid(row=1,column=1,padx=5)

#Function to run when button is clicked
def checkin_():
    topic=entry_topic
    reason=entry_reason

    if topic:
        message = f"Check in Saved : {topic}"
        if reason:
            message += f"\nReason:{reason}"
        messagebox.showinfo("Success","Succed")

    else:
        messagebox.showwarning("You not filled correctly","Not Succed")

#Submit button
s_btn = t.Button(app,text="Submit",command=checkin_)
s_btn.grid(row=2,column=0,columnspan=2,pady=20)

app.mainloop()