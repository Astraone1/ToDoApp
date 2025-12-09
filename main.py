
# Let's go!

import tkinter as tk

def submit():
    input_field.delete(0, tk.END)

root = tk.Tk()
root.geometry("500x500")
root.title("To-Do App")

label = tk.Label(root, text="Meine To-Do App")
label.pack()

input_field = tk.Entry(root)
input_field.pack()

button = tk.Button(root, text="Submit", command=submit)
button.pack()










root.mainloop()