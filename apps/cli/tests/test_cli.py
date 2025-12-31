import pytest
from ..src.cli import TodoApp

def test_add_task():
    app = TodoApp()
    app.add_task("Test Title", "Test Desc")
    assert len(app.todos) == 1
    assert app.todos[0].title == "Test Title"

def test_toggle_task():
    app = TodoApp()
    app.add_task("Test")
    app.toggle_task(1)
    assert app.todos[0].is_completed is True
    app.toggle_task(1)
    assert app.todos[0].is_completed is False

def test_delete_task():
    app = TodoApp()
    app.add_task("Test")
    app.delete_task(1)
    assert len(app.todos) == 0
