import re
import tkinter as tk
from tkinter import messagebox


def evaluate_expression(expression):
    """
    Evaluates a mathematical expression using Python's eval function.
    """
    safe_expression = re.sub(r'[^\d\+\-\*/\%\(\)\.\*\*]', '', expression)
    try:
        result = eval(safe_expression)
    except ZeroDivisionError:
        result = "Error: Division by zero."
    except Exception as e:
        result = f"Error: {str(e)}"
    return result


def on_button_click(event):
    """
    Handles button click events.
    """
    text = event.widget.cget("text")
    if text == "=":
        try:
            expression = entry.get()
            result = evaluate_expression(expression)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Error", f"Invalid Expression: {str(e)}")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)


def create_calculator_gui():
    """
    This function will Creates the GUI for the calculator.
    """
    global entry

    root = tk.Tk()
    root.title("Basic Calculator")
    root.configure(
        bg="sky blue")  # Set the background color of the main window

    entry = tk.Entry(root,
                     font="Calibri 20",
                     borderwidth=5,
                     relief=tk.SUNKEN,
                     bg="white")
    entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    buttons = [
        '7', '8', '9', '/', '4', '5', '6', '*', '1', '2', '3', '-', '0', '.',
        '=', '+', 'C'
    ]

    row = 1
    col = 0
    for button in buttons:
        b = tk.Button(root,
                      text=button,
                      font="calibri 20",
                      padx=18,
                      pady=18,
                      bg="dark blue",
                      fg="white",
                      activebackground="darkblue",
                      activeforeground="white")
        b.grid(row=row, column=col, padx=5, pady=5)
        b.bind("<Button-1>", on_button_click)
        col += 1
        if col > 3:
            col = 0
            row += 1

    root.mainloop()


if __name__ == "__main__":
    create_calculator_gui()
