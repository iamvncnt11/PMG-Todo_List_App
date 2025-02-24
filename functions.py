FILEPATH = 'todos.txt'

def read_todos():
    with open(FILEPATH,'r') as file:
        todos = file.read()
    return todos


def write_todos(todo_list):
    with open(FILEPATH,'w') as file:
        file.write(todo_list)