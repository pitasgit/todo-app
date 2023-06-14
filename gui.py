import functions
import PySimpleGUI as sg

# window = PySimpleGUI.Window('My To-Do App', Layout="")
# window.read()
# window.close()

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

window = sg.Window('My To-Do App', layout=[[label], [input_box, add_button]])
window.read()
window.close()