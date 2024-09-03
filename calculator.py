import tkinter as tk
from tkinter import messagebox

def calculate(operation):
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())

        if operation == "Add":
            result = int(num1 + num2)
        elif operation == "Subtract":
            result = int(num1 - num2)
        elif operation == "Multiply":
            result = int(num1 * num2)
        elif operation == "Divide":
            if num2 == 0:
                messagebox.showwarning("Warning", "Cannot divide by zero!")
                return
            result = int(num1 / num2)  # Convert the result to an integer

        entry_result.delete(0, tk.END)  # Clear the result box
        entry_result.insert(0, str(result))  # Display the result
    except ValueError:
        messagebox.showwarning("Warning", "Please enter valid numbers.")

# Create main window
window = tk.Tk()
window.title("Simple Calculator")

# Input fields for numbers
label_num1 = tk.Label(window, text="Enter first number:")
label_num1.pack()

entry_num1 = tk.Entry(window)
entry_num1.pack()

label_num2 = tk.Label(window, text="Enter second number:")
label_num2.pack()

entry_num2 = tk.Entry(window)
entry_num2.pack()

# Buttons for operations
button_add = tk.Button(window, text="Add", command=lambda: calculate("Add"))
button_add.pack()

button_subtract = tk.Button(window, text="Subtract", command=lambda: calculate("Subtract"))
button_subtract.pack()

button_multiply = tk.Button(window, text="Multiply", command=lambda: calculate("Multiply"))
button_multiply.pack()

button_divide = tk.Button(window, text="Divide", command=lambda: calculate("Divide"))
button_divide.pack()

# Entry to display result in a white box
entry_result = tk.Entry(window, bg="white", fg="black")
entry_result.pack()

# Run the application
window.mainloop()
