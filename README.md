# 🗜️ SqueezeIt - Kompresor Plików

## 📋 Opis projektu

**SqueezeIt** to aplikacja desktop do kompresji plików tekstowych, napisana w Pythonie z wykorzystaniem biblioteki FreeSimpleGUI. Projekt został stworzony jako narzędzie do nauki programowania i demonstracji tworzenia aplikacji GUI.

## 🎯 Funkcjonalności

### ✅ Zaimplementowane
- **Interfejs graficzny** - intuicyjny GUI z FreeSimpleGUI
- **Wybór plików** - możliwość wyboru plików do kompresji
- **Wybór folderu docelowego** - określenie miejsca zapisu
- **Obsługa zdarzeń** - reakcja na kliknięcia i zamknięcie okna
- **Kompresja plików** - prawdziwa kompresja do formatu ZIP
- **Walidacja plików** - sprawdzanie poprawności danych
- **Komunikaty o postępie** - informowanie użytkownika o statusie
- **Obsługa błędów** - graceful handling wyjątków
- **Ustawienia kompresji** - wybór poziomu kompresji (1-9)
- **Statystyki operacji** - okno ze statystykami
- **Wyniki kompresji** - szczegółowe raporty

### 🚧 W trakcie rozwoju
- **Różne formaty plików** - rozszerzenie poza pliki tekstowe
- **Historia operacji** - logowanie wykonanych kompresji
- **Batch processing** - kompresja wielu plików jednocześnie

### 🔮 Planowane
- **Wielowątkowa kompresja** - równoległa kompresja dużych plików
- **Integracja z chmurą** - bezpośrednie zapisywanie do chmury
- **API dla innych aplikacji** - możliwość integracji
- **Wersja webowa** - aplikacja w przeglądarce

## 🛠️ Technologie

- **Python 3.12+** - język programowania
- **FreeSimpleGUI** - biblioteka do tworzenia GUI
- **Standardowe biblioteki Python** - obsługa plików, kompresja

## 📁 Struktura projektu

```
SqueezeIt-vibe/
├── main.py              # ✅ Główny plik aplikacji
├── gui.py               # ✅ Moduł interfejsu użytkownika
├── core.py              # ✅ Logika kompresji plików
├── utils.py             # ✅ Funkcje pomocnicze
├── README.md            # ✅ Dokumentacja projektu
├── pyproject.toml       # ✅ Konfiguracja projektu
├── .gitignore           # ✅ Pliki ignorowane przez Git
└── docs/                # ✅ Dokumentacja edukacyjna
    ├── KURS.md          # ✅ Kurs Python od podstaw
    ├── ĆWICZENIA.md     # ✅ Zadania do wykonania
    └── PRD.md           # ✅ Dokument wymagań produktu
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
- **`docs/KURS.md`** - kompletny kurs Python od podstaw z przykładami z SqueezeIt
- **`docs/ĆWICZENIA.md`** - praktyczne zadania do wykonania (4 poziomy trudności)
- **`docs/PRD.md`** - dokument wymagań produktu (Product Requirements Document)

### Kluczowe koncepcje w projekcie
- **GUI Programming** - tworzenie interfejsów użytkownika z FreeSimpleGUI
- **Event Handling** - obsługa zdarzeń (kliknięcia, zamknięcie, slider)
- **File I/O** - praca z plikami i folderami (zipfile, os.path)
- **Error Handling** - obsługa błędów i wyjątków (try/except/finally)
- **Code Organization** - organizacja kodu w moduły (main.py, gui.py, core.py, utils.py)
- **Object-Oriented Programming** - klasy i obiekty (KompresorPlikow, SqueezeItGUI)
- **Type Hints** - adnotacje typów dla lepszej czytelności kodu

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
