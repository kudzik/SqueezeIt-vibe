# 🎯 Ćwiczenia Python - SqueezeIt Project

## 📚 Wprowadzenie

Ten plik zawiera praktyczne ćwiczenia do wykonania po przeczytaniu kursu Python. Ćwiczenia są podzielone na poziomy trudności i bezpośrednio związane z projektem SqueezeIt.

## 🏗️ Poziom 1: Podstawy (Dla początkujących)

### Ćwiczenie 1.1: Zmienne i typy danych
**Cel:** Zrozumienie podstawowych typów danych w Pythonie

```python
# Zadanie: Stwórz zmienne dla kompresora plików
nazwa_pliku = "dokument.txt"
rozmiar_pliku = 1024  # w bajtach
czy_skompresowany = False
lista_plikow = ["plik1.txt", "plik2.txt", "plik3.txt"]

# Wyświetl informacje o pliku
print(f"Nazwa: {nazwa_pliku}")
print(f"Rozmiar: {rozmiar_pliku} bajtów")
print(f"Skompresowany: {czy_skompresowany}")
```

**Pytania do przemyślenia:**
- Jaki typ danych ma każda zmienna?
- Jak zmienić `czy_skompresowany` na `True`?
- Jak dodać nowy plik do `lista_plikow`?

### Ćwiczenie 1.2: Funkcje podstawowe
**Cel:** Nauka tworzenia i wywoływania funkcji

```python
# Zadanie: Stwórz funkcję do obliczania rozmiaru pliku
def oblicz_rozmiar_mb(rozmiar_bajty):
    """Konwertuje rozmiar z bajtów na megabajty"""
    return rozmiar_bajty / (1024 * 1024)

# Przetestuj funkcję
rozmiar = 1048576  # 1 MB w bajtach
print(f"Rozmiar: {oblicz_rozmiar_mb(rozmiar):.2f} MB")
```

**Zadanie dodatkowe:**
- Stwórz funkcję `formatuj_rozmiar(rozmiar_bajty)` która zwraca ładnie sformatowany rozmiar (np. "1.5 MB", "500 KB")

### Ćwiczenie 1.3: Pętle i warunki
**Cel:** Praktyka z kontrolą przepływu programu

```python
# Zadanie: Sprawdź które pliki są większe niż 1MB
pliki = [
    ("dokument.txt", 500000),    # 500 KB
    ("obraz.jpg", 2500000),      # 2.5 MB
    ("muzyka.mp3", 800000),      # 800 KB
    ("film.mp4", 150000000)      # 150 MB
]

for nazwa, rozmiar in pliki:
    if rozmiar > 1000000:  # 1 MB
        print(f"{nazwa}: {rozmiar/1000000:.1f} MB - DUŻY PLIK")
    else:
        print(f"{nazwa}: {rozmiar/1000:.1f} KB - mały plik")
```

---

## 🚀 Poziom 2: Średnio zaawansowany

### Ćwiczenie 2.1: Obsługa plików
**Cel:** Nauka pracy z plikami w Pythonie

```python
# Zadanie: Stwórz funkcję do sprawdzania czy plik istnieje
import os

def sprawdz_plik(sciezka):
    """Sprawdza czy plik istnieje i zwraca informacje o nim"""
    if os.path.exists(sciezka):
        rozmiar = os.path.getsize(sciezka)
        return True, rozmiar
    else:
        return False, 0

# Przetestuj funkcję
istnieje, rozmiar = sprawdz_plik("main.py")
if istnieje:
    print(f"Plik istnieje, rozmiar: {rozmiar} bajtów")
else:
    print("Plik nie istnieje")
```

**Zadanie dodatkowe:**
- Stwórz funkcję `lista_plikow_w_folderze(folder)` która zwraca listę wszystkich plików w folderze

### Ćwiczenie 2.2: Klasy i obiekty
**Cel:** Zrozumienie programowania obiektowego

```python
# Zadanie: Stwórz klasę Plik
class Plik:
    def __init__(self, sciezka):
        self.sciezka = sciezka
        self.nazwa = os.path.basename(sciezka)
        self.rozmiar = os.path.getsize(sciezka) if os.path.exists(sciezka) else 0
    
    def czy_istnieje(self):
        return os.path.exists(self.sciezka)
    
    def rozmiar_mb(self):
        return self.rozmiar / (1024 * 1024)
    
    def __str__(self):
        return f"Plik: {self.nazwa}, Rozmiar: {self.rozmiar_mb():.2f} MB"

# Użyj klasy
plik = Plik("main.py")
print(plik)
```

### Ćwiczenie 2.3: Obsługa błędów
**Cel:** Nauka obsługi wyjątków

