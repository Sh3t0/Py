import PySimpleGUI as sg
import os.path

file_list_column = [
    [
    sg.Text ("Image Folder"),
    sg.In(size=(25,1),enable_events=True, key="-FOLDER-"),
    sg.FolderBrowse(),
     ],

    [
        sg.Listbox(values=[],enable_events=True, size=(40,20), key="-FILE LIST-" )
    ],
]

image_viewer_column = [
    [sg.Text("Choose an image from left side:")],
    [sg.Text(size=(40,1), key="-TOUT-")],
    [sg.Image(key="-IMAGE-")],
]

sz=(10,20)
col1=[[sg.Text('Column1', background_color='red', size=sz)]]
col2=[[sg.Text('Column2', background_color='green', size=sz)]]
#full layout - elements locations
layout = [
    [sg.Column(file_list_column),
    sg.VSeparator(),
    sg.Column(image_viewer_column),
    ],
]

window = sg.Window("Image Viewer", layout)

#event loop
while True:
    event, values = window.read()
    if  event == sg.WIN_CLOSED:
        break
    if event == "-FOLDER-":
        folder = values["-FOLDER-"]
        try:
            file_list = os.listdir(folder)
        except:
            file_list = []

        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder,f))
            and f.lower().endswith((".png,",".gif"))
        ]

        window["-FILE LIST-"].update(fnames)
    elif event == "-FILE LIST-":
        try:
            filename = os.path.join(
                value["-FOLDER-"], values["-FILE LIST-"][0]
            )
            window["-TOUT-"].update(filename)
            window["-IMAGE-"].update(filename=filename)
        except:
            pass
window.close
