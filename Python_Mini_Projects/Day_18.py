import tkinter as tx

window= tx.Tk()
window.title("Book Market")
window.geometry("500x400")

#Heading
head= tx.Label(window,text="Buy Great Novel",font=("Verdana",15,"bold"))
head.grid(row=0, column=1, columnspan=2, pady=10)

#Topic label and entry
tx.Label(window,text="Novel Name",font=("Verdana",10)).grid(row=1, column=0, padx=5, pady=5)
topic_entry=tx.Entry(window,width=25)
topic_entry.grid(row=1, column=1, padx=5, pady=5)

#Quantity 
tx.Label(window,text="How much you want",font=("Verdana",10)).grid(row=2,column=0,padx=5,pady=5)
quantity=tx.Entry(window,width=25)
quantity.grid(row=2,column=1,padx=5,pady=5)

#Submit button
submit_btn=tx.Button(window,text="Submit")
submit_btn.grid(row=3,column=0,columnspan=2,pady=10)

window.mainloop()