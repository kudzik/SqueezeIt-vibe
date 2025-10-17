# Import biblioteki FreeSimpleGUI do tworzenia interfejsu graficznego
import FreeSimpleGUI as sg  # noqa: N813

# === ELEMENTY INTERFEJSU UŻYTKOWNIKA ===

# Etykieta i pole do wyboru plików do kompresji
label_compressor = sg.Text("Files to compress", key="label_compressor")
input_compressor = sg.Input(key="input_compressor")  # Pole tekstowe na ścieżkę pliku
choose_button1 = sg.FileBrowse("Choose Files")  # Przycisk do wyboru plików

# Etykieta i pole do wyboru folderu docelowego
label_destination = sg.Text("Destination Folder", key="label_destination")
input_destination = sg.Input(
    key="input_destination"
)  # Pole tekstowe na ścieżkę folderu
choose_destination = sg.FolderBrowse("Choose Destination")  # Przycisk do wyboru folderu

# Przycisk do uruchomienia kompresji
compress_button = sg.Button("Compress", key="compress_btn")

# === UKŁAD INTERFEJSU ===
# Layout definiuje jak elementy GUI są rozmieszczone w oknie
# Każda lista w layout to jeden rząd elementów
layout = [
    [label_compressor, input_compressor, choose_button1],  # Rząd 1: wybór plików
    [label_destination, input_destination, choose_destination],  # Rząd 2: wybór folderu
    [compress_button],  # Rząd 3: przycisk kompresji
]

# === TWORZENIE OKNA APLIKACJI ===
# Window to główne okno aplikacji z tytułem i układem elementów
window = sg.Window("SqueezeIt File Compressor", layout=layout)

# === GŁÓWNA PĘTLA ZDARZEŃ ===
# Aplikacja działa w pętli dopóki użytkownik nie zamknie okna
while True:
    # Czytanie zdarzeń i wartości z interfejsu
    # event - co się stało (kliknięcie, zamknięcie okna)
    # values - wartości z pól tekstowych i innych elementów
    event, values = window.read()

    # === OBSŁUGA ZAMKNIĘCIA OKNA ===
    # Sprawdzenie czy użytkownik zamknął okno (X w prawym górnym rogu)
    if event == sg.WIN_CLOSED:
        break  # Wyjście z pętli i zakończenie aplikacji

    # === OBSŁUGA PRZYCISKU KOMPRESJI ===
    # Sprawdzenie czy użytkownik kliknął przycisk "Compress"
    if event == "compress_btn":
        # Wyświetlenie informacji debug w konsoli
        print("Przycisk Compress został kliknięty!")
        print(f"Pliki do kompresji: {values['input_compressor']}")
        print(f"Folder docelowy: {values['input_destination']}")

        # Wyświetlenie komunikatu użytkownikowi
        # Tutaj będzie logika kompresji w przyszłości
        sg.popup(
            "Funkcja kompresji będzie wkrótce zaimplementowana!",
            title="Info",
            keep_on_top=True,  # Okno popup będzie na wierzchu
        )

# === ZAMKNIĘCIE APLIKACJI ===
# Zawsze zamykaj okno na końcu - zwalnia zasoby systemowe
window.close()
