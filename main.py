from tkinter import *

# colour pallet
# background: #202020
# buttons: #3B3B3B
# mathematical signs: #323232
# equation sing: #F38064
# operations: #9C9C9C

root = Tk()
root.geometry("900x590")
root.title("calculator")
root.configure(bg="#202020")
root.state("zoomed")


def delete_zeros():
    global current_num, current_num_var, current_num_text

    current_num_text = current_num_text.lstrip('0')

def clear():
    global current_num, current_num_var, current_num_text

    current_num_text = "0"
    current_num_var.set(current_num_text)
    delete_zeros()

    operations_text = ""
    operations_var.set(operations_text)

def equation_func():
    global current_num, current_num_var, current_num_text, operations_text, operations_var

    try:
        current_num_text = str(eval(operations_text))
        current_num_var.set(current_num_text)
        delete_zeros()

        operations_text = operations_text + "="
        operations_var.set(operations_text)
    except ZeroDivisionError:
        current_num_text = "0"
        current_num_var.set("cannot be divided by 0")
        delete_zeros()
    except SyntaxError:
        current_num_text = "0"
        current_num_var.set("syntax error")
        delete_zeros()

def add_to_label(symbol):
    global current_num, current_num_var, current_num_text, operations_text, operations_var

    current_num_text = current_num_text + symbol
    current_num_var.set(current_num_text)
    delete_zeros()

    operations_text = operations_text + symbol


def add_to_label_sign(symbol):
    global current_num, current_num_var, current_num_text, operations_text, operations_var

    current_num_text = ""
    operations_text = operations_text + symbol
    operations_var.set(operations_text)

operations_var = StringVar()
operations_text = ("")
operations_var.set(operations_text)


current_num_var = StringVar()
current_num_text = ("0")
current_num_var.set(current_num_text)
delete_zeros()


fill = Label(root, bg="#202020", height=6)

fill.pack()


operations = Label(
    root, textvariable=operations_var,
    font=("Arial", 25, "bold"), bg="#202020", fg="#9C9C9C"
    )

operations.pack(anchor="se", padx=100)

current_num = Label(
    root, textvariable=current_num_var,
    font=("Arial", 35, "bold"), bg="#202020", fg="white")


current_num.pack(ancho="se", padx=100)




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


btn_0 = Button(buttonframe, text="0", bg="#3B3B3B", font=("Arial", 50), borderwidth=0, command=lambda: add_to_label("0"))
btn_0.grid(row=3, column=1, sticky="nsew", padx=2, pady=2)

btn_clear = Button(buttonframe, text="C", bg="#3B3B3B", font=("Arial", 50), borderwidth=0, command=clear)
btn_clear.grid(row=3, column=0, sticky="nsew", padx=2, pady=2)

btn_comma = Button(buttonframe, text=",", bg="#3B3B3B", font=("Arial", 50), borderwidth=0, command=lambda: add_to_label("."))
btn_comma.grid(row=3, column=2, sticky="nsew", padx=2, pady=2)


multiplication_sign = Button(buttonframe, text="x", bg="#323232", font=("Arial", 50), borderwidth=0, command=lambda: add_to_label_sign("*"))
multiplication_sign.grid(row=0, column=3, sticky="nsew", padx=2, pady=2)

subtraction_sign = Button(buttonframe, text="-", bg="#323232", font=("Arial", 50), borderwidth=0, command=lambda: add_to_label_sign("-"))
subtraction_sign.grid(row=1, column=3, sticky="nsew", padx=2, pady=2)

addition_sign = Button(buttonframe, text="+", bg="#323232", font=("Arial", 50), borderwidth=0, command=lambda: add_to_label_sign("+"))
addition_sign.grid(row=2, column=3, sticky="nsew", padx=2, pady=2)

division_sign = Button(buttonframe, text="/", bg="#323232", font=("Arial", 50), borderwidth=0, command=lambda: add_to_label_sign("/"))
division_sign.grid(row=3, column=3, sticky="nsew", padx=2, pady=2)


equation_sign = Button(buttonframe, text="=", bg="#F38064", font=("Arial", 50), borderwidth=0, command=equation_func)
equation_sign.grid(row=0, column=4, sticky="nsew", rowspan=4, padx=2, pady=2)


buttonframe.pack(fill="both", expand=True)


root.mainloop()