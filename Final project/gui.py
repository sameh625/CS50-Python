# gui.py
import tkinter as tk
from tkinter import ttk, messagebox
import db

class Todo:
    def __init__(self, root):
        # Title and Size of the page
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("600x400")

        # Frame for title staff
        top_frame = tk.Frame(root)
        top_frame.pack(pady=5)

        # Title Label , Entry and Add button
        tk.Label(top_frame, text="Title:").pack(side="left", padx=5)
        self.title_entry = tk.Entry(top_frame, width= 40)
        self.title_entry.pack(side="left", padx=5)
        tk.Button(top_frame, text="Add Task",command=self.add_task, bg="gray",fg="white").pack(side="left")

        # Tasks Table
        self.tree = ttk.Treeview(root, columns=("ID", "Title", "Status"), show='headings')
        self.tree.heading("ID", text="ID")
        self.tree.heading("Title", text="Title")
        self.tree.heading("Status", text="Status")
        self.tree.pack(padx= 5,pady=10, fill="both", expand=True)

        # Frame for delete and mark done buttons
        bottom_frame = tk.Frame(root)
        bottom_frame.pack(fill = "x", pady = 5)

        # Delete button
        tk.Button(
            bottom_frame, text="Delete Task", command=self.delete_task,
            bg="red", fg="white"
        ).pack(side="right", padx=5, pady=5)

        # Mark done button
        tk.Button(
            bottom_frame, text="Mark as Done", command=self.mark_done,
            bg="green", fg="white"
        ).pack(side="left", padx=5, pady=5)

        self.load_tasks()
    
    
    def load_tasks(self):
        self.tree.tag_configure('pending', foreground='blue')
        self.tree.tag_configure('done', foreground='green')
        for item in self.tree.get_children():# this loop for the add task , delete or markdown to remove the repeated ones
            self.tree.delete(item)
        for task in db.get_tasks():
            status = task[2]
            self.tree.insert('','end', values = task, tags = (status,))
    

    def add_task(self):
        title = self.title_entry.get()
        if not title:
            messagebox.showwarning("Input Error", "Please enter a task title.")
            return
        db.add_task(title)
        self.title_entry.delete(0, tk.END)
        self.load_tasks()


    def delete_task(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Selection Error", "Select a task to delete.")
            return
        task_id = self.tree.item(selected[0])["values"][0]
        db.delete_task(task_id)
        self.load_tasks()


    def mark_done(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Selection Error", "Select a task to mark done.")
            return
        task_id = self.tree.item(selected[0])["values"][0]
        db.mark_done(task_id)
        self.load_tasks()
