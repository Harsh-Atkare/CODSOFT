import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.tasks = []

        self.frame = tk.Frame(self.root)
        self.frame.pack()

        self.task_entry = tk.Entry(self.frame, width=50)
        self.task_entry.pack(side=tk.LEFT)

        self.add_button = tk.Button(self.frame, text="Add Task", command=self.add_task)
        self.add_button.pack(side=tk.LEFT)

        self.tasks_listbox = tk.Listbox(self.root, width=50, height=10)
        self.tasks_listbox.pack()

        self.complete_button = tk.Button(self.root, text="Complete Task", command=self.complete_task)
        self.complete_button.pack()

        self.delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({'task': task, 'completed': False})
            self.update_tasks_listbox()
            self.task_entry.delete(0, tk.END)

    def complete_task(self):
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            self.tasks[selected_task_index[0]]['completed'] = True
            self.update_tasks_listbox()

    def delete_task(self):
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            del self.tasks[selected_task_index[0]]
            self.update_tasks_listbox()

    def update_tasks_listbox(self):
        self.tasks_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "Done" if task['completed'] else "Pending"
            self.tasks_listbox.insert(tk.END, f"{task['task']} [{status}]")

def main():
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
