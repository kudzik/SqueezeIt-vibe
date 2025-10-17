# 📚 Dokumentacja API - SqueezeIt

## 📋 Spis treści
1. [Przegląd API](#przegląd-api)
2. [Moduł core.py](#moduł-corepy)
3. [Moduł gui.py](#moduł-guipy)
4. [Moduł utils.py](#moduł-utilspy)
5. [Przykłady użycia](#przykłady-użycia)
6. [Obsługa błędów](#obsługa-błędów)

---

## Przegląd API

SqueezeIt API składa się z trzech głównych modułów:

- **`core.py`** - Logika kompresji plików
- **`gui.py`** - Interfejs użytkownika
- **`utils.py`** - Funkcje pomocnicze

### Importowanie modułów
```python
from core import KompresorPlikow, formatuj_rozmiar_pliku, oblicz_oszczednosc
from gui import SqueezeItGUI, uruchom_aplikacje
from utils import sprawdz_rozszerzenie_pliku, czy_plik_tekstowy
```

---

## Moduł core.py

### Klasa KompresorPlikow

#### `__init__(sciezka_docelowa: str, poziom_kompresji: int = 6)`
Inicjalizuje kompresor plików.

**Parametry:**
- `sciezka_docelowa` (str): Folder gdzie zapisać skompresowane pliki
- `poziom_kompresji` (int): Poziom kompresji od 1 (najszybszy) do 9 (najlepszy)

**Przykład:**
```python
kompresor = KompresorPlikow("/path/to/output", poziom_kompresji=8)
```

#### `waliduj_pliki(sciezki_plikow: list[str]) -> tuple[list[str], list[str]]`
Sprawdza czy pliki istnieją i są dostępne do kompresji.

**Parametry:**
- `sciezki_plikow` (list[str]): Lista ścieżek do plików

**Zwraca:**
- `tuple[list[str], list[str]]`: (pliki_prawidlowe, pliki_bledne)

**Przykład:**
```python
pliki_ok, pliki_bledne = kompresor.waliduj_pliki(["/path/file1.txt", "/path/file2.txt"])
print(f"Prawidłowe: {len(pliki_ok)}, Błędne: {len(pliki_bledne)}")
```

#### `kompresuj_plik(sciezka_pliku: str) -> tuple[bool, str, str]`
Kompresuje pojedynczy plik tekstowy.

**Parametry:**
- `sciezka_pliku` (str): Ścieżka do pliku do skompresowania

**Zwraca:**
- `tuple[bool, str, str]`: (sukces, sciezka_wyniku, komunikat)

**Przykład:**
```python
sukces, sciezka_wyniku, komunikat = kompresor.kompresuj_plik("/path/file.txt")
if sukces:
    print(f"Plik skompresowany: {sciezka_wyniku}")
else:
    print(f"Błąd: {komunikat}")
```

#### `kompresuj_wiele_plikow(sciezki_plikow: list[str]) -> tuple[int, int, list[str]]`
Kompresuje wiele plików do osobnych archiwów ZIP.

**Parametry:**
- `sciezki_plikow` (list[str]): Lista ścieżek do plików

**Zwraca:**
- `tuple[int, int, list[str]]`: (liczba_sukcesow, liczba_bledow, komunikaty)

**Przykład:**
```python
sukces, bledy, komunikaty = kompresor.kompresuj_wiele_plikow(pliki)
print(f"Sukces: {sukces}, Błędy: {bledy}")
for komunikat in komunikaty:
    print(komunikat)
```

#### `pobierz_statystyki() -> dict`
Zwraca statystyki wykonanych operacji.

**Zwraca:**
- `dict`: Słownik ze statystykami

**Przykład:**
```python
statystyki = kompresor.pobierz_statystyki()
print(f"Liczba operacji: {statystyki['liczba_operacji']}")
print(f"Ostatnia operacja: {statystyki['ostatnia_operacja']}")
```

#### `wyczysc_log()`
Czyści historię operacji.

**Przykład:**
```python
kompresor.wyczysc_log()
```

### Funkcje pomocnicze

#### `formatuj_rozmiar_pliku(rozmiar_bajty: int) -> str`
Formatuje rozmiar pliku w czytelnej postaci.

**Parametry:**
- `rozmiar_bajty` (int): Rozmiar w bajtach

**Zwraca:**
- `str`: Sformatowany rozmiar (np. "1.5 MB")

**Przykład:**
```python
rozmiar = formatuj_rozmiar_pliku(1048576)  # 1 MB
print(rozmiar)  # "1.0 MB"
```

#### `oblicz_oszczednosc(rozmiar_przed: int, rozmiar_po: int) -> float`
Oblicza procent oszczędności miejsca.

**Parametry:**
- `rozmiar_przed` (int): Rozmiar przed kompresją
- `rozmiar_po` (int): Rozmiar po kompresji

**Zwraca:**
- `float`: Procent oszczędności (0-100)

**Przykład:**
```python
oszczednosc = oblicz_oszczednosc(1000000, 500000)  # 50% oszczędności
print(f"Oszczędność: {oszczednosc:.1f}%")
```

---

## Moduł gui.py

### Klasa SqueezeItGUI

#### `__init__()`
Inicjalizuje interfejs użytkownika.

**Przykład:**
```python
app = SqueezeItGUI()
```

#### `stworz_glowne_okno() -> sg.Window`
Tworzy główne okno aplikacji.

**Zwraca:**
- `sg.Window`: Główne okno aplikacji

**Przykład:**
```python
window = app.stworz_glowne_okno()
```

#### `aktualizuj_poziom_kompresji(poziom: int)`
Aktualizuje wyświetlany poziom kompresji.

**Parametry:**
- `poziom` (int): Nowy poziom kompresji

**Przykład:**
```python
app.aktualizuj_poziom_kompresji(8)
```

#### `dodaj_komunikat(komunikat: str)`
Dodaje komunikat do obszaru wyników.

**Parametry:**
- `komunikat` (str): Komunikat do wyświetlenia

**Przykład:**
```python
app.dodaj_komunikat("Kompresja zakończona pomyślnie!")
```

#### `wyczysc_wyniki()`
Czyści obszar wyników.

**Przykład:**
```python
app.wyczysc_wyniki()
```

#### `pokaz_okno_statystyk(statystyki: dict)`
Wyświetla okno ze statystykami.

**Parametry:**
- `statystyki` (dict): Słownik ze statystykami

**Przykład:**
```python
statystyki = {"liczba_operacji": 5, "ostatnia_operacja": "Kompresja pliku.txt"}
app.pokaz_okno_statystyk(statystyki)
```

#### `pokaz_okno_wynikow(sukces: int, bledy: int, komunikaty: list[str])`
Wyświetla okno z wynikami kompresji.

**Parametry:**
- `sukces` (int): Liczba pomyślnie skompresowanych plików
- `bledy` (int): Liczba błędów
- `komunikaty` (list[str]): Lista komunikatów

**Przykład:**
```python
app.pokaz_okno_wynikow(3, 1, ["✅ file1.txt", "❌ file2.txt"])
```

#### `uruchom_aplikacje()`
Uruchamia główną pętlę aplikacji.

**Przykład:**
```python
app.uruchom_aplikacje()
```

### Funkcja pomocnicza

#### `uruchom_aplikacje()`
Funkcja pomocnicza do uruchomienia aplikacji.

**Przykład:**
```python
from gui import uruchom_aplikacje
uruchom_aplikacje()
```

---

## Moduł utils.py

### Funkcje operacji na plikach

#### `sprawdz_rozszerzenie_pliku(sciezka_pliku: str) -> str`
Sprawdza rozszerzenie pliku.

**Parametry:**
- `sciezka_pliku` (str): Ścieżka do pliku

**Zwraca:**
- `str`: Rozszerzenie pliku (np. '.txt', '.csv')

**Przykład:**
```python
rozszerzenie = sprawdz_rozszerzenie_pliku("/path/file.txt")
print(rozszerzenie)  # ".txt"
```

#### `czy_plik_tekstowy(sciezka_pliku: str) -> bool`
Sprawdza czy plik to plik tekstowy na podstawie rozszerzenia.

**Parametry:**
- `sciezka_pliku` (str): Ścieżka do pliku

**Zwraca:**
- `bool`: True jeśli plik jest tekstowy

**Przykład:**
```python
if czy_plik_tekstowy("/path/file.txt"):
    print("To jest plik tekstowy")
```

#### `pobierz_rozmiar_pliku(sciezka_pliku: str) -> int`
Pobiera rozmiar pliku w bajtach.

**Parametry:**
- `sciezka_pliku` (str): Ścieżka do pliku

**Zwraca:**
- `int`: Rozmiar pliku w bajtach, -1 jeśli błąd

**Przykład:**
```python
rozmiar = pobierz_rozmiar_pliku("/path/file.txt")
print(f"Rozmiar: {rozmiar} bajtów")
```

#### `formatuj_rozmiar(rozmiar_bajty: int) -> str`
Formatuje rozmiar pliku w czytelnej postaci.

**Parametry:**
- `rozmiar_bajty` (int): Rozmiar w bajtach

**Zwraca:**
- `str`: Sformatowany rozmiar (np. "1.5 MB")

**Przykład:**
```python
rozmiar = formatuj_rozmiar(1048576)  # 1 MB
print(rozmiar)  # "1.0 MB"
```

#### `oblicz_oszczednosc(rozmiar_przed: int, rozmiar_po: int) -> float`
Oblicza procent oszczędności miejsca.

**Parametry:**
- `rozmiar_przed` (int): Rozmiar przed kompresją
- `rozmiar_po` (int): Rozmiar po kompresji

**Zwraca:**
- `float`: Procent oszczędności (0-100)

**Przykład:**
```python
oszczednosc = oblicz_oszczednosc(1000000, 500000)
print(f"Oszczędność: {oszczednosc:.1f}%")  # 50.0%
```

### Funkcje systemowe

#### `sprawdz_uprawnienia_zapisu(folder: str) -> bool`
Sprawdza czy można zapisywać pliki w danym folderze.

**Parametry:**
- `folder` (str): Ścieżka do folderu

**Zwraca:**
- `bool`: True jeśli można zapisywać

**Przykład:**
```python
if sprawdz_uprawnienia_zapisu("/path/to/folder"):
    print("Można zapisywać pliki")
else:
    print("Brak uprawnień do zapisu")
```

#### `pobierz_informacje_o_pliku(sciezka_pliku: str) -> dict[str, Any]`
Pobiera szczegółowe informacje o pliku.

**Parametry:**
- `sciezka_pliku` (str): Ścieżka do pliku

**Zwraca:**
- `dict[str, Any]`: Słownik z informacjami o pliku

**Przykład:**
```python
info = pobierz_informacje_o_pliku("/path/file.txt")
print(f"Nazwa: {info['nazwa']}")
print(f"Rozmiar: {info['rozmiar']} bajtów")
print(f"Czy tekstowy: {info['czy_tekstowy']}")
```

#### `filtruj_pliki_tekstowe(sciezki_plikow: list[str]) -> list[str]`
Filtruje listę plików, zostawiając tylko pliki tekstowe.

**Parametry:**
- `sciezki_plikow` (list[str]): Lista ścieżek do plików

**Zwraca:**
- `list[str]`: Lista ścieżek do plików tekstowych

**Przykład:**
```python
pliki = ["/path/file1.txt", "/path/file2.jpg", "/path/file3.py"]
pliki_tekstowe = filtruj_pliki_tekstowe(pliki)
print(pliki_tekstowe)  # ["/path/file1.txt", "/path/file3.py"]
```

### Funkcje raportowania

#### `stworz_raport_kompresji(pliki_przed: list[str], pliki_po: list[str]) -> dict[str, Any]`
Tworzy raport z kompresji plików.

**Parametry:**
- `pliki_przed` (list[str]): Lista plików przed kompresją
- `pliki_po` (list[str]): Lista plików po kompresji

**Zwraca:**
- `dict[str, Any]`: Raport kompresji

**Przykład:**
```python
raport = stworz_raport_kompresji(pliki_przed, pliki_po)
print(f"Oszczędność: {raport['oszczednosc_procent']:.1f}%")
```

#### `zapisz_log_do_pliku(sciezka_pliku: str, logi: list[str])`
Zapisuje logi do pliku.

**Parametry:**
- `sciezka_pliku` (str): Ścieżka do pliku logów
- `logi` (list[str]): Lista logów do zapisania

**Przykład:**
```python
logi = ["Kompresja rozpoczęta", "Plik skompresowany", "Kompresja zakończona"]
zapisz_log_do_pliku("squeezeit.log", logi)
```

### Funkcje informacyjne

#### `pobierz_wersje_aplikacji() -> str`
Pobiera wersję aplikacji.

**Zwraca:**
- `str`: Wersja aplikacji

**Przykład:**
```python
wersja = pobierz_wersje_aplikacji()
print(f"Wersja: {wersja}")  # "1.0.0"
```

#### `pobierz_informacje_systemowe() -> dict[str, str]`
Pobiera podstawowe informacje o systemie.

**Zwraca:**
- `dict[str, str]`: Informacje o systemie

**Przykład:**
```python
info = pobierz_informacje_systemowe()
print(f"System: {info['system']}")
print(f"Python: {info['python']}")
```

---

## Przykłady użycia

### Podstawowe użycie kompresora
```python
from core import KompresorPlikow

# Stwórz kompresor
kompresor = KompresorPlikow("/path/to/output", poziom_kompresji=8)

# Kompresuj pojedynczy plik
sukces, sciezka_wyniku, komunikat = kompresor.kompresuj_plik("/path/file.txt")
if sukces:
    print(f"Plik skompresowany: {sciezka_wyniku}")
else:
    print(f"Błąd: {komunikat}")

# Kompresuj wiele plików
pliki = ["/path/file1.txt", "/path/file2.txt"]
sukces, bledy, komunikaty = kompresor.kompresuj_wiele_plikow(pliki)
print(f"Sukces: {sukces}, Błędy: {bledy}")
```

### Uruchomienie GUI
```python
from gui import uruchom_aplikacje

# Uruchom aplikację GUI
uruchom_aplikacje()
```

### Użycie funkcji pomocniczych
```python
from utils import sprawdz_rozszerzenie_pliku, czy_plik_tekstowy, formatuj_rozmiar

# Sprawdź typ pliku
sciezka = "/path/file.txt"
if czy_plik_tekstowy(sciezka):
    rozszerzenie = sprawdz_rozszerzenie_pliku(sciezka)
    print(f"Plik tekstowy z rozszerzeniem: {rozszerzenie}")

# Formatuj rozmiar
rozmiar = formatuj_rozmiar(1048576)  # 1 MB
print(f"Rozmiar: {rozmiar}")
```

---

## Obsługa błędów

### Typowe wyjątki
```python
try:
    kompresor = KompresorPlikow("/path/to/output")
    sukces, sciezka_wyniku, komunikat = kompresor.kompresuj_plik("/path/file.txt")
except FileNotFoundError:
    print("Plik nie został znaleziony")
except PermissionError:
    print("Brak uprawnień do pliku")
except Exception as e:
    print(f"Nieoczekiwany błąd: {e}")
```

### Walidacja danych wejściowych
```python
from core import KompresorPlikow

kompresor = KompresorPlikow("/path/to/output")

# Sprawdź pliki przed kompresją
pliki_ok, pliki_bledne = kompresor.waliduj_pliki(["/path/file1.txt", "/path/file2.txt"])

if pliki_bledne:
    print("Błędy w plikach:")
    for blad in pliki_bledne:
        print(f"  - {blad}")

if pliki_ok:
    sukces, bledy, komunikaty = kompresor.kompresuj_wiele_plikow(pliki_ok)
    print(f"Kompresja zakończona: {sukces} sukcesów, {bledy} błędów")
```

### Logowanie błędów
```python
import logging

# Skonfiguruj logowanie
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('squeezeit.log'),
        logging.StreamHandler()
    ]
)

try:
    # Kod który może się nie powieść
    kompresor.kompresuj_plik("/path/file.txt")
except Exception as e:
    logging.error(f"Błąd kompresji: {e}")
```

---

**Dokumentacja API v1.0 - SqueezeIt Kompresor Plików**  
*Ostatnia aktualizacja: 2024*
