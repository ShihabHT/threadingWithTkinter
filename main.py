import tkinter as tk
import time

root = tk.Tk()

root.title("Threading with tkinter")
root.geometry("600x400")

label = tk.Label(root, text="Snake egg", bg="red")
label.pack(padx=20, pady=20)


def change_egg():
    time.sleep(5)
    print("Conversion started, Please wait...")
    val = label.cget('text')
    if val == "Ostrich Egg":
        label.config(text="Snake egg")
    elif val == "Snake egg":
        label.config(text='Ostrich Egg')


button1 = tk.Button(root, text="Convert Egg", command=change_egg)
button1.pack()

button2 = tk.Button(root, )
root.mainloop()
