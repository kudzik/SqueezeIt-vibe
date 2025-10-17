import FreeSimpleGUI as sg  # noqa: N813

label_compressor = sg.Text("Files to compress", key="label_compressor")
input_compressor = sg.Input(key="input_compressor")
choose_button1 = sg.FileBrowse("Choose Files")

label_destination = sg.Text("Destination Folder", key="label_destination")
input_destination = sg.Input(key="input_destination")
choose_destination = sg.FolderBrowse("Choose Destination")

compress_button = sg.Button("Compress", key="compress_btn")

layout = [
    [label_compressor, input_compressor, choose_button1],
    [label_destination, input_destination, choose_destination],
    [compress_button],
]


window = sg.Window("SqueezeIt File Compressor", layout=layout)

# Główna pętla zdarzeń - aplikacja działa dopóki użytkownik nie zamknie okna
while True:
    event, values = window.read()

    # Sprawdzenie czy użytkownik zamknął okno
    if event == sg.WIN_CLOSED:
        break

    # Obsługa przycisku kompresji
    if event == "compress_btn":
        print("Przycisk Compress został kliknięty!")
        print(f"Pliki do kompresji: {values['input_compressor']}")
        print(f"Folder docelowy: {values['input_destination']}")

        # Tutaj będzie logika kompresji
        sg.popup(
            "Funkcja kompresji będzie wkrótce zaimplementowana!",
            title="Info",
            keep_on_top=True,
        )

window.close()
