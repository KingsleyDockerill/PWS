from tkinter import *
from tkinter import messagebox

with open("passwords.passwords", "a+") as f:
    root = Tk()
    root.geometry("1000x1000")
    root.wm_title("Info Collect")

    mylist = []

    var1 = StringVar()
    var1.set("Application:")
    label1 = Label(root, textvariable=var1, height=2)
    label1.grid(row=0, column=0)
    var2 = StringVar()
    var2.set("Password:")
    label2 = Label(root, textvariable=var2, height=2)
    label2.grid(row=0, column=3)

    ID1 = StringVar()
    ID2 = StringVar()
    box1 = Entry(root, bd=4, textvariable=ID1)
    box1.grid(row=0, column=1)
    box2 = Entry(root, bd=5, textvariable=ID2)
    box2.grid(row=0, column=4)


    def get_info():
        f.write(", {0}: {1}".format(box1.get(), box2.get()))

    def output_info():
        f.seek(0)
        messagebox.showinfo("Passwords", f.read())

    buttonA = Button(root, text="Save info", command=get_info, width=8)
    buttonA.grid(row=0, column=2)
    buttonB = Button(root, text="Output info", command=output_info, width=8)
    buttonB.grid(row=0, column=5)

    root.mainloop()