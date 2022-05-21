import PySimpleGUI as sg

sg.theme("LightGray")
layout = [
    []
]
window = sg.Window("Текстовый редактор", layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

window.close()