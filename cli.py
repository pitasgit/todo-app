# from functions import get_todos, write_todos # folosim aceasta metoda daca dorim sa importam mai multe module
import functions  # folosim aceasta metoda ca sa determinam de unde am importat unde sunt definite exe get_todos
import time

now = time.strftime("%d %b %Y, %H:%M:%S")
print("It is", now)
while True:
    # get user input and strip space chars from it
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        to_do = user_action[4:]

        todos = functions.get_todos()

        todos.append(to_do + '\n')

        # file = open('todos.txt', 'r')
        # todos = file.readlines()
        # file.close() sau varianta mai simpla si recomandata
        # (pentru ca daca vom avea erori, fisierul tot se va inchide):

        # file = open('todos.txt', 'w')
        functions.write_todos(todos)
        # file.close()

    elif user_action.startswith("show"):

        todos = functions.get_todos()

        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            continue
    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            functions.write_todos(todos)
            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("There is not item with that number.")
            continue
    elif user_action.startswith('exit'):
        break
    else:
        print("Command is not valid")
    # case whatever:
    #     print("Hey, enter a known command")
print("Bye!")
