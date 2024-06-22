import tkinter as tk
from tkinter import ttk, messagebox

def calculate(operation):
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                messagebox.showerror("Error", "Division by zero is not allowed.")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Invalid Operation")
            return

        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numeric values.")

root = tk.Tk()
root.title("Calculator")

ttk.Label(root, text="Number 1:").grid(row=0, column=0, padx=10, pady=10)
entry_num1 = ttk.Entry(root)
entry_num1.grid(row=0, column=1, padx=10, pady=10)

ttk.Label(root, text="Number 2:").grid(row=1, column=0, padx=10, pady=10)
entry_num2 = ttk.Entry(root)
entry_num2.grid(row=1, column=1, padx=10, pady=10)

ttk.Button(root, text="+", command=lambda: calculate("+")).grid(row=2, column=0, padx=10, pady=10)
ttk.Button(root, text="-", command=lambda: calculate("-")).grid(row=2, column=1, padx=10, pady=10)
ttk.Button(root, text="*", command=lambda: calculate("*")).grid(row=2, column=2, padx=10, pady=10)
ttk.Button(root, text="/", command=lambda: calculate("/")).grid(row=2, column=3, padx=10, pady=10)

result_label = ttk.Label(root, text="Result: ")
result_label.grid(row=3, column=0, columnspan=4, padx=10, pady=10)

root.mainloop()
