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
#__________________________________________________________________________________________________________________________________________

############### TAB 1 ##########################
# Funkcja usuwająca uslugi amigo
@functools.lru_cache()
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
    print('Nic nie usunięto')


@functools.lru_cache()
def install_amigo_services(folder_path):
    # Ścieżka do katalogu \amigo
    amigo_directory = folder_path

    # Przeszukiwanie katalogu /amigo w poszukiwaniu usług
    for item in os.listdir(amigo_directory):
        full_path = os.path.join(amigo_directory, item)

        if os.path.isdir(full_path):
            # Zmień nazwę katalogu na małe litery
            item_lower = item.lower()

            # Pomijaj katalogi zawierające frazę ".ui" lub ".UI" w nazwie
            if ".ui" in item_lower:
                print(f"Katalog {item} zawiera frazę '.ui' w nazwie. Pomijanie...")
                continue

            # Sprawdź, czy podkatalog zawiera plik AMIGO.SERVICES.EXE
            amigo_services_exe = os.path.join(full_path, "AMIGO.SERVICES.EXE")
            amigo_svc_statistics_exe = os.path.join(full_path, "AMIGO.SVC.STATISTICS.EXE")

            if os.path.isfile(amigo_svc_statistics_exe) and (item_lower.startswith("amigo")):
                service_name = item  # Użyj oryginalnej nazwy katalogu
                print(f"Instalowanie usługi: {service_name}")
                cmd = [amigo_svc_statistics_exe, "-i"]
                try:
                    subprocess.run(cmd, cwd=full_path, check=True)
                    print(f"Usługa {service_name} została pomyślnie zainstalowana.")
                except subprocess.CalledProcessError as e:
                    print(f"Błąd podczas instalowania usługi {service_name}: {e}")
            if os.path.isfile(amigo_services_exe) and (item_lower.startswith("amigo")):
                service_name = item  # Użyj oryginalnej nazwy katalogu
                print(f"Instalowanie usługi: {service_name}")
                cmd = [amigo_services_exe, "-i", service_name]
                try:
                    subprocess.run(cmd, cwd=full_path, check=True)
                    print(f"Usługa {service_name} została pomyślnie zainstalowana.")
                except subprocess.CalledProcessError as e:
                    print(f"Błąd podczas instalowania usługi {service_name}: {e}")
            else:
                print(f"Podkatalog {item} nie zawiera odpowiednich plików lub nie spełnia warunku nazwy. Pomijanie...")


    sys.exit()

# Funkcja do pobierania listy usług rozpoczynających się od 'AMIGO' lub 'amigo'
@functools.lru_cache()
def get_amigo_services():
    service_list = []
    for service in psutil.win_service_iter():
        if service.name().startswith('AMIGO.') or service.name().startswith('amigo.'):
            service_list.append(service.name())
    return service_list


############### TAB 2 ##########################
# Funkcja do uruchamiania usługi
def start_service(service_name):
    try:
        service = psutil.win_service_get(service_name)
        if service.status() == psutil.STATUS_RUNNING:
            print(f"The service '{service_name}' is already running.")
        else:
            subprocess.run(["sc", "start", service_name], check=True)
            print(f"The service '{service_name}' has been started successfully.")
    except Exception as e:
            print(f"Error starting the service '{service_name}': {str(e)}")

# Funkcja do zatrzymywania usługi
def stop_service(service_name):
    try:
        service = psutil.win_service_get(service_name)
        if service.status() == psutil.STATUS_STOPPED:
            print(f"The service '{service_name}' is already stopped.")
        else:
            # Zatrzymywanie usługi za pomocą komendy systemowej
            subprocess.run(["sc", "stop", service_name], check=True)
            print(f"The service '{service_name}' has been stopped successfully.")
    except Exception as e:
        print(f"Error stopping the service '{service_name}': {str(e)}")
def restart_service(service_name):
    try:
        service = psutil.win_service_get(service_name)
        subprocess.run(["sc", "stop", service_name], check=True)
        subprocess.run(["sc", "start", service_name], check=True)
        print(f"The service '{service_name}' has been restarted successfully.")
    except Exception as e:
        print(f"Error restarting the service '{service_name}': {str(e)}")


# Funkcja do startowania wszystkich usług
def start_all_services():
    service_list = get_amigo_services()
    for service_name in service_list:
        start_service(service_name)