```python
# Zadanie: Stwórz bezpieczną funkcję do czytania pliku
def bezpieczne_czytanie_pliku(sciezka):
    """Bezpiecznie czyta plik z obsługą błędów"""
    try:
        with open(sciezka, 'r', encoding='utf-8') as plik:
            zawartosc = plik.read()
            return True, zawartosc
    except FileNotFoundError:
        return False, "Plik nie został znaleziony"
    except PermissionError:
        return False, "Brak uprawnień do pliku"
    except Exception as e:
        return False, f"Nieoczekiwany błąd: {e}"

# Przetestuj funkcję
sukces, wynik = bezpieczne_czytanie_pliku("nieistniejacy_plik.txt")
if sukces:
    print("Plik został odczytany")
else:
    print(f"Błąd: {wynik}")
```

---

## 🎯 Poziom 3: Zaawansowany

### Ćwiczenie 3.1: Kompresja plików
**Cel:** Implementacja podstawowej kompresji

```python
# Zadanie: Stwórz prosty kompresor tekstu
import zipfile
import os

def kompresuj_plik(sciezka_wejscie, sciezka_wyjscie):
    """Kompresuje plik tekstowy"""
    try:
        with zipfile.ZipFile(sciezka_wyjscie, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(sciezka_wejscie, os.path.basename(sciezka_wejscie))
        return True, "Kompresja zakończona pomyślnie"
    except Exception as e:
        return False, f"Błąd kompresji: {e}"

# Przetestuj kompresję
sukces, komunikat = kompresuj_plik("test.txt", "test.zip")
print(komunikat)
```

### Ćwiczenie 3.2: GUI z FreeSimpleGUI
**Cel:** Rozszerzenie interfejsu użytkownika

```python
# Zadanie: Stwórz prosty GUI
import FreeSimpleGUI as sg

def stworz_proste_gui():
    """Tworzy prosty interfejs użytkownika"""
    layout = [
        [sg.Text("SqueezeIt - Kompresor Plików", font=("Arial", 16))],
        [sg.Text("Plik do kompresji:")],
        [sg.Input(key="plik"), sg.FileBrowse("Wybierz plik")],
        [sg.Text("Folder docelowy:")],
        [sg.Input(key="folder"), sg.FolderBrowse("Wybierz folder")],
        [sg.Button("Kompresuj"), sg.Button("Anuluj")],
        [sg.Output(size=(50, 10), key="output")]
    ]
    return sg.Window("SqueezeIt", layout)

# Użyj funkcji
window = stworz_proste_gui()
```

### Ćwiczenie 3.3: Logowanie i monitoring
**Cel:** Dodanie systemu logowania

```python
# Zadanie: Stwórz system logowania operacji
import logging
from datetime import datetime

def skonfiguruj_logowanie():
    """Konfiguruje system logowania"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('squeezeit.log'),
            logging.StreamHandler()
        ]
    )

def loguj_operacje(operacja, plik, sukces):
    """Loguje operacje kompresji"""
    status = "SUKCES" if sukces else "BŁĄD"
    logging.info(f"{operacja} - {plik} - {status}")

# Użyj systemu logowania
skonfiguruj_logowanie()
loguj_operacje("KOMPRESJA", "test.txt", True)
```

---

## 🏆 Poziom 4: Ekspert

### Ćwiczenie 4.1: Optymalizacja wydajności
**Cel:** Poprawa wydajności aplikacji

```python
# Zadanie: Stwórz wielowątkowy kompresor
import threading
import queue
from concurrent.futures import ThreadPoolExecutor

class WielowatkowyKompresor:
    def __init__(self, max_watkow=4):
        self.max_watkow = max_watkow
        self.kolejka = queue.Queue()
    
    def kompresuj_plik(self, sciezka):
        """Kompresuje pojedynczy plik"""
        # Implementacja kompresji...
        pass
    
    def kompresuj_wszystkie(self, lista_plikow):
        """Kompresuje wiele plików równolegle"""
        with ThreadPoolExecutor(max_workers=self.max_watkow) as executor:
            futures = [executor.submit(self.kompresuj_plik, plik) for plik in lista_plikow]
            return [future.result() for future in futures]
```

### Ćwiczenie 4.2: Testy jednostkowe
**Cel:** Napisanie testów dla aplikacji

