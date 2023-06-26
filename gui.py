import functions
import PySimpleGUI as sg

# window = PySimpleGUI.Window('My To-Do App', Layout="")
# window.read()
# window.close()

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo") # am pus key=
                                                            # pentru a fi cheia din dictionar pentru ceea ce am adaugat
add_button = sg.Button("Add")

window = sg.Window('My To-Do App',
                   layout=[[label], [input_box], [add_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo= values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()
