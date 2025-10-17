# 🐍 Kurs Python od Podstaw

## Spis treści
1. [Wprowadzenie do Pythona](#wprowadzenie-do-pythona)
2. [Podstawowe typy danych](#podstawowe-typy-danych)
3. [Zmienne i operatory](#zmienne-i-operatory)
4. [Struktury kontrolne](#struktury-kontrolne)
5. [Funkcje](#funkcje)
6. [Klasy i obiekty](#klasy-i-obiekty)
7. [Obsługa plików](#obsługa-plików)
8. [Biblioteki i moduły](#biblioteki-i-moduły)

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

## 🎯 Podsumowanie

### Kluczowe koncepcje:
1. **Zmienne** - przechowują dane
2. **Funkcje** - bloki kodu do wielokrotnego użycia
3. **Klasy** - szablony do tworzenia obiektów
4. **Pętle** - powtarzanie kodu
5. **Warunki** - podejmowanie decyzji
6. **Pliki** - praca z danymi

### Następne kroki:
- Praktykuj z prostymi programami
- Eksperymentuj z różnymi typami danych
- Twórz własne funkcje
- Czytaj dokumentację Python

### Przydatne zasoby:
- [Python.org](https://python.org) - oficjalna dokumentacja
- [Real Python](https://realpython.com) - tutoriale i artykuły
- [Python Tutor](https://pythontutor.com) - wizualizacja kodu

**Powodzenia w nauce Pythona! 🚀**
