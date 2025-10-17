# === MODUŁ CORE - LOGIKA KOMPRESJI ===
"""
Moduł zawierający główną logikę kompresji plików.
Odpowiedzialny za:
- Kompresję plików tekstowych
- Walidację plików
- Obsługę błędów
- Logowanie operacji
"""

import os
import zipfile
from datetime import datetime
from typing import List, Tuple


class KompresorPlikow:
    """
    Główna klasa odpowiedzialna za kompresję plików.

    Atrybuty:
        sciezka_docelowa (str): Ścieżka do folderu docelowego
        poziom_kompresji (int): Poziom kompresji (1-9)
        log_operacji (List[str]): Lista wykonanych operacji
    """

    def __init__(self, sciezka_docelowa: str, poziom_kompresji: int = 6):
        """
        Inicjalizuje kompresor plików.

        Args:
            sciezka_docelowa (str): Folder gdzie zapisać skompresowane pliki
            poziom_kompresji (int): Poziom kompresji od 1 (najszybszy) do 9 (najlepszy)
        """
        self.sciezka_docelowa = sciezka_docelowa
        self.poziom_kompresji = min(max(poziom_kompresji, 1), 9)  # Ograniczenie 1-9
        self.log_operacji = []

        # Sprawdź czy folder docelowy istnieje, jeśli nie - stwórz go
        if not os.path.exists(sciezka_docelowa):
            os.makedirs(sciezka_docelowa)

    def waliduj_pliki(self, sciezki_plikow: list[str]) -> tuple[list[str], list[str]]:
        """
        Sprawdza czy pliki istnieją i są dostępne do kompresji.

        Args:
            sciezki_plikow (List[str]): Lista ścieżek do plików

        Returns:
            Tuple[List[str], List[str]]: (pliki_prawidlowe, pliki_bledne)
        """
        pliki_prawidlowe = []
        pliki_bledne = []

        for sciezka in sciezki_plikow:
            if os.path.exists(sciezka) and os.path.isfile(sciezka):
                # Sprawdź czy plik można odczytać
                try:
                    with open(sciezka, "rb") as f:
                        f.read(1)  # Próba odczytu pierwszego bajtu
                    pliki_prawidlowe.append(sciezka)
                except (PermissionError, IOError):
                    pliki_bledne.append(f"{sciezka} - brak uprawnień do odczytu")
            else:
                pliki_bledne.append(f"{sciezka} - plik nie istnieje")

        return pliki_prawidlowe, pliki_bledne

    def kompresuj_plik(self, sciezka_pliku: str) -> tuple[bool, str, str]:
        """
        Kompresuje pojedynczy plik tekstowy.

        Args:
            sciezka_pliku (str): Ścieżka do pliku do skompresowania

        Returns:
            Tuple[bool, str, str]: (sukces, sciezka_wyniku, komunikat)
        """
        try:
            # Pobierz nazwę pliku bez rozszerzenia
            nazwa_pliku = os.path.basename(sciezka_pliku)
            nazwa_bez_rozszerzenia = os.path.splitext(nazwa_pliku)[0]

            # Stwórz nazwę pliku wynikowego
            sciezka_wyniku = os.path.join(
                self.sciezka_docelowa, f"{nazwa_bez_rozszerzenia}.zip"
            )

            # Kompresja pliku
            with zipfile.ZipFile(
                sciezka_wyniku,
                "w",
                zipfile.ZIP_DEFLATED,
                compresslevel=self.poziom_kompresji,
            ) as zipf:
                zipf.write(sciezka_pliku, nazwa_pliku)

            # Logowanie operacji
            komunikat = f"Plik {nazwa_pliku} skompresowany pomyślnie"
            self.log_operacji.append(f"{datetime.now()}: {komunikat}")

            return True, sciezka_wyniku, komunikat

        except Exception as e:
            komunikat = (
                f"Błąd kompresji pliku {os.path.basename(sciezka_pliku)}: {str(e)}"
            )
            self.log_operacji.append(f"{datetime.now()}: {komunikat}")
            return False, "", komunikat

    def kompresuj_wiele_plikow(
        self, sciezki_plikow: list[str]
    ) -> tuple[int, int, list[str]]:
        """
        Kompresuje wiele plików do osobnych archiwów ZIP.

        Args:
            sciezki_plikow (List[str]): Lista ścieżek do plików

        Returns:
            Tuple[int, int, List[str]]: (liczba_sukcesow, liczba_bledow, komunikaty)
        """
        # Walidacja plików
        pliki_prawidlowe, pliki_bledne = self.waliduj_pliki(sciezki_plikow)

        komunikaty = []
        liczba_sukcesow = 0
        liczba_bledow = len(pliki_bledne)

        # Dodaj komunikaty o błędach walidacji
        for blad in pliki_bledne:
            komunikaty.append(f"❌ {blad}")

        # Kompresja prawidłowych plików
        for sciezka_pliku in pliki_prawidlowe:
            sukces, sciezka_wyniku, komunikat = self.kompresuj_plik(sciezka_pliku)

            if sukces:
                liczba_sukcesow += 1
                komunikaty.append(f"✅ {komunikat}")
            else:
                liczba_bledow += 1
                komunikaty.append(f"❌ {komunikat}")

        return liczba_sukcesow, liczba_bledow, komunikaty

    def pobierz_statystyki(self) -> dict:
        """
        Zwraca statystyki wykonanych operacji.

        Returns:
            dict: Słownik ze statystykami
        """
        return {
            "liczba_operacji": len(self.log_operacji),
            "ostatnia_operacja": self.log_operacji[-1]
            if self.log_operacji
            else "Brak operacji",
            "poziom_kompresji": self.poziom_kompresji,
            "folder_docelowy": self.sciezka_docelowa,
        }

    def wyczysc_log(self):
        """Czyści historię operacji."""
        self.log_operacji.clear()


def formatuj_rozmiar_pliku(rozmiar_bajty: int) -> str:
    """
    Formatuje rozmiar pliku w czytelnej postaci.

    Args:
        rozmiar_bajty (int): Rozmiar w bajtach

    Returns:
        str: Sformatowany rozmiar (np. "1.5 MB")
    """
    if rozmiar_bajty < 1024:
        return f"{rozmiar_bajty} B"
    elif rozmiar_bajty < 1024 * 1024:
        return f"{rozmiar_bajty / 1024:.1f} KB"
    elif rozmiar_bajty < 1024 * 1024 * 1024:
        return f"{rozmiar_bajty / (1024 * 1024):.1f} MB"
    else:
        return f"{rozmiar_bajty / (1024 * 1024 * 1024):.1f} GB"


def oblicz_oszczednosc(rozmiar_przed: int, rozmiar_po: int) -> float:
    """
    Oblicza procent oszczędności miejsca.

    Args:
        rozmiar_przed (int): Rozmiar przed kompresją
        rozmiar_po (int): Rozmiar po kompresji

    Returns:
        float: Procent oszczędności (0-100)
    """
    if rozmiar_przed == 0:
        return 0.0
    return ((rozmiar_przed - rozmiar_po) / rozmiar_przed) * 100
