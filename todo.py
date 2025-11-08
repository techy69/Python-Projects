"""
TODO List Manager - A simple command-line TODO list application
"""

import sys
import json
import os
from rich.console import Console
from rich.table import Table
from rich import box

console = Console()
TODO_FILE = 'todos.json'

def load_todos():
    """Load todos from JSON file"""
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as f:
            return json.load(f)
    return []

def save_todos(todos):
    """Save todos to JSON file"""
    with open(TODO_FILE, 'w') as f:
        json.dump(todos, f, indent=2)

def add_task(task_description):
    """Add a new task to the TODO list"""
    todos = load_todos()
    task = {
        'id': len(todos) + 1,
        'task': task_description,
        'done': False
    }
    todos.append(task)
    save_todos(todos)
    console.print(f"[green]✓[/green] Added: '{task_description}'", style="bold")

def list_tasks():
    """Display all tasks in a formatted table"""
    todos = load_todos()
    
    if not todos:
        console.print("[yellow]No tasks found. Add some tasks to get started![/yellow]")
        return
    
    table = Table(title="📝 TODO List", box=box.ROUNDED)
    table.add_column("ID", justify="center", style="cyan")
    table.add_column("Task", style="white")
    table.add_column("Status", justify="center")
    
    for todo in todos:
        status = "[green]✓ Done[/green]" if todo['done'] else "[yellow]⏳ Pending[/yellow]"
        table.add_row(str(todo['id']), todo['task'], status)
    
    console.print(table)

def mark_done(task_id):
    """Mark a task as done"""
    todos = load_todos()
    task_id = int(task_id)
    
    for todo in todos:
        if todo['id'] == task_id:
            todo['done'] = True
            save_todos(todos)
            console.print(f"[green]✓[/green] Task {task_id} marked as done!", style="bold")
            return
    
    console.print(f"[red]✗[/red] Task {task_id} not found!", style="bold")

def delete_task(task_id):
    """Delete a task from the list"""
    todos = load_todos()
    task_id = int(task_id)
    
    todos = [todo for todo in todos if todo['id'] != task_id]
    
    # Reassign IDs
    for idx, todo in enumerate(todos, 1):
        todo['id'] = idx
    
    save_todos(todos)
    console.print(f"[green]✓[/green] Task {task_id} deleted!", style="bold")

def print_usage():
    """Print usage instructions"""
    console.print("\n[bold cyan]TODO List Manager[/bold cyan]\n")
    console.print("[yellow]Usage:[/yellow]")
    console.print("  python todo.py add <task>     - Add a new task")
    console.print("  python todo.py list           - List all tasks")
    console.print("  python todo.py done <id>      - Mark task as done")
    console.print("  python todo.py delete <id>    - Delete a task\n")

def main():
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)
    
    command = sys.argv[1].lower()
    
    if command == 'add':
        if len(sys.argv) < 3:
            console.print("[red]Error: Please provide a task description[/red]")
            sys.exit(1)
        task = ' '.join(sys.argv[2:])
        add_task(task)
    
    elif command == 'list':
        list_tasks()
    
    elif command == 'done':
        if len(sys.argv) < 3:
            console.print("[red]Error: Please provide a task ID[/red]")
            sys.exit(1)
        mark_done(sys.argv[2])
    
    elif command == 'delete':
        if len(sys.argv) < 3:
            console.print("[red]Error: Please provide a task ID[/red]")
            sys.exit(1)
        delete_task(sys.argv[2])
    
    else:
        console.print(f"[red]Error: Unknown command '{command}'[/red]")
        print_usage()
        sys.exit(1)

if __name__ == "__main__":
    main()