```python
# Zadanie: Stwórz testy dla funkcji kompresji
import unittest
import tempfile
import os

class TestKompresor(unittest.TestCase):
    def setUp(self):
        """Przygotowanie do testów"""
        self.temp_dir = tempfile.mkdtemp()
        self.test_file = os.path.join(self.temp_dir, "test.txt")
        
        # Stwórz testowy plik
        with open(self.test_file, 'w') as f:
            f.write("To jest testowy plik")
    
    def test_kompresja_pliku(self):
        """Test kompresji pliku"""
        # Implementuj test...
        pass
    
    def tearDown(self):
        """Sprzątanie po testach"""
        import shutil
        shutil.rmtree(self.temp_dir)

# Uruchom testy
if __name__ == '__main__':
    unittest.main()
```

---

## 📝 Zadania do wykonania

### 🎯 Zadanie 1: Podstawy
- [ ] Stwórz zmienne dla 5 różnych plików
- [ ] Napisz funkcję do obliczania rozmiaru pliku w MB
- [ ] Stwórz pętlę która wyświetli wszystkie pliki większe niż 1MB

### 🎯 Zadanie 2: Funkcje
- [ ] Napisz funkcję `sprawdz_plik(sciezka)` która zwraca informacje o pliku
- [ ] Stwórz funkcję `lista_plikow(folder)` która zwraca listę plików w folderze
- [ ] Napisz funkcję `formatuj_rozmiar(bajty)` która ładnie formatuje rozmiar

### 🎯 Zadanie 3: Klasy
- [ ] Stwórz klasę `Plik` z metodami do sprawdzania istnienia i rozmiaru
- [ ] Dodaj metodę `__str__` do klasy Plik
- [ ] Stwórz klasę `Kompresor` z metodą `kompresuj`

### 🎯 Zadanie 4: GUI
- [ ] Dodaj nowe elementy do interfejsu (slider, output, progress bar)
- [ ] Zaimplementuj obsługę nowych zdarzeń
- [ ] Dodaj walidację danych wejściowych

### 🎯 Zadanie 5: Zaawansowane
- [ ] Zaimplementuj rzeczywistą kompresję plików
- [ ] Dodaj system logowania operacji
- [ ] Stwórz testy jednostkowe dla głównych funkcji

---

## 🎓 Wskazówki do nauki

### Jak podejść do ćwiczeń:
1. **Czytaj kod** - zrozum co robi każda linia
2. **Eksperymentuj** - zmieniaj wartości i obserwuj wyniki
3. **Debuguj** - używaj `print()` do śledzenia wykonania
4. **Dokumentuj** - dodawaj komentarze do swojego kodu
5. **Testuj** - sprawdzaj różne scenariusze

### Przydatne narzędzia:
- **IDE** - PyCharm, VS Code, lub inny edytor z podświetlaniem składni
- **Debugger** - do śledzenia wykonania kodu
- **Terminal** - do uruchamiania programów
- **Git** - do wersjonowania kodu

### Gdzie szukać pomocy:
- **Dokumentacja Python** - [docs.python.org](https://docs.python.org)
- **Stack Overflow** - pytania i odpowiedzi
- **Real Python** - tutoriale i artykuły
- **Python Tutor** - wizualizacja kodu

---

## 🔧 Praktyczne projekty do wykonania

### Projekt 1: Prosty kalkulator
```python
# Stwórz kalkulator z GUI
def kalkulator():
    layout = [
        [sg.Text("Kalkulator", font=("Arial", 16))],
        [sg.Input(key="wynik", size=(20, 1))],
        [sg.Button("1"), sg.Button("2"), sg.Button("3"), sg.Button("+")],
        [sg.Button("4"), sg.Button("5"), sg.Button("6"), sg.Button("-")],
        [sg.Button("7"), sg.Button("8"), sg.Button("9"), sg.Button("*")],
        [sg.Button("0"), sg.Button("="), sg.Button("C"), sg.Button("/")]
    ]
    # Implementuj logikę kalkulatora...
```

### Projekt 2: Menedżer plików
```python
# Stwórz prosty menedżer plików
def menedzer_plikow():
    layout = [
        [sg.Text("Menedżer Plików")],
        [sg.Listbox(values=[], size=(40, 10), key="lista_plikow")],
        [sg.Button("Odśwież"), sg.Button("Usuń"), sg.Button("Kopiuj")]
    ]
    # Implementuj funkcjonalność...
```

### Projekt 3: Notatnik
```python
# Stwórz prosty notatnik
def notatnik():
    layout = [
        [sg.Text("Notatnik")],
        [sg.Multiline(size=(50, 20), key="tekst")],
        [sg.Button("Zapisz"), sg.Button("Otwórz"), sg.Button("Nowy")]
    ]
    # Implementuj funkcjonalność...
```

---

**Powodzenia w nauce! 🚀**

*Pamiętaj: programowanie to praktyka - im więcej kodujesz, tym lepiej rozumiesz!*