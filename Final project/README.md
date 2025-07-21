# To-Do List Manager with Tkinter and MySQL

#### Video Demo: [<YOUR VIDEO URL HERE>]
#### Author: Sameh
#### GitHub Username: sameh625
#### edX Username: SM_2502_O1D7
#### Location: [Menofia, Egypt]
#### Date: [21/7/2025]

---

## Description:

This is a simple and functional **To-Do List Desktop App** built using:

- 🐍 **Python 3**
- 🖼️ **Tkinter** (for the GUI)
- 🗄️ **MySQL** (for task storage)

The project was created for **CS50P**, and demonstrates the use of GUI programming, persistent database storage, and user interaction in a clean desktop application.

---

## 💡 Features:

- **Add Task**: Create a new task with a title.
- **View Tasks**: Automatically loads tasks on launch or update.
- **Mark as Done**: Update task status visually and in the database.
- **Delete Task**: Remove tasks completely.
- **Color Coding**: 
  - Pending tasks appear in **blue**.
  - Completed (done) tasks appear in **green**.

---

## 🧪 Testing:

Testing is done using **pytest**. Unit tests are written for database operations:
- Add Task
- Mark Task as Done
- Delete Task

Run tests with:
```bash
pytest test_project.py
