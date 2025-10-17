# 🗜️ SqueezeIt - Kompresor Plików

## 📋 Opis projektu

**SqueezeIt** to aplikacja desktop do kompresji plików tekstowych, napisana w Pythonie z wykorzystaniem biblioteki FreeSimpleGUI. Projekt został stworzony jako narzędzie do nauki programowania i demonstracji tworzenia aplikacji GUI.

## 🎯 Funkcjonalności

### ✅ Zaimplementowane
- **Interfejs graficzny** - intuicyjny GUI z FreeSimpleGUI
- **Wybór plików** - możliwość wyboru plików do kompresji
- **Wybór folderu docelowego** - określenie miejsca zapisu
- **Obsługa zdarzeń** - reakcja na kliknięcia i zamknięcie okna

### 🚧 W trakcie rozwoju
- **Kompresja plików tekstowych** - algorytm kompresji
- **Walidacja plików** - sprawdzanie poprawności danych
- **Komunikaty o postępie** - informowanie użytkownika o statusie
- **Obsługa błędów** - graceful handling wyjątków

### 🔮 Planowane
- **Różne formaty plików** - rozszerzenie poza pliki tekstowe
- **Ustawienia kompresji** - wybór poziomu kompresji
- **Historia operacji** - logowanie wykonanych kompresji
- **Batch processing** - kompresja wielu plików jednocześnie

## 🛠️ Technologie

- **Python 3.12+** - język programowania
- **FreeSimpleGUI** - biblioteka do tworzenia GUI
- **Standardowe biblioteki Python** - obsługa plików, kompresja

## 📁 Struktura projektu

```
SqueezeIt-vibe/
├── main.py              # Główny plik aplikacji
├── gui.py               # Moduł interfejsu użytkownika (planowany)
├── core.py              # Logika kompresji (planowany)
├── utils.py             # Funkcje pomocnicze (planowany)
├── KURS.md              # Kurs Python od podstaw
├── ĆWICZENIA.md         # Zadania do wykonania
├── README.md            # Dokumentacja projektu
└── docs/                # Dodatkowa dokumentacja
```

## 🚀 Instalacja i uruchomienie

### Wymagania
- Python 3.12 lub nowszy
- FreeSimpleGUI

### Instalacja zależności
```bash
# Instalacja FreeSimpleGUI
pip install FreeSimpleGUI
```

### Uruchomienie aplikacji
```bash
# Uruchom główny plik
python main.py
```

## 📖 Jak używać

1. **Uruchom aplikację** - `python main.py`
2. **Wybierz pliki** - kliknij "Choose Files" i wybierz pliki do kompresji
3. **Wybierz folder docelowy** - kliknij "Choose Destination" i wybierz folder
4. **Kompresuj** - kliknij przycisk "Compress"
5. **Sprawdź wyniki** - skompresowane pliki znajdziesz w wybranym folderze

## 🎓 Materiały edukacyjne

### Kurs Python
- **KURS.md** - kompletny kurs Python od podstaw
- **ĆWICZENIA.md** - praktyczne zadania do wykonania

### Kluczowe koncepcje w projekcie
- **GUI Programming** - tworzenie interfejsów użytkownika
- **Event Handling** - obsługa zdarzeń (kliknięcia, zamknięcie)
- **File I/O** - praca z plikami i folderami
- **Error Handling** - obsługa błędów i wyjątków
- **Code Organization** - organizacja kodu w moduły

## 🔧 Rozwój projektu

### Struktura kodu
```python
# main.py - punkt wejścia
import FreeSimpleGUI as sg

# Główna pętla zdarzeń
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    # Obsługa zdarzeń...
```

### Konwencje nazewnictwa
- **Zmienne** - `snake_case` (np. `nazwa_pliku`)
- **Funkcje** - `snake_case` (np. `kompresuj_plik`)
- **Klasy** - `PascalCase` (np. `KompresorPlikow`)
- **Stałe** - `UPPER_CASE` (np. `MAX_ROZMIAR_PLIKU`)

### Style kodowania
- **PEP 8** - standardowe konwencje Python
- **Type hints** - adnotacje typów
- **Docstrings** - dokumentacja funkcji
- **Komentarze** - wyjaśnienia dla początkujących

## 🐛 Znane problemy

- Brak walidacji plików wejściowych
- Brak obsługi błędów kompresji
- Ograniczona obsługa formatów plików

## 🤝 Wkład w projekt

### Jak pomóc
1. **Zgłaszaj błędy** - opisz problem i kroki do reprodukcji
2. **Proponuj funkcje** - nowe pomysły na rozwój
3. **Poprawiaj dokumentację** - ulepszaj opisy i przykłady
4. **Testuj kod** - sprawdzaj działanie na różnych systemach

### Zasady współpracy
- Kod powinien być czytelny i dobrze udokumentowany
- Nowe funkcje powinny być testowane
- Zmiany powinny być zgodne z PEP 8
- Komentarze w języku polskim

## 📄 Licencja

Projekt jest udostępniony na licencji MIT - możesz go swobodnie używać, modyfikować i dystrybuować.

## 👨‍💻 Autor

Projekt stworzony jako narzędzie edukacyjne do nauki programowania w Pythonie.

## 📞 Kontakt

W przypadku pytań lub problemów, utwórz issue w repozytorium projektu.

---

**Powodzenia w nauce programowania! 🚀**
