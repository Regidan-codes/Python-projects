import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)


while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if "add" in user_action:
        todo = user_action[4:]

        todos = functions.get_todos("todos.txt")

        todos.append(todo + '\n')

        functions.write_todos("todos.txt", todos)

    elif "show" in user_action:

        todos = functions.get_todos("todos.txt")

        for index, items in enumerate(todos):
            items = items.strip('\n')
            row = f"{index + 1}-{items}"
            print(row)

    elif user_action.startswith('edit'):

        try:

            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos("todos.txt")

            new_todo = input("Enter a new todo:")
            todos[number] = new_todo + '\n'

            functions.write_todos("todos.txt", todos)

        except ValueError:
            print("Your command is not valid.")
            continue

    elif "complete" in user_action:

        try:

            number = int(user_action[9:])

            todos = functions.get_todos("todos.txt")

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos("todos.txt", todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)

        except IndexError:
            print("There is no item with that number. ")

    elif "exit" in user_action:
        break

    else:
        print("Command is not valid.")

print("Bye!")
