import tkinter as tk
root=tk.Tk()
root.title("buttons")
root.geometry("300x120")
def on_click():
    print("Button Clicked")

button=tk.Button(root,text="Click Me ",command=on_click)
button.pack()

root.mainloop()