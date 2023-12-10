import customtkinter
from tkinter import *
from tkinter import messagebox

app = customtkinter.CTk()
app.title("Calculator")
app.geometry("250x350")
app.config(bg="#000000")

font1 = ('Arial', 20, 'bold')

i = 0
equation = ""
previous_result = None

def show(value):
    global i
    global equation
    if(value == "%"):
        value="/100"
    equation += value
    result_entry.insert(i, value)
    i = i + 1

def clear():
    global equation
    result_entry.delete(0, END)
    equation=""


def calculate():
    try:
        global equation
        global previous_result
        result = ""
        if previous_result is not None:
            equation = str(previous_result) + equation
        result = eval(equation)
        clear()
        result_entry.insert(0, result)
        previous_result = result
    except:
        messagebox.showerror(title="Error",message="Please enter a valid number!")

result_entry = customtkinter.CTkEntry(app, width=250, font=font1,fg_color="#000000", border_color="#000000")
result_entry.place(x=0, y=10)

Button_clear = customtkinter.CTkButton(app, command=clear, text="C", font=font1, width=50, height=2, fg_color="#b5520b",
                                border_color="#b5520b")
Button_clear.place(x=10, y=60)

Button_percent = customtkinter.CTkButton(app, command=lambda: show("%"), text="%", font=font1, width=50, height=2,
                                   fg_color="#b5520b", border_color="#b5520b")
Button_percent.place(x=70, y=60)

Button_divide = customtkinter.CTkButton(app, command=lambda: show("/"), text="/", font=font1, width=50, height=2,
                                  fg_color="#b5520b", border_color="#b5520b")
Button_divide.place(x=130, y=60)

Button_multiply = customtkinter.CTkButton(app, command=lambda: show("*"), text="x", font=font1, width=50, height=2,
                                    fg_color="#b5520b", border_color="#b5520b")
Button_multiply.place(x=190, y=60)

Button_7 = customtkinter.CTkButton(app, command=lambda: show("7"), text="7", font=font1, width=50, height=2,
                             fg_color="#2e2a27", border_color="#2e2a27")
Button_7.place(x=10, y=120)

Button_8 = customtkinter.CTkButton(app, command=lambda: show("8"), text="8", font=font1, width=50, height=2,
                             fg_color="#2e2a27", border_color="#2e2a27")
Button_8.place(x=70, y=120)

Button_9 = customtkinter.CTkButton(app, command=lambda: show("9"), text="9", font=font1, width=50, height=2,
                             fg_color="#2e2a27", border_color="#2e2a27")
Button_9.place(x=130, y=120)

Button_add = customtkinter.CTkButton(app, command=lambda: show("+"), text="+", font=font1, width=50, height=2,
                               fg_color="#b5520b", border_color="#b5520b")
Button_add.place(x=190, y=120)

Button_4 = customtkinter.CTkButton(app, command=lambda: show("4"), text="4", font=font1, width=50, height=2,
                             fg_color="#2e2a27", border_color="#2e2a27")
Button_4.place(x=10, y=180)

Button_5 = customtkinter.CTkButton(app, command=lambda: show("5"), text="5", font=font1, width=50, height=2,
                             fg_color="#2e2a27", border_color="#2e2a27")
Button_5.place(x=70, y=180)

Button_6 = customtkinter.CTkButton(app, command=lambda: show("6"), text="6", font=font1, width=50, height=2,
                             fg_color="#2e2a27", border_color="#2e2a27")
Button_6.place(x=130, y=180)

Button_subtract = customtkinter.CTkButton(app, command=lambda: show("-"), text="-", font=font1, width=50, height=2,
                                    fg_color="#b5520b", border_color="#b5520b")
Button_subtract.place(x=190, y=180)

Button_0 = customtkinter.CTkButton(app, command=lambda: show("0"), text="0", font=font1, width=50, height=2,
                             fg_color="#2e2a27", border_color="#2e2a27")
Button_0.place(x=10, y=240)

Button_1 = customtkinter.CTkButton(app, command=lambda: show("1"), text="1", font=font1, width=50, height=2,
                             fg_color="#2e2a27", border_color="#2e2a27")
Button_1.place(x=70, y=240)

Button_2 = customtkinter.CTkButton(app, command=lambda: show("2"), text="2", font=font1, width=50, height=2,
                             fg_color="#2e2a27", border_color="#2e2a27")
Button_2.place(x=130, y=240)

Button_3 = customtkinter.CTkButton(app, command=lambda: show("3"), text="3", font=font1, width=50, height=2,
                             fg_color="#2e2a27", border_color="#2e2a27")
Button_3.place(x=190, y=240)

Button_dot = customtkinter.CTkButton(app, command=lambda: show("."), text=".", font=font1, width=50, height=2,
                               fg_color="#2e2a27", border_color="#2e2a27")
Button_dot.place(x=10, y=300)

Button_equal = customtkinter.CTkButton(app, command=calculate, text="=", font=font1, width=170, height=2,
                                 fg_color="#b5520b", border_color="#b5520b")
Button_equal.place(x=70, y=300)

app.mainloop()
