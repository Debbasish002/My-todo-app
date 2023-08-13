def get_todos(filepath='todos.txt'):           #use filepath info here, and in all get_todos(), use this default argument.
    """" Read a text file and return the list of
    to-do items"""

    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath = 'todos.txt'):
    """"Write todo items list in the text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

