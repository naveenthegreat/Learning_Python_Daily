# Layout in Tkinter :
'''
Your app window is like an empty canvas. Layout managers decides where each button,label or box 
will appear.


Tkinter has 3 layout systems :

1 .pack()  -> vertical/horizontal stacking (basic layout):
    "Auto-stakcs widgets vertically (top to bottom) or horizontally (left to right)"

Syntax: 
        widget.pack(side="top", fill="x", padx=10, pady=5)
      
        Here: 
              fill      = x,y both - fills horizontally or vertically
              padx/pady = adds spacing around widget

    
        
2 .grid()  -> table-based positioning (rows and columns)
    "Arrange widgets in rows and columns (like Excel or calender grid)"

Syntax:
        widget.grid(row=0, column=1, padx=5, pady= 10)
        
        Here:
              columnspan, rowspan	= Stretch across multiple cells
        

        
3 .place() -> absolute positioning (x,y)
    "Place widgets at exact x, y coodinates."

Syntax:
        widgets.place(x=100, y=200)                    # Use only for small fine-tuning or special effects (not for full layout).

'''