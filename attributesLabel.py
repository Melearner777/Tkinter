from tkinter import *
root=Tk()
root.geometry("450x233")
root.title("My GUI with Harry")

# Import Label Options
# text- adds the Text
# bd-background
# fg-foreground
# font-sets the font
# padx-padding in X
# pady-padding in Y
# relief-border styling- SUNKEN,RAISED,GROOVE,RIDGE

title_label=Label(text='''hlo  how r u . I am fine allhamdulillah!. What about you''',bg="green",fg="Yellow",padx=23,pady=4,font=("Arial Black",9,"bold"),borderwidth=3,relief=SUNKEN)
title_label.pack()

#IMPORTANT PACK OPTION
#side=top,bottom,left,right


title_label.pack(side="bottom",anchor="ne")

root.mainloop()