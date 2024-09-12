import sys
import sqlite3
import models
import display
import migrations

migrations.migrate()

db = sqlite3.connect('todo.sqlite')

command = 'help' if len(sys.argv) < 2 else sys.argv[1]
arguments = sys.argv[2:] if len(sys.argv) > 2 else []

if command == 'help':
    print("""
Syntax: python main.py <command> [command arguments]

help            Display help
list            List all todos
create <name>   Create a new todo
find <id>       Find a todo
complete <id>   Complete a todo
delete <id>     Delete a todo
""")
    exit()

# This gets the command function and display function by the command passed in
# the shell; executing it with any possible other arguments that were passed in
command_function = getattr(models.Todo, command)
display_function = getattr(display, command)

# Execute the command function with the arguments, then the display function
# with the results of the command function
results = command_function(arguments, db=db)
display_function(results)