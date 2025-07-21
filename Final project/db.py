import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="todo_app",
        port=3306
    )

def add_task(title):
    con = get_connection()
    cursor = con.cursor()
    cursor.execute("INSERT INTO `tasks` (`title`) VALUES (%s)",(title,))
    con.commit()
    cursor.close()

def get_tasks():
    con = get_connection()
    cursor = con.cursor()
    cursor.execute("SELECT id, title, status FROM `tasks`")
    tasks = cursor.fetchall()
    cursor.close()
    con.close()
    return tasks  

def delete_task(task_id):
    con = get_connection()
    cursor = con.cursor()
    cursor.execute("DELETE FROM `tasks` WHERE id = %s", (task_id,))
    con.commit()
    cursor.close()

def mark_done(task_id):
    con = get_connection()
    cursor = con.cursor()
    cursor.execute("UPDATE `tasks` SET status = 'done' WHERE id = %s", (task_id,))
    con.commit()
    cursor.close()
