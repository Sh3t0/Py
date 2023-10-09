import PySimpleGUI as sg
import os

sg.theme('DarkGrey9')

# Inicjalizacja zmiennych
folder_path = ""
selected_note_index = None

def update_notes_list():
    global folder_path
    if folder_path and os.path.exists(folder_path):
        text_files = [f for f in os.listdir(folder_path) if f.endswith(".txt")]
        window["NOTES LIST"].update(values=text_files)

def update_note_preview(selected_note):
    global folder_path
    if folder_path:
        note_path = os.path.join(folder_path, selected_note)
        try:
            with open(note_path, "r") as note_file:
                note_content = note_file.read().replace("\r\n", "\n")  # Usuń znaki \r
                window["NOTE PREVIEW"].update(note_content)
        except FileNotFoundError:
            window["NOTE PREVIEW"].update("Selected note does not exist.")

def update_contents_list(folder_path):
    contents = []
    if os.path.exists(folder_path):
        # Wylistuj zawartość folderu (katalogi i pliki)
        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item)
            if os.path.isdir(item_path):
                item += '/'  # Oznacz katalogi znakiem '/'
            contents.append(item)
    return contents



layout = [
    [
        sg.Text("Choose location:"),
        sg.Input(size=(25, 1), enable_events=True, key="FOLDER"),
        sg.FolderBrowse(),
        sg.Submit("Submit"),
        sg.Text('', size=(50, 1)),
        sg.Button("Exit")
    ],
    [
        sg.Button('Delete Note'),
        sg.Button('Rename Note'),
        sg.Button('Edit'),
    ],
    [

    ],
    [

        sg.Listbox(values=[], enable_events=True, size=(60, 20), key="NOTES LIST"),
        sg.VSeparator(),
        sg.Multiline("", size=(55, 20), key="NOTE PREVIEW", disabled=True)
    ],
]

window = sg.Window("File Browser", layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == "Exit":
        break
    elif event == "Submit":
        folder_path = values["FOLDER"]
        update_notes_list()
        window["CONTENTS"].update(values=update_contents_list(folder_path))
    elif event == "NOTES LIST":
        selected_note_index = values["NOTES LIST"][0]
        update_note_preview(selected_note_index)
    elif event == "Edit":
        if folder_path:
            sg.popup_get_text("Enter note name:", default_text="New Note", title="Add Note")
            update_notes_list()
    elif event == "Delete Note" and selected_note_index:
        note_path = os.path.join(folder_path, selected_note_index)
        os.remove(note_path)
        selected_note_index = None
        update_notes_list()
        window["NOTE PREVIEW"].update("")
    elif event == "Rename Note" and selected_note_index:
        new_name = sg.popup_get_text("Enter new name for the note:", default_text=selected_note_index, title="Rename Note")
        if new_name:
            new_note_path = os.path.join(folder_path, new_name)
            note_path = os.path.join(folder_path, selected_note_index)
            os.rename(note_path, new_note_path)
            selected_note_index = new_name
            update_notes_list()
            update_note_preview(selected_note_index)

window.close()
