import PySimpleGUI as sg
import os
import xml.etree.ElementTree as ET

def find_serviceconfiguration_file(directory):
    for filename in os.listdir(directory):
        if filename.lower() == 'serviceconfiguration.xml':
            return os.path.join(directory, filename)
    return None

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
                if key in element_values:
                    window[f"-{key.replace(' ', '_')}-"].update(value=element_values[key])
                else:
                    window[f"-{key.replace(' ', '_')}-"].update(value='')
    except ET.ParseError:
        sg.popup_error("Błąd podczas parsowania pliku XML.")

def edit_service_config_file(window, values, folder_path):
    for root_folder, _, files in os.walk(folder_path):
        for file_name in files:
            if file_name.lower() == "serviceconfiguration.xml":
                file_path = os.path.join(root_folder, file_name)
                try:
                    tree = ET.parse(file_path)
                    root = tree.getroot()
                    key_elements = ["XpoProvider", "data source", "user id", "password", "initial catalog"]
                    changes_made = False  # Flaga informująca o zmianach

                    # Tworzymy zmienną elements i łączymy w niej wartości na podstawie values
                    connection_elements = []
                    for key in key_elements:
                        input_key = f"-{key.replace(' ', '_')}-"
                        new_value = values[input_key]
                        if new_value:
                            connection_elements.append(f"{key}={new_value}")

                    # Sprawdzamy, czy sekcja "ConnectionString" istnieje
                    connection_string_element = root.find("ConnectionString")
                    if connection_string_element is not None:
                        connection_string = connection_string_element.text
                        sections = connection_string.split(";")
                        for section in sections:
                            key, val = section.split("=")
                            if key.strip() == "Persist Security Info":
                                connection_elements.append(f"{key}={values['-Persist_Security_Info-']}")

                    # Łączymy te wartości w jedną sekcję ConnectionString
                    connection_string = ";".join(connection_elements)

                    # Znajdujemy sekcję "ConnectionString" i aktualizujemy jej tekst
                    connection_string_element = root.find("ConnectionString")
                    if connection_string_element is not None:
                        connection_string_element.text = connection_string
                        changes_made = True

                    if changes_made:
                        tree.write(file_path)
                        print("\nZapisano zmiany w pliku.")
                    else:
                        print("\nNie dokonano żadnych zmian w pliku.")

                except ET.ParseError:
                    sg.popup_error(f"Error parsing XML file: {file_path}")

layout = [
    [sg.Text("Wybierz katalog:"), sg.InputText(key="-ServiceConfig_Path-", enable_events=True), sg.FolderBrowse()],
]

key_elements = ["XpoProvider", "data source", "user id", "password", "initial catalog", "Persist Security Info"]

for key in key_elements:
    layout.append([sg.Text(f"{key}: "), sg.Input(key=f"-{key.replace(' ', '_')}-", default_text='')])

layout.extend([
    [sg.Output(size=(80, 10), key="-Service_Configuration-")],
    [sg.Button("Exit"), sg.Button("Save Changes")]
])

window = sg.Window("XML Parser", layout)

# Przypisanie początkowej wartości ConnectionString
connection_string = ""

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == "Exit":
        break
    elif event == "-ServiceConfig_Path-":
        folder_path = values["-ServiceConfig_Path-"]
        xml_file_path = find_serviceconfiguration_file(folder_path)
        load_xml_data_to_inputs(window, xml_file_path)
    elif event == "Save Changes":
        # Aktualizuj zawartość ConnectionString
        connection_string = f"XpoProvider={values['-XpoProvider-']};data source={values['-data_source-']};user id={values['-user_id-']};password={values['-password-']};initial catalog={values['-initial_catalog-']};Persist Security Info={values['-Persist_Security_Info-']} "
        window["-Service_Configuration-"].update(connection_string)
        # Zapisz zmiany w pliku serviceconfig
        edit_service_config_file(window, values, folder_path)
        sg.popup("Zmiany zostały zapisane pomyślnie!", title="Zapisz zmiany")

window.close()
