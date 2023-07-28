from tkinter import *

# colour pallet
# background: #202020
# buttons: #3B3B3B
# mathematical signs: #323232
# equation sing: #F38064

root = Tk()
root.geometry("700x590")
root.title("calculator")
root.configure(bg="#202020")
#root.resizable(False, False)

equation_var = StringVar()
equation_var_text = ("")
equation_var.set(equation_var_text)



def equation_func():
    global equation, equation_var, equation_var_text

    equation_var_text = str(eval(equation_var_text))
    equation_var.set(equation_var_text)


def add_to_label(symbol):
    global equation, equation_var, equation_var_text

    equation_var_text = equation_var_text + symbol
    equation_var.set(equation_var_text)


equation = Label(
    root, textvariable=equation_var,
    font=("Arial", 35, "bold"), bg="#202020", fg="white", height=3,
    width=24, anchor="se", justify="right")

equation.pack()


buttonframe = Frame(root, bg="#202020")

buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)
buttonframe.columnconfigure(3, weight=1)
buttonframe.columnconfigure(4, weight=1)

buttonframe.rowconfigure(0, weight=1)
buttonframe.rowconfigure(1, weight=1)
buttonframe.rowconfigure(2, weight=1)
buttonframe.rowconfigure(3, weight=1)


btn_7 = Button(buttonframe, text="7", bg="#3B3B3B", font=("Arial", 50), borderwidth=0, command=lambda: add_to_label("7"))
btn_7.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)

btn_8 = Button(buttonframe, text="8", bg="#3B3B3B", font=("Arial", 50), borderwidth=0, command=lambda: add_to_label("8"))
btn_8.grid(row=0, column=1, sticky="nsew", padx=2, pady=2)

btn_9 = Button(buttonframe, text="9", bg="#3B3B3B", font=("Arial", 50), borderwidth=0, command=lambda: add_to_label("9"))
btn_9.grid(row=0, column=2, sticky="nsew", padx=2, pady=2)


btn_4 = Button(buttonframe, text="4", bg="#3B3B3B", font=("Arial", 50), borderwidth=0, command=lambda: add_to_label("4"))
btn_4.grid(row=1, column=0, sticky="nsew", padx=2, pady=2)

btn_5 = Button(buttonframe, text="5", bg="#3B3B3B", font=("Arial", 50), borderwidth=0, command=lambda: add_to_label("5"))
btn_5.grid(row=1, column=1, sticky="nsew", padx=2, pady=2)

btn_6 = Button(buttonframe, text="6", bg="#3B3B3B", font=("Arial", 50), borderwidth=0, command=lambda: add_to_label("6"))
btn_6.grid(row=1, column=2, sticky="nsew", padx=2, pady=2)


btn_1 = Button(buttonframe, text="1", bg="#3B3B3B", font=("Arial", 50), borderwidth=0, command=lambda: add_to_label("1"))
btn_1.grid(row=2, column=0, sticky="nsew", padx=2, pady=2)

btn_2 = Button(buttonframe, text="2", bg="#3B3B3B", font=("Arial", 50), borderwidth=0, command=lambda: add_to_label("2"))
btn_2.grid(row=2, column=1, sticky="nsew", padx=2, pady=2)

btn_3 = Button(buttonframe, text="3", bg="#3B3B3B", font=("Arial", 50), borderwidth=0, command=lambda: add_to_label("3"))
btn_3.grid(row=2, column=2, sticky="nsew", padx=2, pady=2)


btn_0 = Button(buttonframe, text="0", bg="#3B3B3B", font=("Arial", 50), borderwidth=0, command=lambda: add_to_label("7"))
btn_0.grid(row=3, column=1, sticky="nsew", padx=2, pady=2)

btn_clear = Button(buttonframe, text="C", bg="#3B3B3B", font=("Arial", 50), borderwidth=0)
btn_clear.grid(row=3, column=0, sticky="nsew", padx=2, pady=2)

btn_comma = Button(buttonframe, text=",", bg="#3B3B3B", font=("Arial", 50), borderwidth=0, command=lambda: add_to_label("."))
btn_comma.grid(row=3, column=2, sticky="nsew", padx=2, pady=2)


multiplication_sign = Button(buttonframe, text="x", bg="#323232", font=("Arial", 50), borderwidth=0, command=lambda: add_to_label("*"))
multiplication_sign.grid(row=0, column=3, sticky="nsew", padx=2, pady=2)

subtraction_sign = Button(buttonframe, text="-", bg="#323232", font=("Arial", 50), borderwidth=0, command=lambda: add_to_label("-"))
subtraction_sign.grid(row=1, column=3, sticky="nsew", padx=2, pady=2)

addition_sign = Button(buttonframe, text="+", bg="#323232", font=("Arial", 50), borderwidth=0, command=lambda: add_to_label("+"))
addition_sign.grid(row=2, column=3, sticky="nsew", padx=2, pady=2)

division_sign = Button(buttonframe, text="/", bg="#323232", font=("Arial", 50), borderwidth=0, command=lambda: add_to_label("/"))
division_sign.grid(row=3, column=3, sticky="nsew", padx=2, pady=2)


equation_sign = Button(buttonframe, text="=", bg="#F38064", font=("Arial", 50), borderwidth=0, command=equation_func)
equation_sign.grid(row=0, column=4, sticky="nsew", rowspan=4, padx=2, pady=2)


buttonframe.pack(fill="both", expand=True)


root.mainloop()