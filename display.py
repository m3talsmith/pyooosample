def list(todos):
    print_header()
    for todo in todos:
        print_todo(todo)

def create(todo):
    print('[*Todo Created*]')
    print_header()
    print_todo(todo)

def find(todo):
    print('[*Todo Found*]')
    print_header()
    print_todo(todo)

def complete(todo):
    print('[*Todo Completed*]')
    print_header()
    print_todo(todo)

def delete(todo):
    print('[*Todo Deleted*]')
    print_header()
    print_todo(todo)

def print_header():
    print('[Todos]')
    print('| ID | Name | Completed |')

def print_todo(todo):
    complete = False if (todo.complete == None or todo.complete == 0) else True
    print(f'| {todo.id} | {todo.name} | {complete} |')