import tkinter as tk


def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operator = operator_var.get()

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = num1 / num2

        result_label.config(text="Result: " + str(result),
                            font=("Arial", 20, "bold"), fg="blue")
    except ValueError:
        result_label.config(text="Invalid input!", fg="red")


root = tk.Tk()
root.title("Wabweni Brian's Calculator")

# Set window size
root.geometry("500x300")  # Width x Height

# Add spacing between elements
element_spacing = 10

# Entry labels
label1 = tk.Label(root, text="Number 1:")
label1.pack()


# Entry fields for numbers
entry1 = tk.Entry(root, width=35)
entry1.pack(pady=element_spacing)

label2 = tk.Label(root, text="Number 2:")
label2.pack()

entry2 = tk.Entry(root, width=35)
entry2.pack(pady=element_spacing)

# Operator selection
operator_var = tk.StringVar(root)
operator_var.set('+')
operator_menu = tk.OptionMenu(root, operator_var, '+', '-', '*', '/')
operator_menu.config(width=17)
operator_menu.pack(pady=element_spacing)

# Button to calculate result
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.config(width=19)
calculate_button.pack(pady=element_spacing)

# Label to display result
result_label = tk.Label(root)
result_label.pack(pady=element_spacing)

root.mainloop()
