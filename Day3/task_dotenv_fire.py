import os

import requests
from dotenv import load_dotenv
import fire

def search_training(keyword: str):
    # Wczytanie adresu URL z pliku .env
    load_dotenv()
    url = os.getenv("TRAINING_URL")

    response = requests.get(url)
    data = response.json()

    # Filtracja
    filtered_trainings = [training for training in data if keyword.lower() in training['tytul_szkolenia'].lower()]

    print("Znalezione szkolenia:")
    for training in filtered_trainings:
        print(f"Tytuł: {training['tytul_szkolenia']}, Miasto: {training['miasto']}, Data: {training['termin']}")


# Opakowanie funkcji przy użyciu biblioteki fire
if __name__ == "__main__":
    #search_training('python') # dla debugowania
    fire.Fire(search_training)