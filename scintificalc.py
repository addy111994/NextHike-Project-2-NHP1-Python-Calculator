import tkinter as tk
import math

# Function to update expression in calculator
def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

# Function to evaluate final expression in calculator
def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except:
        equation.set(" error ")
        expression = ""

# Function to clear display in calculator
def clear():
    global expression
    expression = ""
    equation.set("")

# scientific expression operations in calculator
def sqrt():
    try:
        global expression
        total = str(math.sqrt(float(expression)))
        equation.set(total)
        expression = total
    except:
        equation.set(" error ")
        expression = ""

def square():
    try:
        global expression
        total = str(float(expression) ** 2)
        equation.set(total)
        expression = total
    except:
        equation.set(" error ")
        expression = ""

def log():
    try:
        global expression
        total = str(math.log10(float(expression)))
        equation.set(total)
        expression = total
    except:
        equation.set(" error ")
        expression = ""

def sin():
    try:
        global expression
        total = str(math.sin(math.radians(float(expression))))
        equation.set(total)
        expression = total
    except:
        equation.set(" error ")
        expression = ""

def cos():
    try:
        global expression
        total = str(math.cos(math.radians(float(expression))))
        equation.set(total)
        expression = total
    except:
        equation.set(" error ")
        expression = ""

def tan():
    try:
        global expression
        total = str(math.tan(math.radians(float(expression))))
        equation.set(total)
        expression = total
    except:
        equation.set(" error ")
        expression = ""

# Program code
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Scientific Calculator")
    root.geometry("400x600")
    root.resizable(True, False)

    expression = ""
    equation = tk.StringVar()

    # Input field entry
    entry = tk.Entry(root, textvariable=equation, font=('Arial', 20), bd=10, insertwidth=2, width=18,
                     borderwidth=4, relief="ridge", justify='right')
    entry.grid(row=0, column=0, columnspan=5, pady=10)

    # Standard buttons layout in calculator
    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
    ]

    for (text, row, col) in buttons:
        if text == "=":
            tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 15), command=equalpress).grid(row=row, column=col)
        else:
            tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 15), command=lambda t=text: press(t)).grid(row=row, column=col)

    # Scientific function buttons in calculator
    sci_buttons = [
        ('sqrt', sqrt, 5, 0), ('x²', square, 5, 1), ('log', log, 5, 2), ('C', clear, 5, 3),
        ('sin', sin, 6, 0), ('cos', cos, 6, 1), ('tan', tan, 6, 2)
    ]

    for (text, func, row, col) in sci_buttons:
        tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 15), command=func).grid(row=row, column=col)

    root.mainloop()