# Funkcja do zatrzymywania wszystkich usług
def stop_all_services():
    service_list = get_amigo_services()
    for service_name in service_list:
        stop_service(service_name)

def restart_all_services():
    service_list = get_amigo_services()
    for service_name in service_list:
        restart_service(service_name)


# Funkcja do restartowania usługi



############### TAB 4 ##########################
# Funkcja do usuwania najnowszego logu w folderze
def delete_latest_log(folder_path):
    latest_log = None
    latest_log_path = None

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            if not latest_log or os.path.getctime(file_path) > latest_log:
                latest_log = os.path.getctime(file_path)
                latest_log_path = file_path

    if latest_log_path:
        os.remove(latest_log_path)

# Funkcja do archiwizacji najnowszego logu w folderze
def archive_latest_log(folder_path, archive_folder_path):
    latest_log = None
    latest_log_path = None

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            if not latest_log or os.path.getctime(file_path) > latest_log:
                latest_log = os.path.getctime(file_path)
                latest_log_path = file_path

    if latest_log_path:
        shutil.move(latest_log_path, os.path.join(archive_folder_path, os.path.basename(latest_log_path)))
def delete_all_logs(log_folder_path, history, unique_messages):
    for root, dirs, files in os.walk(log_folder_path):
        for directory in dirs:
            log_dir = os.path.join(root, directory, "logs")
            if os.path.exists(log_dir):
                for log_file in os.listdir(log_dir):
                    log_file_path = os.path.join(log_dir, log_file)
                    try:
                        os.remove(log_file_path)
                        message = f"Pliki w katalogu '{log_dir}' zostały usunięte."
                        if message not in unique_messages:
                            history.append(message)
                            unique_messages.add(message)
                    except Exception as e:
                        message = f"Błąd podczas usuwania pliku '{log_file_path}': {str(e)}"
                        if message not in unique_messages:
                            history.append(message)
                            unique_messages.add(message)

def delete_latest_log(log_folder_path, history, unique_messages):
    latest_log_path = None
    latest_log_time = None

    for root, dirs, files in os.walk(log_folder_path):
        for directory in dirs:
            log_dir = os.path.join(root, directory, "logs")
            if os.path.exists(log_dir):
                for log_file in os.listdir(log_dir):
                    log_file_path = os.path.join(log_dir, log_file)
                    file_time = os.path.getctime(log_file_path)
                    if latest_log_time is None or file_time > latest_log_time:
                        latest_log_time = file_time
                        latest_log_path = log_file_path

    if latest_log_path:
        try:
            os.remove(latest_log_path)
            message = f"Usunięto najnowszy plik: '{latest_log_path}'."
            if message not in unique_messages:
                history.append(message)
                unique_messages.add(message)
        except Exception as e:
            message = f"Błąd podczas usuwania najnowszego pliku: '{str(e)}'."
            if message not in unique_messages:
                history.append(message)
                unique_messages.add(message)


def archive_all_logs(log_folder_path, history, unique_messages):
    for root, dirs, files in os.walk(log_folder_path):
        for directory in dirs:
            log_dir = os.path.join(root, directory, "logs")
            archiv_dir = os.path.join(log_dir, "archiv")

            if os.path.exists(log_dir):
                # Sprawdź, czy katalog 'archiv' istnieje, jeśli nie, to go utwórz
                if not os.path.exists(archiv_dir):
                    os.makedirs(archiv_dir)

                for log_file in os.listdir(log_dir):
                    log_file_path = os.path.join(log_dir, log_file)
                    archiv_file_path = os.path.join(archiv_dir, log_file)

                    try:
                        shutil.move(log_file_path, archiv_file_path)
                        message = f"Plik '{log_file}' został przeniesiony do katalogu 'archiv' w '{log_dir}'."
                        if message not in unique_messages:
                            history.append(message)
                            unique_messages.add(message)
                    except Exception as e:
                        message = f"Błąd podczas przenoszenia pliku '{log_file}' do 'archiv': {str(e)}"
                        if message not in unique_messages:
                            history.append(message)
                            unique_messages.add(message)
