# Buttons + Events + Command Functions 
'''
1. What is Command Functions
    Command Function is a python function that runs when user clicks the button. 
Ex.:
    import tkinter as t

def greet():
    print("Hello Naveen!")

window= t.Tk()
window.title("Book Market")
window.geometry("500x400")

t.Button(window, text="Greet Me", command=greet).pack()

window.mainloop()




2. Getting Input from entry Widgets:
    To collect what the user typed, you use .get()
Ex.: 
    user_input = entry_box.get()                    #It returns the text inside the entry box


    

3. messagebox:
    Tkinter has builtin popups:
    from tkinter import messagebox

            Function                                            Use

i.    showinfor(title,message)                               info popup
ii.   showwarning(title,message)                            warning popup
iii.  showerror(title,message)                               error popup
'''
