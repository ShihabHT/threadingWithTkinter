import tkinter as tk
import time
import threading

root = tk.Tk()

root.title("Threading with tkinter")
root.geometry("600x400")

label = tk.Label(root, text="Snake egg", bg="red")
label.pack(padx=20, pady=20)


def change_egg():
    time.sleep(5)
    print("Conversion started, Please wait...")
    val = label.cget('text')
    if val == 'Ostrich Egg':
        label.config(text="Snake egg")
    elif val == "Snake egg":
        label.config(text='Ostrich Egg')


button1 = tk.Button(root, text="Convert Egg", command=threading.Thread(target=change_egg).start())
button1.pack()


def make_decision():
    print("Changing decision, Please wait...")
    val = label1.cget('text')
    if val == "But Chicken came first":
        label1.config(text="But egg came first")
    elif val == "But egg came first":
        label1.config(text='But Chicken came first')


label1 = tk.Label(root, text="But Chicken came first", bg="red")
label1.pack()
button2 = tk.Button(root, text='DECIDE', command=threading.Thread(target=make_decision).start())
button2.pack()

root.mainloop()
