import db
import pytest

test_title = "pytest task"

def test_add_task():
    db.add_task(test_title)
    tasks = db.get_tasks()
    found = [t for t in tasks if t[1] == test_title and t[2] == "pending"]
    assert len(found) > 0 # it should be 1 cause we added a new task to it
    global test_task_id
    test_task_id = found[0][0]  # Save ID for later tests

def test_mark_done():
    db.mark_done(test_task_id)
    tasks = db.get_tasks()
    updated = [t for t in tasks if t[0] == test_task_id] # it should toggle the panding status to done
    assert updated and updated[0][2] == "done"

def test_delete_task():
    db.delete_task(test_task_id)
    tasks = db.get_tasks()
    deleted = [t for t in tasks if t[0] == test_task_id] # it should return nothing cause we deleted it
    assert len(deleted) == 0
