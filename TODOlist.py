import tkinter as tk
from tkinter import messagebox, simpledialog

tasks = []


def update_listbox():
    listbox.delete(0, tk.END)
    for i, task in enumerate(tasks):
        status = "✅" if task["done"] else "❌"
        listbox.insert(tk.END, f"{i+1}. {task['task']}  [{status}]")


def add_task():
    task_text = simpledialog.askstring("Add Task", "Enter the task:")
    if task_text:
        tasks.append({"task": task_text, "done": False})
        update_listbox()


def mark_done():
    selection = listbox.curselection()
    if selection:
        index = selection[0]
        tasks[index]["done"] = True
        update_listbox()
    else:
        messagebox.showwarning("Warning", "Please select a task first!")


def delete_task():
    selection = listbox.curselection()
    if selection:
        index = selection[0]
        tasks.pop(index)
        update_listbox()
    else:
        messagebox.showwarning("Warning", "Please select a task to delete!")


# ----- Graphic connection -----
root = tk.Tk()
root.title("To-Do List")

# work list
listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)

# buttons
add_btn = tk.Button(root, text="➕ Add Task", cursor="hand2", command=add_task)
add_btn.pack()

done_btn = tk.Button(root, text="✅ Mark as Done", command=mark_done)
done_btn.pack()

delete_btn = tk.Button(root, text="🗑 Delete Task", command=delete_task)
delete_btn.pack()

exit_btn = tk.Button(root, text="🚪 Exit", command=root.quit)
exit_btn.pack()

# start
update_listbox()
root.mainloop()
