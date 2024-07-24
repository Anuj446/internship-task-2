import tkinter as tk
root =tk.Tk()
root.title(" Simple Calculator")

entry = tk.Entry(root, width=25, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        expression = entry.get()
        result = str(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")



buttons = [
    'C', '', '', '/',
    '7', '8', '9', '*',
    '4', '5', '6', '-',
    '1', '2', '3', '+',
    '0', '.', '=', ''
]

row = 1
col = 0

for button in buttons:
    if button == '=':
        tk.Button(root, text=button, padx=40, pady=20, command=button_equal).grid(row=row, column=col, columnspan=2)
        col += 2
    elif button == 'C':
        tk.Button(root, text=button, padx=40, pady=20, command=button_clear).grid(row=row, column=col)
        col += 1
    elif button == '':
        col += 1
    else:
        tk.Button(root, text=button, padx=40, pady=20, command=lambda num=button: button_click(num)).grid(row=row, column=col)
        col += 1

    if col > 3:
        col = 0
        row += 1

root.mainloop()
