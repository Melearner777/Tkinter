import tkinter as tk
from tkcalendar import Calendar

# Create the main window
root = tk.Tk()
root.title("Date picker")
root.geometry("300x250")

# Create and place the calendar widget
cal = Calendar(root, selectmode='day', year=2024, month=1, day=1)
cal.pack(pady=20)

# Function to print the selected date
def print_date():
    print(cal.get_date())

# Create and place the button widget
button = tk.Button(root, text="Get Date", command=print_date)
button.pack(pady=20)

# Start the main event loop
root.mainloop()
