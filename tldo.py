import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def delete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
    except:
        messagebox.showwarning("Warning", "You must select a task.")

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        for task in tasks:
            listbox_tasks.insert(tk.END, task.strip())
    except FileNotFoundError:
        open("tasks.txt", "w").close()

def save_tasks():
    tasks = listbox_tasks.get(0, listbox_tasks.size())
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")
    messagebox.showinfo("Info", "Tasks saved successfully.")

window = tk.Tk()
window.title("To-Do List")

label_heading = tk.Label(window, text="To-Do List", font=("Arial", 24))
label_heading.pack()

frame_tasks = tk.Frame(window)
frame_tasks.pack()

listbox_tasks = tk.Listbox(frame_tasks, height=10, width=50)
listbox_tasks.pack(side=tk.LEFT)

scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tk.Entry(window, width=50)
entry_task.pack()

button_add_task = tk.Button(window, text="Add task", width=48, command=add_task)
button_add_task.pack()

button_delete_task = tk.Button(window, text="Delete task", width=48, command=delete_task)
button_delete_task.pack()

menu_bar = tk.Menu(window)
window.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Load tasks", command=load_tasks)
file_menu.add_command(label="Save tasks", command=save_tasks)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)

load_tasks()

window.mainloop()
