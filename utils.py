# === MODUŁ UTILS - FUNKCJE POMOCNICZE ===
"""
Moduł zawierający funkcje pomocnicze dla aplikacji SqueezeIt.
Odpowiedzialny za:
- Operacje na plikach
- Konwersje danych
- Funkcje systemowe
- Narzędzia debugowania
"""

import os
import time
from datetime import datetime
from typing import Any, Dict, List


def sprawdz_rozszerzenie_pliku(sciezka_pliku: str) -> str:
    """
    Sprawdza rozszerzenie pliku.

    Args:
        sciezka_pliku (str): Ścieżka do pliku

    Returns:
        str: Rozszerzenie pliku (np. '.txt', '.csv')
    """
    return os.path.splitext(sciezka_pliku)[1].lower()


def czy_plik_tekstowy(sciezka_pliku: str) -> bool:
    """
    Sprawdza czy plik to plik tekstowy na podstawie rozszerzenia.

    Args:
        sciezka_pliku (str): Ścieżka do pliku

    Returns:
        bool: True jeśli plik jest tekstowy
    """
    rozszerzenia_tekstowe = {
        ".txt",
        ".csv",
        ".json",
        ".xml",
        ".html",
        ".css",
        ".js",
        ".py",
        ".md",
    }
    return sprawdz_rozszerzenie_pliku(sciezka_pliku) in rozszerzenia_tekstowe


def pobierz_rozmiar_pliku(sciezka_pliku: str) -> int:
    """
    Pobiera rozmiar pliku w bajtach.

    Args:
        sciezka_pliku (str): Ścieżka do pliku

    Returns:
        int: Rozmiar pliku w bajtach, -1 jeśli błąd
    """
    try:
        return os.path.getsize(sciezka_pliku)
    except (OSError, IOError):
        return -1


def formatuj_rozmiar(rozmiar_bajty: int) -> str:
    """
    Formatuje rozmiar pliku w czytelnej postaci.

    Args:
        rozmiar_bajty (int): Rozmiar w bajtach

    Returns:
        str: Sformatowany rozmiar (np. "1.5 MB")
    """
    if rozmiar_bajty < 0:
        return "Nieznany"

    jednostki = ["B", "KB", "MB", "GB", "TB"]
    rozmiar = float(rozmiar_bajty)
    jednostka = 0

    while rozmiar >= 1024 and jednostka < len(jednostki) - 1:
        rozmiar /= 1024
        jednostka += 1

    if jednostka == 0:
        return f"{int(rozmiar)} {jednostki[jednostka]}"
    else:
        return f"{rozmiar:.1f} {jednostki[jednostka]}"


def oblicz_oszczednosc(rozmiar_przed: int, rozmiar_po: int) -> float:
    """
    Oblicza procent oszczędności miejsca.

    Args:
        rozmiar_przed (int): Rozmiar przed kompresją
        rozmiar_po (int): Rozmiar po kompresji

    Returns:
        float: Procent oszczędności (0-100)
    """
    if rozmiar_przed <= 0:
        return 0.0

    oszczednosc = ((rozmiar_przed - rozmiar_po) / rozmiar_przed) * 100
    return max(0.0, min(100.0, oszczednosc))  # Ograniczenie 0-100%


def stworz_nazwe_pliku_wynikowego(sciezka_pliku: str, folder_docelowy: str) -> str:
    """
    Tworzy nazwę pliku wynikowego dla kompresji.

    Args:
        sciezka_pliku (str): Ścieżka do pliku źródłowego
        folder_docelowy (str): Folder docelowy

    Returns:
        str: Pełna ścieżka do pliku wynikowego
    """
    nazwa_pliku = os.path.basename(sciezka_pliku)
    nazwa_bez_rozszerzenia = os.path.splitext(nazwa_pliku)[0]
    nazwa_wynikowa = f"{nazwa_bez_rozszerzenia}.zip"

    return os.path.join(folder_docelowy, nazwa_wynikowa)


def sprawdz_uprawnienia_zapisu(folder: str) -> bool:
    """
    Sprawdza czy można zapisywać pliki w danym folderze.

    Args:
        folder (str): Ścieżka do folderu

    Returns:
        bool: True jeśli można zapisywać
    """
    try:
        # Próba utworzenia tymczasowego pliku
        test_plik = os.path.join(folder, f"test_{int(time.time())}.tmp")
        with open(test_plik, "w") as f:
            f.write("test")
        os.remove(test_plik)
        return True
    except (OSError, IOError, PermissionError):
        return False


