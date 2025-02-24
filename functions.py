FILEPATH = 'todos.txt'

def read_todos(filepath = FILEPATH):
    with open(filepath,'r') as file:
        todos = file.readlines()
    return todos


def write_todos(todo_list, filepath = FILEPATH):
    with open(filepath,'w') as file:
        file.writelines(todo_list)