import requests
from typing import Optional

API_BASE_URL = "http://localhost:8000/api/v1"

def create_todo(title: str, description: Optional[str] = None, priority: str = "medium"):
    """Create a new todo item."""
    payload = {"title": title, "description": description, "priority": priority}
    response = requests.post(f"{API_BASE_URL}/todos", json=payload)
    return response.json()

def list_todos():
    """Get all todo items."""
    response = requests.get(f"{API_BASE_URL}/todos")
    return response.json()

def toggle_todo(todo_id: int):
    """Toggle the completion status of a todo."""
    # Simplified toggle for the agent
    response = requests.patch(f"{API_BASE_URL}/todos/{todo_id}", json={"status": "completed"})
    return response.json()

def delete_todo(todo_id: int):
    """Delete a todo item."""
    response = requests.delete(f"{API_BASE_URL}/todos/{todo_id}")
    return response.json()
