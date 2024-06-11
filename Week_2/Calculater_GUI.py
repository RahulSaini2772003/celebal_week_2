import tkinter as tk
from PIL import Image,ImageTk

def on_button_click(text):
    if text == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
        
    elif text == 'X':
        if entry.get() == 'Error' :
            entry.delete(0, tk.END)
        current_index = entry.index(tk.INSERT)
        if current_index:
            entry.delete(f"{current_index-1}")
    else:
        entry.insert(tk.INSERT, text)

root = tk.Tk()
root.title("Basic Calculator With GUI")
root.iconphoto(True,tk.PhotoImage(file='img\icon.png'))
root.configure(background='lightblue')


root.resizable(0,0)

entry = tk.Entry(root, font=("Helvetica", 20),borderwidth=5,width=15,background='lightpink')
entry.grid(row=0, column=0, columnspan=5)


buttons = [
    ("X", 1, 0), ("C", 1, 1), (".", 1, 2), ("/", 1, 3),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("*", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
    ("(", 5, 0), ("0", 5, 1), (")", 5, 2), ("=", 5, 3)
]
org = Image.open('img\clear.png')
image1 = org.resize((40, 40))
image1 = ImageTk.PhotoImage(image1)
org = Image.open('img\cross.png')
image2 = org.resize((50, 50))
image2 = ImageTk.PhotoImage(image2)
bg = 'lightgreen'
for (text, row, col) in buttons:
    if text == 'C':
        button = tk.Button(root, font=("Helvetica", 20), command=lambda t=text: on_button_click(t),height=50,width=50,image=image1,justify='left',background=bg)
    elif text == 'X':
        button = tk.Button(root, font=("Helvetica", 20), command=lambda t=text: on_button_click(t),height=50,width=50,image=image2,justify='left', background=bg)
    else :    
        button = tk.Button(root, text=text, font=("Helvetica", 20), command=lambda t=text: on_button_click(t),height=1,width=3,background=bg, justify='center')
    button.grid(row=row, column=col, columnspan=2)

root.mainloop()

