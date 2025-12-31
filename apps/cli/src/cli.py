import argparse
from typing import List
from rich.console import Console
from rich.table import Table
from .models import Todo

console = Console()

class TodoApp:
    def __init__(self):
        self.todos: List[Todo] = []
        self.next_id = 1

    def add_task(self, title: str, description: str = ""):
        todo = Todo(id=self.next_id, title=title, description=description)
        self.todos.append(todo)
        self.next_id += 1
        console.print(f"[green]Added task:[/green] {title}")

    def list_tasks(self):
        if not self.todos:
            console.print("[yellow]No tasks found.[/yellow]")
            return

        table = Table(title="Todo List")
        table.add_column("ID", justify="right", style="cyan")
        table.add_column("Title", style="magenta")
        table.add_column("Description", style="white")
        table.add_column("Status", justify="center")

        for todo in self.todos:
            status = "[green]Done[/green]" if todo.is_completed else "[red]Pending[/red]"
            table.add_row(str(todo.id), todo.title, todo.description, status)

        console.print(table)

    def delete_task(self, todo_id: int):
        self.todos = [t for t in self.todos if t.id != todo_id]
        console.print(f"[red]Deleted task ID:[/red] {todo_id}")

    def toggle_task(self, todo_id: int):
        for todo in self.todos:
            if todo.id == todo_id:
                todo.toggle()
                status = "completed" if todo.is_completed else "pending"
                console.print(f"[blue]Task {todo_id} is now {status}.[/blue]")
                return
        console.print(f"[bold red]Task {todo_id} not found.[/bold red]")

    def update_task(self, todo_id: int, title: str = None, description: str = None):
        for todo in self.todos:
            if todo.id == todo_id:
                if title: todo.title = title
                if description: todo.description = description
                console.print(f"[blue]Updated task {todo_id}.[/blue]")
                return
        console.print(f"[bold red]Task {todo_id} not found.[/bold red]")
