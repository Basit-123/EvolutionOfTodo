import sys
from .cli import TodoApp, console

def print_help():
    console.print("\n[bold]Available Commands:[/bold]")
    console.print("  add <title> [description] - Add a new task")
    console.print("  list                      - Show all tasks")
    console.print("  done <id>                 - Toggle completion status")
    console.print("  delete <id>               - Remove a task")
    console.print("  update <id> <title> [desc]- Update task details")
    console.print("  help                      - Show this menu")
    console.print("  exit                      - Close application\n")

def main():
    app = TodoApp()
    console.print("[bold green]Welcome to the Evolution of Todo (Phase I)[/bold green]")
    print_help()

    while True:
        try:
            cmd_input = input(">> ").strip().split()
            if not cmd_input:
                continue

            command = cmd_input[0].lower()
            args = cmd_input[1:]

            if command == "exit":
                break
            elif command == "help":
                print_help()
            elif command == "add":
                if len(args) < 1:
                    console.print("[red]Usage: add <title> [description][/red]")
                else:
                    title = args[0]
                    desc = " ".join(args[1:]) if len(args) > 1 else ""
                    app.add_task(title, desc)
            elif command == "list":
                app.list_tasks()
            elif command == "done":
                if len(args) < 1:
                    console.print("[red]Usage: done <id>[/red]")
                else:
                    app.toggle_task(int(args[0]))
            elif command == "delete":
                if len(args) < 1:
                    console.print("[red]Usage: delete <id>[/red]")
                else:
                    app.delete_task(int(args[0]))
            elif command == "update":
                if len(args) < 2:
                    console.print("[red]Usage: update <id> <title> [desc][/red]")
                else:
                    todo_id = int(args[0])
                    title = args[1]
                    desc = " ".join(args[2:]) if len(args) > 2 else None
                    app.update_task(todo_id, title, desc)
            else:
                console.print(f"[red]Unknown command: {command}[/red]")
        except ValueError:
            console.print("[red]Error: Invalid ID format. Must be an integer.[/red]")
        except KeyboardInterrupt:
            break
        except Exception as e:
            console.print(f"[red]An error occurred: {e}[/red]")

if __name__ == "__main__":
    main()
