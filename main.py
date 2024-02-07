import tkinter as tk
from tkinter import messagebox

def add_task(entry, listbox):
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task(listbox):
    try:
        index = listbox.curselection()
        listbox.delete(index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def main():
    root = tk.Tk()
    root.title("To-Do List")

    # Create and pack the entry and button widgets
    entry = tk.Entry(root, font=("Helvetica", 14))
    entry.pack(pady=10)

    add_button = tk.Button(root, text="Add Task", command=lambda: add_task(entry, listbox))
    add_button.pack(pady=5)

    delete_button = tk.Button(root, text="Delete Task", command=lambda: delete_task(listbox))
    delete_button.pack(pady=5)

    # Create and pack the listbox widget
    listbox = tk.Listbox(root, font=("Helvetica", 12), width=50)
    listbox.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()