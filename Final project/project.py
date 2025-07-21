import tkinter as tk
from tkinter import ttk
from gui import Todo

def main():
    root = tk.Tk()
    Todo(root)
    root.mainloop()


if __name__ == "__main__":
    main()