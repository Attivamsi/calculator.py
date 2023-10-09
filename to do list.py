import tkinter as tk
from tkinter import messagebox

class ToDoWindow:
    def __init__(self,root):
        self.root = root
        self.root.title("To-Do List App")
        
        self.tasks = []

        self.task_entry = tk.Entry(root, width=60)
        self.task_entry.pack(pady=10)
        
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()
        
        self.listbox = tk.Listbox(root, width=60)
        self.listbox.pack()
        
        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        self.remove_button.pack()
        
        self.root.mainloop()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.show_warning("Warning", "Task can't be empty!")

    def remove_task(self):
        selected_task_index = self.listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            self.listbox.delete(task_index)
            del self.tasks[task_index]

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoWindow(root)

