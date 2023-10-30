import os
import subprocess
import PySimpleGUI as sg
import ctypes
import sys
import time
import re
import psutil
#__________________________________________________________________________________________________________________________________________
# Funkcja do sprawdzania i otwierania konsoli jako administrator
def run_as_admin():
    if ctypes.windll.shell32.IsUserAnAdmin() == 0:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 0)
        sys.exit()

# Lista of ALL Services
def list_services():
    services = psutil.win_service_iter()
    for service in services:
        service_name = service.name()
        service_status = service.status()
        print(f"Usługa: {service_name}, Status: {service_status}")


# Funkcja usuwająca uslugi amigo
def uninstall_amigo_services():
    # Pobierz iterator usług systemowych z biblioteki psutil
    services = psutil.win_service_iter()

    # Iteruj przez dostępne usługi systemowe
    for service in services:
        # Pobierz nazwę aktualnie rozważanej usługi
        service_name = service.name()

        # Sprawdź, czy nazwa usługi pasuje do wzorca, który zaczyna się od "amigo" lub "Amigo"
        if re.match(r'(?i)^amigo', service_name):
            try:
                # Jeśli pasuje, próbuj usunąć usługę za pomocą narzędzia "sc" (Service Control Manager)
                subprocess.run(['sc', 'delete', service_name], check=True)
                #subprocess.run(['czlon1', 'czlon2', 'czlon3', 'czlon4', 'czlon5'], check=True)
                #Każdy człon polecenia, w tym jego argumenty, powinien być oddzielony jako osobny element listy. subprocess.run() automatycznie obsłuży te elementy i poprawnie uruchomi polecenie.

                # Wyświetl komunikat informujący o pomyślnym usunięciu usługi
                print(f"Usługa '{service_name}' została usunięta.")
            except subprocess.CalledProcessError as e:
                # Jeśli nie udało się usunąć usługi, wyświetl komunikat o błędzie
                print(f"Błąd podczas usuwania usługi '{service_name}': {e}")



def install_amigo_services(folder_path):
    # Ścieżka do katalogu \amigo
    amigo_directory = folder_path

    # Przeszukiwanie katalogu /amigo w poszukiwaniu usług
    for item in os.listdir(amigo_directory):
        full_path = os.path.join(amigo_directory, item)

        if os.path.isdir(full_path):
            # Sprawdź, czy podkatalog zawiera plik AMIGO.SERVICES.EXE
            amigo_services_exe = os.path.join(full_path, "AMIGO.SERVICES.EXE")
            amigo_svc_statistics_exe = os.path.join(full_path, "AMIGO.SVC.STATISTICS.EXE") #AMIGO.SVC.STATISTICS.exe
            #Sprawdź czy katalog zawiera AMIGO.SVC.STATISTICS.EXE dla uslugi STATISTICS
            if os.path.isfile(amigo_svc_statistics_exe):
                if os.path.isfile(os.path.join(full_path, "AMIGO.SVC.STATISTICS.EXE")) and (item.lower().startswith("amigo") or item.startswith("AMIGO")):
                    service_name = '.'.join(parts[:5])
                    print(f"Instalowanie usługi: {service_name}")
                    cmd = [amigo_svc_statistics_exe, "-i"]
                    try:
                        subprocess.run(cmd, cwd=full_path, check=True)
                        print(f"Usługa {service_name} została pomyślnie zainstalowana.")
                    except subprocess.CalledProcessError as e:
                        print(f"Błąd podczas instalowania usługi {service_name}: {e}")
            else:
                print(f"Podkatalog {item} nie zawiera pliku AMIGO.SVC.STATISTICS.EXE. Pomijanie...")

            #Sprawdź wszystkie katalogi pod kątem AMIGO.SERVICES.EXE
            if os.path.isfile(amigo_services_exe):
                # Sprawdź, czy nazwa katalogu pasuje do wzorca AMIGO.***.# i pobierz nazwę usługi
                parts = item.split('.')
                if os.path.isfile(os.path.join(full_path, "AMIGO.SERVICES.EXE")) and (item.lower().startswith("amigo") or item.startswith("AMIGO")):
                    if os.path.isfile(os.path.join(full_path, "amigo.exe")) and (item.lower().startswith("amigo") or item.startswith("AMIGO"))   :
                        break

                    service_name = '.'.join(parts[:5])
                    print(f"Instalowanie usługi: {service_name}")

                    # Uruchom komendę AMIGO.SERVICES.EXE -i
                    cmd = [amigo_services_exe, "-i", service_name]

                    try:
                        subprocess.run(cmd, cwd=full_path, check=True)
                        print(f"Usługa {service_name} została pomyślnie zainstalowana.")
                    except subprocess.CalledProcessError as e:
                        print(f"Błąd podczas instalowania usługi {service_name}: {e}")
            else:
                print(f"Podkatalog {item} nie zawiera pliku AMIGO.SERVICE.EXE. Pomijanie...")
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
layout = [
    [
        sg.Text("Choose location:"),
        sg.Input(size=(25, 1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse(),
        sg.Submit("Submit")
    ],
    [
        sg.Text("Selected path:"),
        sg.Text("", size=(25, 1), key="-PATH-"),
    ],
    [
        sg.Button("Delete all AMIGO Services")
    ],
    [
        sg.Output(size=(56, 10))
    ],
    [
         sg.Text('', size=(46, 1)),
         sg.Button("Exit")
    ],
]
icon_path = r'.\build\amigo.ico'  # Zmień na ścieżkę do twojego pliku ikony
sg.set_options(icon=icon_path)
run_as_admin()
#window.set_icon(icon_path)
# Create the window
window = sg.Window("Amigo (un)install services", layout, finalize=True)


# Event loop
while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, "Exit"):
        break

    elif event == "-FOLDER-":
        folder_path = values["-FOLDER-"]
        window["-PATH-"].update(folder_path)
    elif event == "Submit":
        #run_as_admin()
        window["-PATH-"].update(folder_path)
        install_amigo_services(folder_path)
    if event == "Delete all AMIGO Services":
       if __name__ == "__main__":
            #run_as_admin()
            print("Lista usług:")
            #list_services()

            print("\nUsuwanie usług rozpoczynających się od 'amigo':")
            uninstall_amigo_services()

# Close the window
window.close()
