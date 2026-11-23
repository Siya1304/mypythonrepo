from tkinter import Label, Tk
from time import strftime

root = Tk()
root.title("Clock")
clock = Label(root, font=("Arial", 48), padx=20, pady=10)
clock.pack()

def update():
    clock.config(text=strftime("%H:%M:%S"))
    clock.after(1000, update)

update()
root.mainloop()