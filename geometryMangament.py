import tkinter as tk
root=tk.Tk()
root.title("Geometry managment Example")
root.geometry("450x300")

label1=tk.Label(root,text="Pack Example",bg="red")
label1.pack(fill="x")

label2=tk.Label(root,text="Grid Example",bg="green")
label2.grid(row=1,column=0,padx=20,pady=20)

label3=tk.Label(root,text="Place Example",bg="blue")
label3.place(x=200,y=150)

root.mainloop()