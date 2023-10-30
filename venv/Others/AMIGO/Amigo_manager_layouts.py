from Amigo_Menager_defs import *
import os
import subprocess
import PySimpleGUI as sg
import ctypes
import sys
import time
import re
import psutil
import threading
import functools
import xml.etree.ElementTree as ET


#parsowanie XML
def load_xml_data_to_inputs(window, xml_file_path=None):
    global connection_string

    if xml_file_path is None:
        sg.popup_error("Nie wybrano pliku serviceconfiguration.xml.")
        return

    try:
        tree = ET.parse(xml_file_path)
        root = tree.getroot()

        connection_string_element = root.find("ConnectionString")
        if connection_string_element is not None:
            connection_string = connection_string_element.text

            # Podziel ConnectionString na sekcje
            sections = connection_string.split(";")
            print(sections)
            element_values = {}
            for section in sections:
                key, val = section.split("=")
                key = key.strip()
                val = val.strip()
                element_values[key] = val

            for key in key_elements:
                window[f"-{key.replace(' ', '_')}-"].update(value=element_values[key])

    except ET.ParseError:
        sg.popup_error("Błąd podczas parsowania pliku XML.")


#__________________________________________________________________________________________________________________________________________
# GUI layout
exit_button_style = {
    'size': (7, 2),  # Rozmiar przycisku
    'font': ('Arial', 9),  # Rozmiar i rodzaj czcionki
    'button_color': ('white', 'red'),  # Kolor tła i kolor czcionki
    'border_width': 2,  # Grubość obramowania
    'pad': (5, 5),  # Wewnętrzne wypełnienie przycisku
    'key': 'exit_style',  # Klucz przycisku
    #'justification': 'right'
}

sg.theme('DarkGrey11')
layout_de_installing = [
    [
        sg.Text("Choose location:"),
        sg.Input(size=(30, 1), enable_events=True, key="-FOLDER-", tooltip='Choose main amigo path'),
        sg.FolderBrowse(),
        sg.Submit("Submit")
    ],
    [
        sg.Text("Selected path:"),
        sg.Text("", size=(30, 1), key="-PATH-"),
    ],
    [
        sg.Button("Delete all AMIGO Services")
    ],
    [
        sg.Output(size=(60, 35), key="-OUTPUT-")
    ],

]


service_labels = []
for service_name in get_amigo_services():
    service_labels.append([sg.Text(f"{service_name} - Status: Unknown", key=service_name, font=("Helvetica", 10), pad=(10, 0))])
layout_services = [
    [sg.Listbox(values=get_amigo_services(), size=(56, 10), key='-SERVICE_LIST-')],
    [sg.Button('Start Service'), sg.Button('Start All Services'),  sg.Button('Restart Service')],
    [sg.Button('Stop Service'), sg.Button('Stop All Services'), sg.Button('Restart All Services')],
    *service_labels,
    [sg.Output(size=(60, 20))]
]


layout_ServiceConfig = [
    [sg.Text("Wybierz katalog:"), sg.InputText(key="-ServiceConfig_Path-", enable_events=True), sg.FolderBrowse()],
   # [sg.Text("Wybierz środowisko:"), sg.InputText(key="-ServiceConfig_Path-", enable_events=True), sg.FolderBrowse()],
]

key_elements = ["XpoProvider", "data source", "user id", "password", "initial catalog", "Persist Security Info"]

for key in key_elements:
    layout_ServiceConfig.append([sg.Text(f"{key}: "), sg.Input(key=f"-{key.replace(' ', '_')}-", default_text='')])

layout_ServiceConfig.extend([
    [sg.Output(size=(80, 10), key="-Service_Configuration-")],
    [sg.Button("Save Changes")]
])




layout_logs = [
    [
        sg.Text("Select service folder:"),
        sg.Input(size=(25, 1), enable_events=True, key="-LOG_FOLDER-"),
        sg.FolderBrowse()
    ],
    [
        sg.Text("Selected path:"),
        sg.Text("", size=(25, 1), key="-LOGS_PATH-"),
    ],
    [
        sg.Button('Delete All Logs'),
        sg.Button('Archive All Logs'),
        sg.Button('Delete Latest Log'),
        sg.Button('Archive Latest Log'),
    ],
    [
        sg.Output(size=(60, 18), key="-PROGRESS_OUTPUT-"),
    ],
]


layout = [
    [sg.TabGroup([
        [sg.Tab('Instalation', layout_de_installing, key='-TAB1-')],
        [sg.Tab('Services', layout_services, key='-TAB2-')],
        [sg.Tab('Service Configuration', layout_ServiceConfig, key='-TAB3-')],
        [sg.Tab('Logs', layout_logs, key='-TAB4-')]

    ])],
    [sg.Button("Exit")]
]

icon_path = r'.\build\amigo.ico'  # Zmień na ścieżkę do twojego pliku ikony
sg.set_options(icon=icon_path)
run_as_admin()
#window.set_icon(icon_path)
# Create the window
window = sg.Window("Aminger", layout, finalize=True)

