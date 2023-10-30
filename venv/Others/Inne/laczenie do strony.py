import requests

# Dane uwierzytelniające
username = "admin"
password = "123456"

# Adres URL strony logowania na localhost
login_url = "http://localhost/phpmyadmin"  # Zaktualizuj adres URL do faktycznego adresu strony logowania

# Dane logowania
login_data = {
    "username": username,
    "password": password
}

# Tworzenie sesji
session = requests.Session()

# Logowanie na stronie
login_response = session.post(login_url, data=login_data)

# Sprawdzenie, czy zalogowano pomyślnie (możesz dostosować warunki)
if login_response.status_code == 200:
    print("Zalogowano pomyślnie.")

    # Tutaj możesz dodać kod do nawigacji po stronie po zalogowaniu
else:
    print("Nie udało się zalogować.")
