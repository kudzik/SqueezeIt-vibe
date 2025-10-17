# 🐍 Kurs Python od Podstaw - SqueezeIt Edition

## Spis treści
1. [Wprowadzenie do Pythona](#wprowadzenie-do-pythona)
2. [Podstawowe typy danych](#podstawowe-typy-danych)
3. [Zmienne i operatory](#zmienne-i-operatory)
4. [Struktury kontrolne](#struktury-kontrolne)
5. [Funkcje](#funkcje)
6. [Klasy i obiekty](#klasy-i-obiekty)
7. [Obsługa plików](#obsługa-plików)
8. [Biblioteki i moduły](#biblioteki-i-moduły)
9. [GUI z FreeSimpleGUI](#gui-z-freesimplegui)
10. [Praktyczne przykłady z SqueezeIt](#praktyczne-przykłady-z-squeezeit)

---

## Wprowadzenie do Pythona

### Co to jest Python?
Python to język programowania wysokiego poziomu, który jest:
- **Łatwy do nauki** - czytelna składnia
- **Uniwersalny** - web, desktop, data science, AI
- **Darmowy** - open source
- **Popularny** - używany przez Google, Netflix, Instagram

### Pierwszy program
```python
# To jest komentarz w Pythonie
print("Witaj w Pythonie!")  # Wyświetla tekst na ekranie
```

### Instalacja i uruchamianie
```bash
# Sprawdź wersję Pythona
python --version

# Uruchom plik Python
python main.py
```

---

## Podstawowe typy danych

### 1. Liczby
```python
# Liczby całkowite (int)
wiek = 25
print(type(wiek))  # <class 'int'>

# Liczby zmiennoprzecinkowe (float)
wzrost = 1.75
print(type(wzrost))  # <class 'float'>
```

### 2. Tekst (string)
```python
# Pojedyncze cudzysłowy
imie = 'Jan'
print(imie)

# Podwójne cudzysłowy
nazwisko = "Kowalski"
print(nazwisko)

# F-string (nowoczesny sposób)
pelne_imie = f"{imie} {nazwisko}"
print(pelne_imie)  # Jan Kowalski
```

### 3. Wartości logiczne (bool)
```python
# True i False (z dużej litery!)
czy_pelnoletni = True
czy_dziecko = False

print(czy_pelnoletni)  # True
print(not czy_pelnoletni)  # False
```

### 4. Listy
```python
# Lista liczb
liczby = [1, 2, 3, 4, 5]
print(liczby[0])  # 1 (pierwszy element)

# Lista tekstów
kolory = ["czerwony", "zielony", "niebieski"]
print(kolory[-1])  # niebieski (ostatni element)

# Dodawanie do listy
kolory.append("żółty")
print(kolory)  # ['czerwony', 'zielony', 'niebieski', 'żółty']
```

---

## Zmienne i operatory

### Zmienne
```python
# Nazwy zmiennych - małe litery, podkreślenia
nazwa_pliku = "dokument.txt"
rozmiar_pliku = 1024
czy_istnieje = True

# Konwencje nazewnictwa
# ✅ DOBRE: user_name, file_size, is_valid
# ❌ ZŁE: userName, FileSize, IS_VALID
```

### Operatory arytmetyczne
```python
a = 10
b = 3

print(a + b)  # 13 (dodawanie)
print(a - b)  # 7 (odejmowanie)
print(a * b)  # 30 (mnożenie)
print(a / b)  # 3.333... (dzielenie)
print(a // b)  # 3 (dzielenie całkowite)
print(a % b)  # 1 (reszta z dzielenia)
print(a ** b)  # 1000 (potęgowanie)
```

### Operatory porównania
```python
x = 5
y = 10

print(x == y)  # False (równe)
print(x != y)  # True (różne)
print(x < y)   # True (mniejsze)
print(x > y)   # False (większe)
print(x <= y)  # True (mniejsze lub równe)
print(x >= y)  # False (większe lub równe)
```

---

## Struktury kontrolne

### 1. Instrukcja if
```python
wiek = 18

if wiek >= 18:
    print("Jesteś pełnoletni")
elif wiek >= 13:
    print("Jesteś nastolatkiem")
else:
    print("Jesteś dzieckiem")
```

### 2. Pętla for
```python
# Iteracja przez listę
owoce = ["jabłko", "banan", "pomarańcza"]
for owoc in owoce:
    print(f"Lubię {owoc}")

# Iteracja przez zakres liczb
for i in range(5):  # 0, 1, 2, 3, 4
    print(f"Liczba: {i}")
```

### 3. Pętla while
```python
licznik = 0
while licznik < 3:
    print(f"Licznik: {licznik}")
    licznik += 1  # Zwiększ licznik o 1
```

---

## Funkcje

### Definiowanie funkcji
```python
def powitanie(imie):
    """Funkcja wyświetla powitanie dla podanego imienia"""
    return f"Cześć {imie}!"

# Wywołanie funkcji
wynik = powitanie("Anna")
print(wynik)  # Cześć Anna!
```

### Funkcje z parametrami
```python
def dodaj(a, b):
    """Dodaje dwie liczby"""
    return a + b

def oblicz_pole_kola(promien):
    """Oblicza pole koła"""
    pi = 3.14159
    return pi * promien ** 2

# Użycie funkcji
suma = dodaj(5, 3)
pole = oblicz_pole_kola(5)
print(f"Suma: {suma}, Pole: {pole}")
```

### Funkcje z wartościami domyślnymi
```python
def powitanie(imie="Gość"):
    """Powitanie z domyślnym imieniem"""
    return f"Cześć {imie}!"

print(powitanie())        # Cześć Gość!
print(powitanie("Jan"))   # Cześć Jan!
```

---

## Klasy i obiekty

### Definiowanie klasy
```python
class Osoba:
    """Klasa reprezentująca osobę"""
    
    def __init__(self, imie, wiek):
        """Konstruktor - tworzy nową osobę"""
        self.imie = imie
        self.wiek = wiek
    
    def przedstaw_sie(self):
        """Metoda przedstawiająca osobę"""
        return f"Jestem {self.imie} i mam {self.wiek} lat"
    
    def czy_pelnoletni(self):
        """Sprawdza czy osoba jest pełnoletnia"""
        return self.wiek >= 18

# Tworzenie obiektu
osoba = Osoba("Anna", 25)
print(osoba.przedstaw_sie())  # Jestem Anna i mam 25 lat
print(osoba.czy_pelnoletni())  # True
```

---

## Obsługa plików

### Czytanie pliku
```python
# Czytanie całego pliku
with open("plik.txt", "r", encoding="utf-8") as plik:
    zawartosc = plik.read()
    print(zawartosc)

# Czytanie linia po linii
with open("plik.txt", "r", encoding="utf-8") as plik:
    for linia in plik:
        print(linia.strip())  # strip() usuwa znaki nowej linii
```

### Zapisywanie do pliku
```python
# Zapisywanie tekstu
with open("nowy_plik.txt", "w", encoding="utf-8") as plik:
    plik.write("To jest nowy plik\n")
    plik.write("Druga linia\n")

# Dodawanie do istniejącego pliku
with open("plik.txt", "a", encoding="utf-8") as plik:
    plik.write("Dodana linia\n")
```

### Sprawdzanie czy plik istnieje
```python
import os

if os.path.exists("plik.txt"):
    print("Plik istnieje")
else:
    print("Plik nie istnieje")
```

---

## Biblioteki i moduły

### Importowanie modułów
```python
# Import całego modułu
import math
print(math.pi)  # 3.141592653589793

# Import konkretnej funkcji
from math import sqrt
print(sqrt(16))  # 4.0

# Import z aliasem
import datetime as dt
teraz = dt.datetime.now()
print(teraz)
```

### Tworzenie własnych modułów
```python
# plik: utils.py
def formatuj_date(data):
    """Formatuje datę do czytelnej postaci"""
    return data.strftime("%d.%m.%Y")

# plik: main.py
from utils import formatuj_date
import datetime

dzisiaj = datetime.datetime.now()
print(formatuj_date(dzisiaj))  # 15.12.2024
```

---

## GUI z FreeSimpleGUI

### Podstawy FreeSimpleGUI
```python
import FreeSimpleGUI as sg

# Tworzenie elementów GUI
layout = [
    [sg.Text("Witaj w aplikacji!")],
    [sg.Input(key="input_tekst")],
    [sg.Button("OK"), sg.Button("Anuluj")]
]

# Tworzenie okna
window = sg.Window("Moja aplikacja", layout)

# Pętla zdarzeń
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "OK":
        print(f"Wpisano: {values['input_tekst']}")

window.close()
```

### Elementy GUI w SqueezeIt
```python
# Przyciski
sg.Button("Kompresuj", key="btn_kompresuj")

# Pola tekstowe
sg.Input(key="input_pliki", size=(40, 1))

# Slider
sg.Slider(range=(1, 9), default_value=6, key="slider_kompresja")

# Obszar tekstu
sg.Multiline(key="output_wyniki", size=(60, 8))
```

---

## Praktyczne przykłady z SqueezeIt

### 1. Klasa KompresorPlikow
```python
class KompresorPlikow:
    def __init__(self, sciezka_docelowa: str, poziom_kompresji: int = 6):
        self.sciezka_docelowa = sciezka_docelowa
        self.poziom_kompresji = min(max(poziom_kompresji, 1), 9)
        self.log_operacji = []
    
    def kompresuj_plik(self, sciezka_pliku: str) -> tuple[bool, str, str]:
        """Kompresuje pojedynczy plik"""
        try:
            # Logika kompresji...
            return True, sciezka_wyniku, "Sukces"
        except Exception as e:
            return False, "", f"Błąd: {e}"
```

### 2. Obsługa zdarzeń GUI
```python
def uruchom_aplikacje(self):
    while True:
        event, values = self.window.read()
        
        if event == sg.WIN_CLOSED:
            break
        elif event == "btn_kompresuj":
            self.obsluz_kompresje(values)
        elif event == "slider_kompresja":
            poziom = int(values["slider_kompresja"])
            self.aktualizuj_poziom_kompresji(poziom)
```

### 3. Walidacja plików
```python
def waliduj_pliki(self, sciezki_plikow: list[str]) -> tuple[list[str], list[str]]:
    pliki_prawidlowe = []
    pliki_bledne = []
    
    for sciezka in sciezki_plikow:
        if os.path.exists(sciezka) and os.path.isfile(sciezka):
            try:
                with open(sciezka, "rb") as f:
                    f.read(1)  # Test odczytu
                pliki_prawidlowe.append(sciezka)
            except (PermissionError, IOError):
                pliki_bledne.append(f"{sciezka} - brak uprawnień")
        else:
            pliki_bledne.append(f"{sciezka} - plik nie istnieje")
    
    return pliki_prawidlowe, pliki_bledne
```

### 4. Obsługa błędów
```python
try:
    # Niebezpieczny kod
    wynik = operacja_ktora_moze_sie_nie_powiesc()
except FileNotFoundError:
    print("Plik nie został znaleziony")
except PermissionError:
    print("Brak uprawnień do pliku")
except Exception as e:
    print(f"Nieoczekiwany błąd: {e}")
finally:
    print("To się zawsze wykona")
```

---

## 🎯 Podsumowanie

### Kluczowe koncepcje w SqueezeIt:
1. **Klasy** - `KompresorPlikow`, `SqueezeItGUI`
2. **Funkcje** - `kompresuj_plik()`, `waliduj_pliki()`
3. **GUI** - FreeSimpleGUI, obsługa zdarzeń
4. **Obsługa plików** - `open()`, `zipfile`, `os.path`
5. **Obsługa błędów** - `try/except/finally`
6. **Moduły** - `main.py`, `gui.py`, `core.py`, `utils.py`

### Następne kroki:
- Praktykuj z prostymi programami
- Eksperymentuj z różnymi typami danych
- Twórz własne funkcje i klasy
- Czytaj dokumentację Python

### Przydatne zasoby:
- [Python.org](https://python.org) - oficjalna dokumentacja
- [Real Python](https://realpython.com) - tutoriale i artykuły
- [Python Tutor](https://pythontutor.com) - wizualizacja kodu
- [FreeSimpleGUI Docs](https://pysimplegui.readthedocs.io/) - dokumentacja GUI

**Powodzenia w nauce Pythona! 🚀**