# Uruchomienie wątku aktualizacji statusu usług
update_thread = threading.Thread(target=update_service_status_thread, args=(window,))
update_thread.daemon = True
update_thread.start()
# Uruchomienie wątku aktualizacji statusu usług


# Przypisanie początkowej wartości ConnectionString
connection_string = ""
# DLA SERVICECONFIGURATION
# Event loop
while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, "Exit"):
        break
    elif event == "-TAB1":
        window[current_tab].update(visible=False)
        current_tab = "-TAB1-"
        window[current_tab].update(visible=True)
    elif event == "-TAB2":
        window[current_tab].update(visible=False)
        current_tab = "-TAB2-"
        window[current_tab].update(visible=True)
    elif event == "-TAB3":
        window[current_tab].update(visible=False)
        current_tab = "-TAB3-"
        window[current_tab].update(visible=True)
    elif event == "-TAB4":
        window[current_tab].update(visible=False)
        current_tab = "-TAB4-"
        window[current_tab].update(visible=True)


    ######## TAB 1 ########
    elif event == "-FOLDER-":
        folder_path = values["-FOLDER-"]
        window["-PATH-"].update(folder_path)
    elif event == "Submit":
        folder_path = values["-FOLDER-"]
        if not folder_path:
            sg.popup("Choose main amigo path")
        elif folder_path:
            window["-PATH-"].update(folder_path)
            install_amigo_services(folder_path)
    elif event == "Delete all AMIGO Services":
       if __name__ == "__main__":
            print("Lista usług:")
            print("\nUsuwanie usług rozpoczynających się od 'amigo':")
            uninstall_amigo_services()

    ######## TAB 2 ########
    elif event == 'Start Service':
        selected_service = values['-SERVICE_LIST-']
        if not selected_service:
            sg.popup("Please Select Service")
        elif selected_service:
            output_elem = window['-OUTPUT-']  # Pobierz element okna Output
            start_service(selected_service[0])
    elif event == 'Stop Service':
        selected_service = values['-SERVICE_LIST-']
        if not selected_service:
            sg.popup("Please Select Service")
        else:
            output_elem = window['-OUTPUT-']  # Pobierz element okna Output
            stop_service(selected_service[0])
    elif event == 'Restart Service':
        selected_service = values['-SERVICE_LIST-']
        if not selected_service:
            sg.popup("Please Select Service")
        else:
            output_elem = window['-OUTPUT-']  # Pobierz element okna Output
            restart_service(selected_service[0])
    elif event == 'Start All Services':
        start_all_services()
    elif event == 'Stop All Services':
        stop_all_services()
    elif event == 'Restart All Services':
        restart_all_services()
    elif event == 'Delete All Logs':
        delete_all_logs(log_folder_path)
        window["-LOG_LIST-"].update(values=[])


    ######## TAB 3 ########
    elif event == "-ServiceConfig_Path-":
        folder_path = values["-ServiceConfig_Path-"]
        xml_file_path = find_serviceconfiguration_file(folder_path)
        load_xml_data_to_inputs(window, xml_file_path)
    elif event == "Save Changes":
        # Aktualizuj zawartość ConnectionString
        connection_string = f"XpoProvider={values['-XpoProvider-']};data source={values['-data_source-']};user id={values['-user_id-']};password={values['-password-']};initial catalog={values['-initial_catalog-']};Persist Security Info={values['-Persist_Security_Info-']}"
        window["-Service_Configuration-"].update(connection_string)
        # Zapisz zmiany w pliku serviceconfig
        edit_service_config_file(window, values, folder_path)
        sg.popup("Zmiany zostały zapisane pomyślnie!", title="Zapisz zmiany")


    ######## TAB 4 ########
    elif event == 'Delete All Logs':
        log_folder_path = values["-LOG_FOLDER-"]
        if not log_folder_path:
            sg.popup("Choose main amigo path")
        elif log_folder_path:
            delete_all_logs(log_folder_path, history, unique_messages)
    elif event == 'Delete Latest Log':
        log_folder_path = values["-LOG_FOLDER-"]
        if not log_folder_path:
            sg.popup("Choose main amigo path")
        elif log_folder_path:
            delete_latest_log(log_folder_path, history, unique_messages)
    elif event == 'Archive All Logs':
        log_folder_path = values["-LOG_FOLDER-"]
        if not log_folder_path:
            sg.popup("Choose main amigo path")
        elif log_folder_path:
            archive_all_logs(log_folder_path, history, unique_messages)
    elif event == 'Archive Latest Log':
        log_folder_path = values["-LOG_FOLDER-"]
        if not log_folder_path:
            sg.popup("Choose main amigo path")
        elif log_folder_path:
            archive_latest_log(log_folder_path, history, unique_messages)
    elif event == 'Archive All Logs':
        archive_all_logs(log_folder_path, archive_folder_path)
        window["-LOG_LIST-"].update(values=[])
    elif event == 'Delete Latest Log':
        delete_latest_log(log_folder_path)
        window["-LOG_LIST-"].update(values=get_log_files(log_folder_path))
    elif event == 'Archive Latest Log':
        archive_latest_log(log_folder_path, archive_folder_path)
        window["-LOG_LIST-"].update(values=get_log_files(log_folder_path))




# Close the window
window.close()
