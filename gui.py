# === MODUŁ GUI - INTERFEJS UŻYTKOWNIKA ===
"""
Moduł zawierający interfejs graficzny aplikacji SqueezeIt.
Odpowiedzialny za:
- Tworzenie okien aplikacji
- Obsługę zdarzeń użytkownika
- Wyświetlanie komunikatów
- Integrację z logiką kompresji
"""

# import os
from typing import List, Optional, Tuple

import FreeSimpleGUI as sg  # noqa: N813

from core import KompresorPlikow, formatuj_rozmiar_pliku, oblicz_oszczednosc


class SqueezeItGUI:
    """
    Główna klasa interfejsu użytkownika aplikacji SqueezeIt.

    Atrybuty:
        window: Główne okno aplikacji
        kompresor: Instancja kompresora plików
    """

    def __init__(self):
        """Inicjalizuje interfejs użytkownika."""
        self.window = None
        self.kompresor = None

    def stworz_glowne_okno(self) -> sg.Window:
        """
        Tworzy główne okno aplikacji.

        Returns:
            sg.Window: Główne okno aplikacji
        """
        # === ELEMENTY INTERFEJSU ===

        # Nagłówek aplikacji
        naglowek = sg.Text(
            "🗜️ SqueezeIt - Kompresor Plików",
            font=("Arial", 16, "bold"),
            justification="center",
        )

        # Sekcja wyboru plików
        sekcja_pliki = [
            sg.Text("Pliki do kompresji:", font=("Arial", 12, "bold")),
            sg.Input(key="input_pliki", size=(40, 1), disabled=True),
            sg.FileBrowse(
                "Wybierz pliki",
                key="btn_wybierz_pliki",
                file_types=(("Pliki tekstowe", "*.txt"), ("Wszystkie pliki", "*.*")),
            ),
        ]

        # Sekcja wyboru folderu docelowego
        sekcja_folder = [
            sg.Text("Folder docelowy:", font=("Arial", 12, "bold")),
            sg.Input(key="input_folder", size=(40, 1), disabled=True),
            sg.FolderBrowse("Wybierz folder", key="btn_wybierz_folder"),
        ]

        # Sekcja ustawień kompresji
        sekcja_ustawienia = [
            sg.Text("Poziom kompresji:", font=("Arial", 12, "bold")),
            sg.Slider(
                range=(1, 9),
                default_value=6,
                orientation="h",
                key="slider_kompresja",
                size=(20, 15),
            ),
            sg.Text("6", key="label_poziom", size=(3, 1)),
        ]

        # Przyciski akcji
        przyciski = [
            sg.Button(
                "🗜️ Kompresuj",
                key="btn_kompresuj",
                size=(12, 1),
                button_color=("white", "green"),
            ),
            sg.Button(
                "📊 Statystyki",
                key="btn_statystyki",
                size=(12, 1),
                button_color=("white", "blue"),
            ),
            sg.Button(
                "❌ Wyjście",
                key="btn_wyjscie",
                size=(12, 1),
                button_color=("white", "red"),
            ),
        ]

        # Obszar wyników
        obszar_wynikow = [
            sg.Text("Wyniki operacji:", font=("Arial", 12, "bold")),
            sg.Multiline(
                key="output_wyniki",
                size=(60, 8),
                disabled=True,
                autoscroll=True,
                background_color="white",
                text_color="black",
            ),
        ]

        # === UKŁAD GŁÓWNEGO OKNA ===
        layout = [
            [naglowek],
            [sg.HSeparator()],
            [sekcja_pliki],
            [sg.HSeparator()],
            [sekcja_folder],
            [sg.HSeparator()],
            [sekcja_ustawienia],
            [sg.HSeparator()],
            [przyciski],
            [sg.HSeparator()],
            [obszar_wynikow],
        ]

        # Tworzenie okna
        window = sg.Window(
            "SqueezeIt - Kompresor Plików",
            layout,
            resizable=True,
            finalize=True,
            element_justification="center",
        )

        return window

    def aktualizuj_poziom_kompresji(self, poziom: int):
        """
        Aktualizuje wyświetlany poziom kompresji.

        Args:
            poziom (int): Nowy poziom kompresji
        """
        if self.window:
            self.window["label_poziom"].update(str(poziom))

    def dodaj_komunikat(self, komunikat: str):
        """
        Dodaje komunikat do obszaru wyników.

        Args:
            komunikat (str): Komunikat do wyświetlenia
        """
        if self.window:
            aktualne = self.window["output_wyniki"].get()
            nowy_tekst = f"{aktualne}\n{komunikat}" if aktualne else komunikat
            self.window["output_wyniki"].update(nowy_tekst)

    def wyczysc_wyniki(self):
        """Czyści obszar wyników."""
        if self.window:
            self.window["output_wyniki"].update("")

    def pokaz_okno_statystyk(self, statystyki: dict):
        """
        Wyświetla okno ze statystykami.

        Args:
            statystyki (dict): Słownik ze statystykami
        """
        layout_statystyki = [
            [sg.Text("📊 Statystyki Kompresji", font=("Arial", 14, "bold"))],
            [sg.HSeparator()],
            [sg.Text(f"Liczba operacji: {statystyki.get('liczba_operacji', 0)}")],
            [
                sg.Text(
                    f"Ostatnia operacja: {statystyki.get('ostatnia_operacja', 'Brak')}"
                )
            ],
            [sg.Text(f"Poziom kompresji: {statystyki.get('poziom_kompresji', 6)}")],
            [
                sg.Text(
                    f"Folder docelowy: {
                        statystyki.get('folder_docelowy', 'Nie ustawiony')
                    }"
                )
            ],
            [sg.HSeparator()],
            [sg.Button("Zamknij", key="btn_zamknij_statystyki")],
        ]

        okno_statystyk = sg.Window("Statystyki", layout_statystyki, modal=True)

        while True:
            event, values = okno_statystyk.read()
            if event in (sg.WIN_CLOSED, "btn_zamknij_statystyki"):
                break

        okno_statystyk.close()

    def pokaz_okno_wynikow(self, sukces: int, bledy: int, komunikaty: List[str]):
        """
        Wyświetla okno z wynikami kompresji.

        Args:
            sukces (int): Liczba pomyślnie skompresowanych plików
            bledy (int): Liczba błędów
            komunikaty (List[str]): Lista komunikatów
        """
        # Oblicz procent sukcesu
        total = sukces + bledy
        procent_sukcesu = (sukces / total * 100) if total > 0 else 0

        layout_wyniki = [
            [sg.Text("🎯 Wyniki Kompresji", font=("Arial", 14, "bold"))],
            [sg.HSeparator()],
            [sg.Text(f"✅ Pomyślnie: {sukces} plików")],
            [sg.Text(f"❌ Błędy: {bledy} plików")],
            [sg.Text(f"📊 Sukces: {procent_sukcesu:.1f}%")],
            [sg.HSeparator()],
            [sg.Text("Szczegóły:")],
            [
                sg.Multiline(
                    "\n".join(komunikaty),
                    size=(50, 10),
                    disabled=True,
                    key="output_szczegoly",
                )
            ],
            [sg.HSeparator()],
            [sg.Button("Zamknij", key="btn_zamknij_wyniki")],
        ]

        okno_wyniki = sg.Window("Wyniki", layout_wyniki, modal=True)

        while True:
            event, values = okno_wyniki.read()
            if event in (sg.WIN_CLOSED, "btn_zamknij_wyniki"):
                break

        okno_wyniki.close()

    def uruchom_aplikacje(self):
        """Uruchamia główną pętlę aplikacji."""
        # Tworzenie głównego okna
        self.window = self.stworz_glowne_okno()

        # Główna pętla zdarzeń
        while True:
            event, values = self.window.read()

            # Obsługa zamknięcia okna
            if event in (sg.WIN_CLOSED, "btn_wyjscie"):
                break

            # Obsługa zmiany poziomu kompresji
            elif event == "slider_kompresja":
                poziom = int(values["slider_kompresja"])
                self.aktualizuj_poziom_kompresji(poziom)

            # Obsługa przycisku kompresji
            elif event == "btn_kompresuj":
                self.obsluz_kompresje(values)

            # Obsługa przycisku statystyk
            elif event == "btn_statystyki":
                self.obsluz_statystyki()

        # Zamknięcie aplikacji
        self.window.close()

    def obsluz_kompresje(self, values: dict):
        """
        Obsługuje proces kompresji plików.

        Args:
            values (dict): Wartości z formularza
        """
        # Pobierz dane z formularza
        pliki_tekst = values.get("input_pliki", "")
        folder_docelowy = values.get("input_folder", "")
        poziom_kompresji = int(values.get("slider_kompresja", 6))

        # Walidacja danych wejściowych
        if not pliki_tekst:
            sg.popup_error("❌ Wybierz pliki do kompresji!")
            return

        if not folder_docelowy:
            sg.popup_error("❌ Wybierz folder docelowy!")
            return

        # Konwersja ścieżki plików na listę
        # FreeSimpleGUI FileBrowse zwraca ścieżkę jako string
        sciezki_plikow = [pliki_tekst] if isinstance(pliki_tekst, str) else pliki_tekst

        try:
            # Inicjalizacja kompresora
            self.kompresor = KompresorPlikow(folder_docelowy, poziom_kompresji)

            # Wyczyść obszar wyników
            self.wyczysc_wyniki()
            self.dodaj_komunikat("🚀 Rozpoczynam kompresję...")

            # Kompresja plików
            sukces, bledy, komunikaty = self.kompresor.kompresuj_wiele_plikow(
                sciezki_plikow
            )

            # Wyświetl wyniki w obszarze wyników
            for komunikat in komunikaty:
                self.dodaj_komunikat(komunikat)

            # Podsumowanie
            self.dodaj_komunikat("\n📊 Podsumowanie:")
            self.dodaj_komunikat(f"✅ Pomyślnie: {sukces} plików")
            self.dodaj_komunikat(f"❌ Błędy: {bledy} plików")

            # Pokaż okno z wynikami
            self.pokaz_okno_wynikow(sukces, bledy, komunikaty)

        except Exception as e:
            komunikat_bledu = f"❌ Błąd aplikacji: {str(e)}"
            self.dodaj_komunikat(komunikat_bledu)
            sg.popup_error(komunikat_bledu)

    def obsluz_statystyki(self):
        """Obsługuje wyświetlanie statystyk."""
        if self.kompresor:
            statystyki = self.kompresor.pobierz_statystyki()
            self.pokaz_okno_statystyk(statystyki)
        else:
            sg.popup("ℹ️ Brak danych - wykonaj najpierw kompresję plików.")


def uruchom_aplikacje():
    """
    Funkcja pomocnicza do uruchomienia aplikacji.
    Używana w main.py jako punkt wejścia.
    """
    app = SqueezeItGUI()
    app.uruchom_aplikacje()
