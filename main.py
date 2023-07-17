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
#root.resizable(False, False)

equation_var = StringVar()
equation_var.set(0)

equation = Label(
    root, textvariable=equation_var,
    font=("Arial", 35, "bold"), bg="#202020", fg="white", height=3,
    width=24, anchor="se", justify="right")

equation.pack()


buttonframe = Frame(root)

buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)
buttonframe.columnconfigure(3, weight=1)

buttonframe.rowconfigure(0, weight=1)
buttonframe.rowconfigure(1, weight=1)
buttonframe.rowconfigure(2, weight=1)
buttonframe.rowconfigure(3, weight=1)
buttonframe.rowconfigure(4, weight=1)


btn_7 = Button(buttonframe, text="7", bg="#43484f", font=("Arial", 50), borderwidth=0)
btn_7.grid(row=1, column=0, sticky=N + S + E + W)

btn_8 = Button(buttonframe, text="8", bg="#43484f", font=("Arial", 50), borderwidth=0)
btn_8.grid(row=1, column=1, sticky=N + S + E + W)

btn_9 = Button(buttonframe, text="9", bg="#43484f", font=("Arial", 50), borderwidth=0)
btn_9.grid(row=1, column=2, sticky=N + S + E + W)


btn_4 = Button(buttonframe, text="4", bg="#43484f", font=("Arial", 50), borderwidth=0)
btn_4.grid(row=2, column=0, sticky=N + S + E + W)

btn_5 = Button(buttonframe, text="5", bg="#43484f", font=("Arial", 50), borderwidth=0)
btn_5.grid(row=2, column=1, sticky=N + S + E + W)

btn_6 = Button(buttonframe, text="6", bg="#43484f", font=("Arial", 50), borderwidth=0)
btn_6.grid(row=2, column=2, sticky=N + S + E + W)


btn_1 = Button(buttonframe, text="1", bg="#43484f", font=("Arial", 50), borderwidth=0)
btn_1.grid(row=3, column=0, sticky=N + S + E + W)

btn_2 = Button(buttonframe, text="2", bg="#43484f", font=("Arial", 50), borderwidth=0)
btn_2.grid(row=3, column=1, sticky=N + S + E + W)

btn_3 = Button(buttonframe, text="3", bg="#43484f", font=("Arial", 50), borderwidth=0)
btn_3.grid(row=3, column=2, sticky=N + S + E + W)


multiplication_sing = Button(buttonframe, text="x", bg="#43484f", font=("Arial", 50), borderwidth=0)
multiplication_sing.grid(row=1, column=3, sticky=N + S + E + W)

subtraction_sing = Button(buttonframe, text="-", bg="#43484f", font=("Arial", 50), borderwidth=0)
subtraction_sing.grid(row=2, column=3, sticky=N + S + E + W)

addition_sing = Button(buttonframe, text="+", bg="#43484f", font=("Arial", 50), borderwidth=0)
addition_sing.grid(row=3, column=3, sticky=N + S + E + W)


buttonframe.pack(fill="both")


root.mainloop()