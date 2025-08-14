import tkinter as tk
from tkinter import messagebox
import os

# ---------- Functions ----------
def add_task():
    task = task_entry.get()
    if task != "":
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def delete_task():
    try:
        selected_task = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task)
        save_tasks()
    except:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

def complete_task():
    try:
        index = tasks_listbox.curselection()[0]
        task = tasks_listbox.get(index)
        if not task.startswith("✔ "):  # avoid marking twice
            tasks_listbox.delete(index)
            tasks_listbox.insert(index, "✔ " + task)
            save_tasks()
    except:
        messagebox.showwarning("Selection Error", "Please select a task to complete.")

def save_tasks():
    tasks = tasks_listbox.get(0, tasks_listbox.size())
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")

def load_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as f:
            for task in f.readlines():
                tasks_listbox.insert(tk.END, task.strip())

# ---------- GUI Setup ----------
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x450")
root.resizable(False, False)

# Entry field
task_entry = tk.Entry(root, width=35, font=("Arial", 14))
task_entry.pack(pady=10)

# Buttons
frame = tk.Frame(root)
frame.pack(pady=5)

add_btn = tk.Button(frame, text="Add Task", command=add_task)
add_btn.grid(row=0, column=0, padx=5)

delete_btn = tk.Button(frame, text="Delete Task", command=delete_task)
delete_btn.grid(row=0, column=1, padx=5)

complete_btn = tk.Button(frame, text="Complete Task", command=complete_task)
complete_btn.grid(row=0, column=2, padx=5)

# Listbox
tasks_listbox = tk.Listbox(root, width=40, height=15, font=("Arial", 12))
tasks_listbox.pack(pady=10)

# Load saved tasks
load_tasks()

root.mainloop()
