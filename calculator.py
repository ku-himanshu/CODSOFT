import tkinter as tk
from tkinter import font as tkfont

# Initialize the main window
root = tk.Tk()
root.title("Simple Calculator")

# Set the main window size
root.geometry("420x500")
root.resizable(False, False)

# Define colors inspired by the provided image
colors = {
    "bg": "#7D349B",  
    "button_bg": "#5CBDCA",  
    "button_fg": "#030303",  
    "entry_bg": "#F0DAE3",  
    "entry_fg": "#000000", 
    "button_active_bg": "#0e0e82",
    "clear_button": "#E87EA2",
    "equal_button":"#F2DC7B" 
}

# Define font styles
e_font = tkfont.Font(family="Times new roman", size=30)
b_font = tkfont.Font(family="Bell Gothic Std Black", size=16, weight="bold")


# Function to clear the entry field
def clear_entry():
    entry.delete(0, tk.END)

# Create entry widget
entry = tk.Entry(root, font=e_font, bg=colors["entry_bg"], fg=colors["entry_fg"], borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4, pady=10, padx=10, sticky="we")



# Defining buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('Clear', 5, 0)
]



# Function to update the entry field
def update_entry(text):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_text + text)

# Function to evaluate the expression
def e_expression():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error Give Valid Input...")



# Create buttons 
for (text, row, col) in buttons:
    if (text == '='):
        btn = tk.Button(root, text=text, font=b_font, bg=colors["equal_button"], fg=colors["button_fg"],
                        activebackground=colors["button_active_bg"], command=e_expression)
    elif (text == 'Clear'):
        btn = tk.Button(root, text=text, font=b_font, bg=colors["clear_button"], fg=colors["button_fg"],
                        activebackground=colors["button_active_bg"], command=clear_entry)
    else:
        btn = tk.Button(root, text=text, font=b_font, bg=colors["button_bg"], fg=colors["button_fg"],
                        activebackground=colors["button_active_bg"], command=lambda t=text: update_entry(t))
    btn.grid(row=row, column=col, padx=6, pady=6, sticky="nsew")




# Configuring row and column weights for resizing
for i in range(6):
    root.grid_rowconfigure(i, weight=2)
for i in range(4):
    root.grid_columnconfigure(i, weight=2)




root.configure(bg=colors["bg"])
root.mainloop()
