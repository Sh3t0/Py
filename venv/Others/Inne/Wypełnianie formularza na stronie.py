from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import PySimpleGUI as sg
import time
import csv

def create_user_groups(grp_no):
    # Tworzenie grup użytkowników
    create_group_button = driver.find_element(By.XPATH, '//button[contains(@aria-label, "plus-circle")]')
    create_group_button.click()
    time.sleep(1)

    group_name = f"Users_Grp_{grp_no}"
    group_name_input = driver.find_element(By.ID, "group_name")
    group_name_input.send_keys(group_name)
    create_group_confirm_button = driver.find_element(By.XPATH, '//button[contains(text(), "Potwierdź")]')
    create_group_confirm_button.click()
    time.sleep(1)


def login_and_navigate_to_admin_page(base_url, username, password, url, session_duration_minutes, csv_file_path):
    # Inicjalizacja przeglądarki Microsoft Edge
    driver = webdriver.Edge()
    entry_count = 0 # licznik userow
    grp_no = 0 #licznik grup
    try:
        # Przejście do strony logowania
        driver.get(f"{base_url}/#/login")

        # Znajdź pola do wprowadzenia loginu i hasła
        username_input = driver.find_element(By.ID, "login_username")
        password_input = driver.find_element(By.ID, "login_password")

        # Wprowadź dane uwierzytelniające i zaloguj się
        username_input.send_keys(username)
        password_input.send_keys(password)
        password_input.send_keys(Keys.ENTER)

        # Odczekaj na załadowanie strony logowania
        time.sleep(2)

        # Przejście do zakładki administracyjnej
        driver.get(url)

        # Odczekaj na załadowanie strony "admin/person"
        time.sleep(2)

        # Wczytaj dane z pliku CSV

######## KASOWANIE PREWENCYJNE #############
#        del_button = driver.find_element(By.XPATH, '//button[@class="ant-btn ant-btn-primary ant-btn-dangerous" and contains(.,"Delete All")]')
#        del_button.click()
#        time.sleep(2)
#        #ant-btn ant-btn-primary ant-btn-sm
#        del_ok_button = driver.find_element(By.XPATH, '//button[@class="ant-btn ant-btn-primary ant-btn-sm" and contains(.,"OK")]')
#        del_ok_button.click()
#        time.sleep(2)
######## KASOWANIE PREWENCYJNE #############

