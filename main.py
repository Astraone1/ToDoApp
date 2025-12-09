import tkinter as tk
from tkinter import ttk

def submit():
    new_todo = input_field.get().strip()
    if new_todo == "":
        return

    # Frame für eine To-Do-Zeile
    todo_frame = tk.Frame(todo_container, bg="#f0f0f0", bd=1, relief="solid")
    todo_frame.pack(fill="x", pady=5, padx=5)

    # Checkbox für erledigt / nicht erledigt
    var = tk.BooleanVar()
    checkbox = tk.Checkbutton(todo_frame, variable=var, bg="#f0f0f0")
    checkbox.pack(side="left", padx=5)

    # Label mit To-Do Text
    todo_label = tk.Label(todo_frame, text=new_todo, bg="#f0f0f0", anchor="w")
    todo_label.pack(side="left", fill="x", expand=True, padx=5)

    # Delete-Button
    delete_button = tk.Button(todo_frame, text="✖", bg="#ff4d4d", fg="white",
                              command=todo_frame.destroy, bd=0)
    delete_button.pack(side="right", padx=5)

    input_field.delete(0, tk.END)

# Hauptfenster
root = tk.Tk()
root.geometry("500x600")
root.title("Meine hübsche To-Do App")

# Titel
title_label = tk.Label(root, text="Meine To-Do App", font=("Arial", 20, "bold"))
title_label.pack(pady=10)

# Eingabefeld + Submit
input_frame = tk.Frame(root)
input_frame.pack(pady=5)

input_field = tk.Entry(input_frame, width=35, font=("Arial", 12))
input_field.pack(side="left", padx=(0,5))

submit_button = tk.Button(input_frame, text="Add", font=("Arial", 12, "bold"),
                          bg="#4caf50", fg="white", command=submit)
submit_button.pack(side="left")

# Scrollbarer Container für To-Dos
canvas = tk.Canvas(root, borderwidth=0, background="#ffffff")
todo_container = tk.Frame(canvas, background="#ffffff")
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)

scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)
canvas.create_window((0,0), window=todo_container, anchor="nw")

def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

todo_container.bind("<Configure>", on_frame_configure)

# Enter-Taste bind
input_field.bind("<Return>", lambda event: submit())

root.mainloop()