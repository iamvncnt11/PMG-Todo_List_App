import functions
import FreeSimpleGUI as sg

label = sg.Text('Type in a to-do')
input_box = sg.InputText(tooltip = 'Enter todo', key = 'todo')
add_button = sg.Button('Add')

window = sg.Window('My To-Do App',
                   layout = [[label],
                             [input_box, add_button]],
                   font = ('Helvetica',20))

event, values = window.Read()
print('Hello')
window.Close()