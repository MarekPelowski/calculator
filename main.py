from tkinter import *

# colour pallet
# background: #202020
# buttons: #3B3B3B
# mathematical signs: #323232
# equation sing: #F38064

root = Tk()
root.geometry("415x590")
root.title("calculator")
root.configure(bg="#202020")
root.resizable(False, False)

equation_var = StringVar()
equation_var.set(0)

equation = Label(
    root, textvariable=equation_var,
    font=("Arial", 35, "bold"), bg="#202020", fg="white", height=3,
    width=24, anchor="se", justify="right")

equation.pack()

root.mainloop()