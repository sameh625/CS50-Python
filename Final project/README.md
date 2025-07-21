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

## 🛠️ How It Works

- The GUI is built with Tkinter and separated into a `gui.py` module.
- MySQL handles all database operations in `db.py`.
- `project.py` serves as the app’s entry point.

**The `tasks` table should have the following structure:**

```sql
CREATE TABLE tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    status ENUM('pending', 'done') DEFAULT 'pending'
);
```

---

## 🧑‍💻 Folder Structure

```
.
├── project.py          # Entry point
├── gui.py              # GUI class using Tkinter
├── db.py               # MySQL functions
├── test_project.py     # Unit tests
└── README.md           # Project description
```

---

## 🚀 How to Run

Make sure you have:

- Python 3 installed
- MySQL server running locally
- Tkinter installed (usually included)
- `mysql-connector-python` installed (`pip install mysql-connector-python`)

Then run:

```bash
python project.py
```

---
## 🧪 Testing:

Testing is done using **pytest**. Unit tests are written for database operations:
- Add Task
- Mark Task as Done
- Delete Task

Run tests with:
```bash
pytest test_project.py
