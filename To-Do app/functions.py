def get_todos(filepath):
    """Read a text-file and return  the list"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
        return todos_local


def write_todos(filepath, todos_arg):
    """Write a to-do items to text file"""
    with open(filepath, todos_arg) as file:
        file.writelines(todos_arg)