def archive_latest_log(log_folder_path, history, unique_messages):
    for root, dirs, files in os.walk(log_folder_path):
        for directory in dirs:
            log_dir = os.path.join(root, directory, "logs")

            if os.path.exists(log_dir):
                latest_log = None
                latest_log_path = None

                for log_file in os.listdir(log_dir):
                    log_file_path = os.path.join(log_dir, log_file)
                    log_file_time = os.path.getctime(log_file_path)

                    if not latest_log or log_file_time > latest_log:
                        latest_log = log_file_time
                        latest_log_path = log_file_path

                if latest_log_path:
                    archiv_dir = os.path.join(log_dir, "archiv")

                    # Sprawdź, czy katalog 'archiv' istnieje, jeśli nie, to go utwórz
                    if not os.path.exists(archiv_dir):
                        os.makedirs(archiv_dir)

                    archiv_file_path = os.path.join(archiv_dir, os.path.basename(latest_log_path))

                    try:
                        shutil.move(latest_log_path, archiv_file_path)
                        message = f"Najnowszy plik '{os.path.basename(latest_log_path)}' został przeniesiony do katalogu 'archiv' w '{log_dir}'."
                        if message not in unique_messages:
                            history.append(message)
                            unique_messages.add(message)
                    except Exception as e:
                        message = f"Błąd podczas przenoszenia najnowszego pliku do 'archiv': {str(e)}"
                        if message not in unique_messages:
                            history.append(message)
                            unique_messages.add(message)




######################## INNE ##################################
# Funkcja do sprawdzania i otwierania konsoli jako administrator
def run_as_admin():
    if ctypes.windll.shell32.IsUserAnAdmin() == 0:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 0)
        sys.exit()

# Lista of ALL Services
@functools.lru_cache()
def list_services():
    services = psutil.win_service_iter()
    for service in services:
        service_name = service.name()
        service_status = service.status()
        print(f"Usługa: {service_name}, Status: {service_status}")


# Wątek do aktualizacji statusu usług w GUI
def update_service_status_thread(window):
    while True:
        service_list = get_amigo_services()
        for service_name in service_list:
            try:
                service = psutil.win_service_get(service_name)
                status = service.status()
                window[service_name].update(f"{service_name} - Status: {status}")
            except Exception as e:
                print(f"Error updating status for the service '{service_name}': {str(e)}")
        time.sleep(5)  # Aktualizacja co 5 sekund



def update_output(output_elem, history):
    output_elem.update("\n".join(history))

def refresh_logs_periodically(log_folder_path, window, stop_event, history, unique_messages):
    last_modified_times = {}  # Słownik przechowujący czasy ostatniej modyfikacji katalogów

    while not stop_event.is_set():
        changes_detected = False  # Flaga informująca, czy wykryto zmiany w katalogach

        for root, dirs, files in os.walk(log_folder_path):
            for directory in dirs:
                log_dir = os.path.join(root, directory, "logs")
                if os.path.exists(log_dir):
                    for log_file in os.listdir(log_dir):
                        log_file_path = os.path.join(log_dir, log_file)
                        last_modified_time = os.path.getmtime(log_file_path)

                        # Sprawdź, czy czas modyfikacji pliku się zmienił
                        if log_file_path in last_modified_times:
                            if last_modified_times[log_file_path] != last_modified_time:
                                changes_detected = True
                                last_modified_times[log_file_path] = last_modified_time
                        else:
                            changes_detected = True
                            last_modified_times[log_file_path] = last_modified_time

        if changes_detected:
            # Jeśli wykryto zmiany, zaktualizuj interfejs graficzny
            update_output(window["-PROGRESS_OUTPUT-"], history)
            window.refresh()  # Aktualizacja okna

        stop_event.wait(1)
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

    [
         sg.Text('ServiceConfig', size=(46, 1))
         # TODO #
    ],
]


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
window = sg.Window("Amigo Menager", layout, finalize=True)

# Uruchomienie wątku aktualizacji statusu usług
update_thread = threading.Thread(target=update_service_status_thread, args=(window,))
update_thread.daemon = True
update_thread.start()

# Uruchomienie wątku aktualizacji statusu usług

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
    elif event == 'Archive All Logs':
        archive_all_logs(log_folder_path, archive_folder_path)
        window["-LOG_LIST-"].update(values=[])
    elif event == 'Delete Latest Log':
        delete_latest_log(log_folder_path)
        window["-LOG_LIST-"].update(values=get_log_files(log_folder_path))
    elif event == 'Archive Latest Log':
        archive_latest_log(log_folder_path, archive_folder_path)
        window["-LOG_LIST-"].update(values=get_log_files(log_folder_path))


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


# Close the window
window.close()
