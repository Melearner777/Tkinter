import tkinter as tk
from tkinter import colorchooser

root = tk.Tk()
root.title("Color Picker")
root.geometry("500x300")


def choose_color():
    color_code = colorchooser.askcolor(title="Choose a color")
    print(color_code)

# Create and place the button widget
button = tk.Button(root, text="Pick a color", command=choose_color, bg="Pink", fg="Red")
button.pack(pady=20)

# Start the main event loop
root.mainloop()