#____________________________________________________________________________________________________________________
        with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
            csvreader = csv.DictReader(csvfile, delimiter=';')
            for row in csvreader:
                #print(f"Przetwarzanie wpisu {entry_count + 1}...")
                 # Kliknij przycisk "Userzy"
                entry_count += 1
                try:# szukaj grupy i wybierz grupe
                    users_button = driver.find_element(By.XPATH, f'//span[contains(text(), "Users_Grp_{grp_no}")]')
                    actions = ActionChains(driver)
                    actions.move_to_element(users_button)
                    actions.click(users_button)
                    actions.perform()
                    time.sleep(1)
                except NoSuchElementException: #jesli nie ma utworz grupe
                    plus_button = driver.find_element(By.XPATH, '//button[contains(@class, "ant-btn ant-btn-text ant-btn-icon-only")]')
                    plus_button.click()
                    time.sleep(1)

                    group_name = f"Users_Grp_{grp_no}"
                    group_name_input = driver.find_element(By.ID, "groupAction_name")
                    group_name_input.send_keys(group_name)
                    group_name_input.send_keys(Keys.TAB*2 + Keys.ENTER)
                    time.sleep(2)
                    #wybierz grupe
                    users_button = driver.find_element(By.XPATH, f'//span[contains(text(), "Users_Grp_{grp_no}")]')
                    actions = ActionChains(driver)
                    actions.move_to_element(users_button)
                    actions.click(users_button)
                    actions.perform()
                    time.sleep(2)
                    #grp_no += 1

                #
                #------- wypelnianie formularza
                #

                add_button = driver.find_element(By.XPATH, '//button[@class="ant-btn ant-btn-primary" and contains(.,"Add")]')
                add_button.click()
                name = row["Name"].replace(" ", "_")
                room_no = row["RoomNo"]
                card_no = row["CardNo"]

                # Znajdź odpowiednie pola na stronie i wprowadź wartości
                name_input = driver.find_element(By.ID, "userAction_name")
                name_input.send_keys(name)

                room_no_input = driver.find_element(By.ID, "userAction_room")
                room_no_input.send_keys(room_no)

                card_no_input = driver.find_element(By.ID, "userAction_cards_0")
                card_no_input.send_keys(card_no)


                # Relays
                relay_0 = driver.find_element(By.ID, "userAction_relay_0")
                relay_0.click()

                relay_1 = driver.find_element(By.ID, "userAction_relay_1")
                relay_1.click()

                relay_2 = driver.find_element(By.ID, "userAction_relay_2")
                relay_2.click()

                # Kliknij przycisk "Status" i potwierdź przyciskiem Enter
                status_button = driver.find_element(By.ID, "userAction_status")
                status_button.click()

                status_button.send_keys(Keys.TAB*6 + Keys.ENTER) # przejdz do przycisku OK
                time.sleep(2)
                try: #sprawdz czy komunikat Save error! istnieje jesli nie to pomin
                    driver.find_element(By.XPATH, '//div[@class="ant-notification-notice-message" and contains(.,"Save error!")]')
                    status_button.send_keys(Keys.TAB*8 + Keys.ENTER) # X dla komunikatu
                except NoSuchElementException:
                    pass






                #
                #------- wypelnianie formularza
                #

                if entry_count == 2: #ilosc userow na grupe
                    ###### DODAJ GRUPE #########
                    grp_no += 1
                    if grp_no >= 3:
                        break
                    plus_button = driver.find_element(By.XPATH, '//button[contains(@class, "ant-btn ant-btn-text ant-btn-icon-only")]')
                    plus_button.click()
                    time.sleep(2)

                    group_name = f"Users_Grp_{grp_no}"
                    group_name_input = driver.find_element(By.ID, "groupAction_name")
                    group_name_input.send_keys(group_name)
                    group_name_input.send_keys(Keys.TAB*2 + Keys.ENTER) # ok dla tworzenia grupy
                    time.sleep(2)

                    try: #sprawdz czy komunikat Save error! istnieje jesli nie to pomin
                        driver.find_element(By.XPATH, '//div[@class="ant-notification-notice-message" and contains(.,"Save error!")]')
                        status_button.send_keys(Keys.TAB*8 + Keys.ENTER) # X dla komunikatu
                    except NoSuchElementException:
                        pass


                    entry_count = 0  # Resetuj licznik

    

    finally:
        # Zamknij przeglądarkę po upływie sesji
        sg.popup("Koniec")
        time.sleep(60*30) #utrzymuj sesje
        driver.quit()



sg.theme('DarkGrey11')
layout = [
    [
        sg.Text("Choose file:"),
        sg.Input("C:/temp/BazaU.csv", size=(30, 1), enable_events=True, key="-FILE-", tooltip='Choose csv file'),
        sg.FileBrowse(),
        sg.Submit("Submit")
    ],

    [
        sg.Text("User:          "),
        sg.Input("admin", size=(30, 1), key="-User-"),
    ],
    [
        sg.Text("Password:  "),
        sg.Input("123456", size=(30, 1), key="-Password-"),
    ],
    [
        sg.Text("IP:             "),
        sg.Input("http://192.168.68.90", size=(30, 1), key="-IP-"),
    ],

]

window = sg.Window("InPutter Demo", layout, finalize=True)
while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, "Exit"):
        break
    elif event == "Submit":
        folder_path = values["-FILE-"]
        if not folder_path:
            sg.popup("Choose path")
        else:
            #folder_path = values["-FILE-"]
            #window["-PATH-"].update(folder_path)
            username = values["-User-"]
            password = values["-Password-"]
            base_url = values["-IP-"]
            url = values["-IP-"] + "/#/admin/person" # G:/Share/Testfiles/BazaU.csv
            csv_file_path = values["-FILE-"]
            window.hide()
            login_and_navigate_to_admin_page(base_url, username, password, url, 30, csv_file_path)


window.close()