def pobierz_informacje_o_pliku(sciezka_pliku: str) -> Dict[str, Any]:
    """
    Pobiera szczegółowe informacje o pliku.

    Args:
        sciezka_pliku (str): Ścieżka do pliku

    Returns:
        Dict[str, Any]: Słownik z informacjami o pliku
    """
    try:
        stat = os.stat(sciezka_pliku)
        return {
            "nazwa": os.path.basename(sciezka_pliku),
            "rozmiar": stat.st_size,
            "data_modyfikacji": datetime.fromtimestamp(stat.st_mtime),
            "data_utworzenia": datetime.fromtimestamp(stat.st_ctime),
            "rozszerzenie": sprawdz_rozszerzenie_pliku(sciezka_pliku),
            "czy_tekstowy": czy_plik_tekstowy(sciezka_pliku),
            "sciezka": sciezka_pliku,
        }
    except (OSError, IOError):
        return {
            "nazwa": os.path.basename(sciezka_pliku),
            "rozmiar": -1,
            "data_modyfikacji": None,
            "data_utworzenia": None,
            "rozszerzenie": sprawdz_rozszerzenie_pliku(sciezka_pliku),
            "czy_tekstowy": False,
            "sciezka": sciezka_pliku,
            "blad": True,
        }


def filtruj_pliki_tekstowe(sciezki_plikow: List[str]) -> List[str]:
    """
    Filtruje listę plików, zostawiając tylko pliki tekstowe.

    Args:
        sciezki_plikow (List[str]): Lista ścieżek do plików

    Returns:
        List[str]: Lista ścieżek do plików tekstowych
    """
    return [sciezka for sciezka in sciezki_plikow if czy_plik_tekstowy(sciezka)]


def stworz_raport_kompresji(
    pliki_przed: List[str], pliki_po: List[str]
) -> Dict[str, Any]:
    """
    Tworzy raport z kompresji plików.

    Args:
        pliki_przed (List[str]): Lista plików przed kompresją
        pliki_po (List[str]): Lista plików po kompresji

    Returns:
        Dict[str, Any]: Raport kompresji
    """
    raport = {
        "data": datetime.now(),
        "liczba_plikow": len(pliki_przed),
        "rozmiar_przed": 0,
        "rozmiar_po": 0,
        "oszczednosc_bajty": 0,
        "oszczednosc_procent": 0,
        "pliki": [],
    }

    for plik_przed in pliki_przed:
        plik_po = stworz_nazwe_pliku_wynikowego(plik_przed, "")
        rozmiar_przed = pobierz_rozmiar_pliku(plik_przed)
        rozmiar_po = pobierz_rozmiar_pliku(plik_po) if os.path.exists(plik_po) else 0

        raport["rozmiar_przed"] += rozmiar_przed
        raport["rozmiar_po"] += rozmiar_po

        raport["pliki"].append(
            {
                "nazwa": os.path.basename(plik_przed),
                "rozmiar_przed": rozmiar_przed,
                "rozmiar_po": rozmiar_po,
                "oszczednosc": oblicz_oszczednosc(rozmiar_przed, rozmiar_po),
            }
        )

    raport["oszczednosc_bajty"] = raport["rozmiar_przed"] - raport["rozmiar_po"]
    raport["oszczednosc_procent"] = oblicz_oszczednosc(
        raport["rozmiar_przed"], raport["rozmiar_po"]
    )

    return raport


def zapisz_log_do_pliku(sciezka_pliku: str, logi: List[str]):
    """
    Zapisuje logi do pliku.

    Args:
        sciezka_pliku (str): Ścieżka do pliku logów
        logi (List[str]): Lista logów do zapisania
    """
    try:
        with open(sciezka_pliku, "a", encoding="utf-8") as f:
            for log in logi:
                f.write(f"{datetime.now()}: {log}\n")
    except (OSError, IOError):
        pass  # Ignoruj błędy zapisu logów


def pobierz_wersje_aplikacji() -> str:
    """
    Pobiera wersję aplikacji.

    Returns:
        str: Wersja aplikacji
    """
    return "1.0.0"


def pobierz_informacje_systemowe() -> Dict[str, str]:
    """
    Pobiera podstawowe informacje o systemie.

    Returns:
        Dict[str, str]: Informacje o systemie
    """
    import platform

    return {
        "system": platform.system(),
        "wersja": platform.version(),
        "architektura": platform.machine(),
        "python": platform.python_version(),
        "aplikacja": pobierz_wersje_aplikacji(),
    }
