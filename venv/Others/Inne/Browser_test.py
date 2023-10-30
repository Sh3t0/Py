

import PySimpleGUI as sg

# Define the layout
layout = [
    [
        sg.Text("Wybierz plik"),
        sg.Input(size=(25, 1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Text("Wybrana ścieżka:"),
        sg.Text("", size=(25, 1), key="-PATH-"),
    ],
    [sg.Button("Exit")],
]

# Create the window
window = sg.Window("Folder Selection", layout, finalize=True)

# Event loop
while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, "Exit"):
        break
    elif event == "-FOLDER-":
        folder_path = values["-FOLDER-"]
        window["-PATH-"].update(folder_path)

# Close the window
print(values["-FOLDER-"])
window.close()
