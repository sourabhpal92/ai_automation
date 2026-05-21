import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self):
        self.current_input = ''
        self.result = 0
        self.window = tk.Tk()
        self.window.title("Calculator")

        # Create display screen
        self.display = tk.Entry(self.window, width=20, borderwidth=5, justify=tk.RIGHT)
        self.display.grid(row=0, column=0, columnspan=4)

        # Create button grid
        self.create_button_grid()

    def create_button_grid(self):
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            tk.Button(self.window, text=button, width=5, command=lambda button=button: self.handle_input(button)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        tk.Button(self.window, text="AC/C", width=22, command=self.clear_input).grid(row=row_val, column=0, columnspan=4)

    def handle_input(self, key):
        if key == '=':
            self.calculate_result()
        elif key == 'AC/C':
            self.clear_input()
        else:
            self.current_input += str(key)
            self.update_display()

    def calculate_result(self):
        try:
            self.result = eval(self.current_input)
            self.update_display(self.result)
        except ZeroDivisionError:
            self.update_display("Error")
        except Exception as e:
            self.update_display("Error")

    def clear_input(self):
        self.current_input = ''
        self.result = 0
        self.update_display(0)

    def update_display(self, value=None):
        if value is None:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.current_input)
        else:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(value))

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calculator = Calculator()
    calculator.run()