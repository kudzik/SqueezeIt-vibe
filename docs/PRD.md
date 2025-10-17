# 📋 PRD - Product Requirements Document
## SqueezeIt - Kompresor Plików

**Wersja:** 1.0  
**Data:** 2024  
**Autor:** Zespół SqueezeIt  
**Status:** W trakcie rozwoju  

---

## 📖 Spis treści

1. [Przegląd produktu](#przegląd-produktu)
2. [Cele biznesowe](#cele-biznesowe)
3. [Użytkownicy docelowi](#użytkownicy-docelowi)
4. [Wymagania funkcjonalne](#wymagania-funkcjonalne)
5. [Wymagania niefunkcjonalne](#wymagania-niefunkcjonalne)
6. [Interfejs użytkownika](#interfejs-użytkownika)
7. [Architektura techniczna](#architektura-techniczna)
8. [Harmonogram rozwoju](#harmonogram-rozwoju)
9. [Kryteria sukcesu](#kryteria-sukcesu)
10. [Ryzyka i ograniczenia](#ryzyka-i-ograniczenia)

---

## 🎯 Przegląd produktu

### Opis produktu
**SqueezeIt** to aplikacja desktop do kompresji plików tekstowych, stworzona w Pythonie z wykorzystaniem biblioteki FreeSimpleGUI. Produkt łączy w sobie funkcjonalność kompresji z elementami edukacyjnymi, służąc jako narzędzie do nauki programowania.

### Wartość dla użytkownika
- **Prostota użycia** - intuicyjny interfejs graficzny
- **Edukacyjność** - możliwość nauki programowania
- **Efektywność** - szybka kompresja plików tekstowych
- **Bezpieczeństwo** - lokalna kompresja bez wysyłania danych

### Pozycjonowanie
- **Główny rynek:** Użytkownicy domowi i studenci
- **Konkurencja:** 7-Zip, WinRAR, ale z naciskiem na edukację
- **Przewaga:** Edukacyjny aspekt + prostota użycia

---

## 💼 Cele biznesowe

### Cele krótkoterminowe (MVP)
- ✅ Stworzenie działającego GUI
- ✅ Implementacja podstawowej kompresji plików tekstowych
- ✅ Dokumentacja edukacyjna (KURS.md, ĆWICZENIA.md)
- ✅ Obsługa podstawowych formatów plików

### Cele średnioterminowe (v1.0)
- 🎯 Kompresja różnych typów plików
- 🎯 Ustawienia poziomu kompresji
- 🎯 Historia operacji
- 🎯 Walidacja i obsługa błędów

### Cele długoterminowe (v2.0+)
- 🚀 Wielowątkowa kompresja
- 🚀 Integracja z chmurą
- 🚀 API dla innych aplikacji
- 🚀 Wersja webowa

---

## 👥 Użytkownicy docelowi

### Główni użytkownicy

#### 1. **Studenci programowania** (60%)
- **Wiek:** 18-25 lat
- **Poziom:** Początkujący do średnio zaawansowanego
- **Potrzeby:** Nauka programowania, praktyczne projekty
- **Pain points:** Brak prostych projektów do nauki

#### 2. **Użytkownicy domowi** (30%)
- **Wiek:** 25-45 lat
- **Poziom:** Podstawowy
- **Potrzeby:** Kompresja plików, oszczędność miejsca
- **Pain points:** Skomplikowane narzędzia kompresji

#### 3. **Nauczyciele programowania** (10%)
- **Wiek:** 30-50 lat
- **Poziom:** Zaawansowany
- **Potrzeby:** Materiały edukacyjne, przykłady kodu
- **Pain points:** Brak gotowych projektów do nauczania

### Persony użytkowników

#### **Anna - Studentka Informatyki**
- 20 lat, studiuje informatykę
- Chce nauczyć się programowania GUI
- Potrzebuje prostych projektów do portfolio
- **Oczekiwania:** Czytelny kod, dobra dokumentacja

#### **Jan - Pracownik biurowy**
- 35 lat, pracuje z dokumentami
- Potrzebuje kompresować pliki do wysyłania
- Nie jest programistą
- **Oczekiwania:** Prosty interfejs, szybka kompresja

---

## ⚙️ Wymagania funkcjonalne

### 🎯 MVP (Minimum Viable Product)

#### **F1.1 - Wybór plików**
- **Opis:** Użytkownik może wybrać pliki do kompresji
- **Priorytet:** Wysoki
- **Akceptacja:** 
  - [ ] Możliwość wyboru pojedynczego pliku
  - [ ] Możliwość wyboru wielu plików
  - [ ] Walidacja wybranych plików
  - [ ] Wyświetlenie listy wybranych plików

#### **F1.2 - Wybór folderu docelowego**
- **Opis:** Użytkownik może wybrać gdzie zapisać skompresowane pliki
- **Priorytet:** Wysoki
- **Akceptacja:**
  - [ ] Możliwość wyboru folderu
  - [ ] Walidacja uprawnień do zapisu
  - [ ] Wyświetlenie ścieżki docelowej

#### **F1.3 - Kompresja plików tekstowych**
- **Opis:** Aplikacja kompresuje wybrane pliki tekstowe
- **Priorytet:** Wysoki
- **Akceptacja:**
  - [ ] Kompresja plików .txt, .csv, .json
  - [ ] Tworzenie archiwum .zip
  - [ ] Zachowanie struktury folderów
  - [ ] Informacja o postępie kompresji

#### **F1.4 - Interfejs użytkownika**
- **Opis:** Intuicyjny GUI z FreeSimpleGUI
- **Priorytet:** Wysoki
- **Akceptacja:**
  - [ ] Przycisk wyboru plików
  - [ ] Przycisk wyboru folderu
  - [ ] Przycisk kompresji
  - [ ] Obsługa zamknięcia okna

### 🚀 Wersja 1.0

#### **F2.1 - Ustawienia kompresji**
- **Opis:** Użytkownik może wybrać poziom kompresji
- **Priorytet:** Średni
- **Akceptacja:**
  - [ ] Slider poziomu kompresji (1-9)
  - [ ] Wybór algorytmu kompresji
  - [ ] Podgląd szacowanego rozmiaru

#### **F2.2 - Historia operacji**
- **Opis:** Aplikacja zapisuje historię kompresji
- **Priorytet:** Średni
- **Akceptacja:**
  - [ ] Lista ostatnich operacji
  - [ ] Szczegóły każdej operacji
  - [ ] Możliwość powtórzenia operacji

#### **F2.3 - Obsługa błędów**
- **Opis:** Graceful handling błędów i wyjątków
- **Priorytet:** Wysoki
- **Akceptacja:**
  - [ ] Komunikaty o błędach
  - [ ] Logowanie błędów
  - [ ] Recovery po błędach

#### **F2.4 - Różne formaty plików**
- **Opis:** Obsługa więcej typów plików
- **Priorytet:** Średni
- **Akceptacja:**
  - [ ] Pliki .docx, .pdf
  - [ ] Obrazy .jpg, .png
  - [ ] Pliki audio .mp3

### 🎯 Wersja 2.0

#### **F3.1 - Wielowątkowa kompresja**
- **Opis:** Równoległa kompresja wielu plików
- **Priorytet:** Średni
- **Akceptacja:**
  - [ ] Threading dla dużych plików
  - [ ] Progress bar dla każdego wątku
  - [ ] Kontrola liczby wątków

#### **F3.2 - Integracja z chmurą**
- **Opis:** Bezpośrednie zapisywanie do chmury
- **Priorytet:** Niski
- **Akceptacja:**
  - [ ] Integracja z Google Drive
  - [ ] Integracja z Dropbox
  - [ ] Autoryzacja OAuth

---

## 🔧 Wymagania niefunkcjonalne

### **N1.1 - Wydajność**
- **Czas kompresji:** < 30 sekund dla pliku 10MB
- **Użycie pamięci:** < 100MB RAM
- **Czas uruchomienia:** < 5 sekund

### **N1.2 - Kompatybilność**
- **Systemy operacyjne:** Windows 10+, macOS 10.14+, Linux Ubuntu 18+
- **Python:** 3.12+
- **Rozdzielczość:** Minimalna 1024x768

### **N1.3 - Bezpieczeństwo**
- **Lokalna kompresja:** Brak wysyłania danych
- **Walidacja plików:** Sprawdzanie przed kompresją
- **Uprawnienia:** Kontrola dostępu do plików

### **N1.4 - Użyteczność**
- **Czas nauki:** < 5 minut dla nowego użytkownika
- **Intuicyjność:** Brak potrzeby instrukcji
- **Dostępność:** Obsługa klawiatury

### **N1.5 - Niezawodność**
- **Uptime:** 99.9% dostępności
- **Recovery:** Automatyczne odzyskiwanie po błędach
- **Backup:** Zachowanie oryginalnych plików

---

## 🎨 Interfejs użytkownika

### **UI1.1 - Główny ekran**
```
┌─────────────────────────────────────────┐
│ SqueezeIt - Kompresor Plików            │
├─────────────────────────────────────────┤
│ Pliki do kompresji:                     │
│ [________________] [Choose Files]       │
│                                         │
│ Folder docelowy:                        │
│ [________________] [Choose Destination] │
│                                         │
│ Poziom kompresji: [████████░░] 6        │
│                                         │
│ [Compress] [Cancel]                     │
└─────────────────────────────────────────┘
```

### **UI1.2 - Ekran postępu**
```
┌─────────────────────────────────────────┐
│ Kompresja w toku...                      │
├─────────────────────────────────────────┤
│ Plik: dokument.txt                      │
│ Postęp: [████████████████████] 100%     │
│                                         │
│ [Cancel]                                │
└─────────────────────────────────────────┘
```

### **UI1.3 - Ekran wyników**
```
┌─────────────────────────────────────────┐
│ Kompresja zakończona!                   │
├─────────────────────────────────────────┤
│ ✅ dokument.txt → dokument.zip          │
│ ✅ raport.csv → raport.zip              │
│                                         │
│ Rozmiar przed: 2.5 MB                   │
│ Rozmiar po: 0.8 MB                      │
│ Oszczędność: 68%                        │
│                                         │
│ [Open Folder] [Close]                   │
└─────────────────────────────────────────┘
```

### **UI1.4 - Zasady projektowania**
- **Kolory:** Niebieski (#007ACC) jako główny, szary (#F0F0F0) jako tło
- **Czcionki:** Segoe UI, 12pt dla tekstu, 14pt dla nagłówków
- **Ikony:** Material Design Icons
- **Layout:** Responsywny, minimalny
- **Animacje:** Płynne przejścia, maksymalnie 300ms

---

## 🏗️ Architektura techniczna

### **A1.1 - Struktura modułów**
```
SqueezeIt-vibe/
├── main.py              # Punkt wejścia aplikacji
├── gui/
│   ├── __init__.py
│   ├── main_window.py   # Główne okno aplikacji
│   ├── progress_window.py # Okno postępu
│   └── results_window.py # Okno wyników
├── core/
│   ├── __init__.py
│   ├── compressor.py    # Logika kompresji
│   ├── validator.py     # Walidacja plików
│   └── logger.py        # System logowania
├── utils/
│   ├── __init__.py
│   ├── file_utils.py    # Funkcje pomocnicze
│   └── config.py        # Konfiguracja
└── tests/
    ├── __init__.py
    ├── test_compressor.py
    └── test_gui.py
```

### **A1.2 - Wzorce projektowe**
- **MVC (Model-View-Controller):** Oddzielenie logiki od interfejsu
- **Observer:** Obserwowanie postępu kompresji
- **Factory:** Tworzenie różnych typów kompresorów
- **Singleton:** Konfiguracja aplikacji

### **A1.3 - Biblioteki i zależności**
```python
# Główne biblioteki
FreeSimpleGUI>=4.0.0      # GUI framework
gzip                       # Kompresja (built-in)
zipfile                    # Archiwizacja (built-in)
threading                  # Wielowątkowość (built-in)

# Biblioteki pomocnicze
pytest>=7.0.0            # Testy jednostkowe
black>=22.0.0            # Formatowanie kodu
mypy>=1.0.0              # Type checking
```

### **A1.4 - Konfiguracja**
```python
# config.py
class Config:
    MAX_FILE_SIZE = 100 * 1024 * 1024  # 100MB
    MAX_THREADS = 4
    COMPRESSION_LEVELS = range(1, 10)
    SUPPORTED_FORMATS = ['.txt', '.csv', '.json', '.xml']
    LOG_LEVEL = 'INFO'
    LOG_FILE = 'squeezeit.log'
```

---

## 📅 Harmonogram rozwoju

### **Faza 1: MVP (4 tygodnie)**
- **Tydzień 1:** Podstawowy GUI, wybór plików
- **Tydzień 2:** Logika kompresji, walidacja
- **Tydzień 3:** Obsługa błędów, testy
- **Tydzień 4:** Dokumentacja, finalizacja

### **Faza 2: v1.0 (6 tygodni)**
- **Tydzień 5-6:** Ustawienia kompresji
- **Tydzień 7-8:** Historia operacji
- **Tydzień 9-10:** Różne formaty plików
- **Tydzień 11-12:** Testy, optymalizacja

### **Faza 3: v2.0 (8 tygodni)**
- **Tydzień 13-16:** Wielowątkowość
- **Tydzień 17-20:** Integracja z chmurą
- **Tydzień 21-24:** Testy, dokumentacja

### **Milestones**
- **M1:** Działający MVP (koniec fazy 1)
- **M2:** Pełna funkcjonalność v1.0 (koniec fazy 2)
- **M3:** Zaawansowane funkcje v2.0 (koniec fazy 3)

---

## 🎯 Kryteria sukcesu

### **Metryki techniczne**
- **Wydajność:** Kompresja 10MB w < 30 sekund
- **Stabilność:** < 1% crash rate
- **Kompatybilność:** Działanie na 95% systemów docelowych

### **Metryki użytkownika**
- **Adopcja:** 100+ pobrań w pierwszym miesiącu
- **Retention:** 70% użytkowników wraca po pierwszym użyciu
- **Satisfaction:** 4.5/5 średnia ocena

### **Metryki edukacyjne**
- **Engagement:** 80% użytkowników czyta dokumentację
- **Learning:** 60% użytkowników wykonuje ćwiczenia
- **Community:** 20+ pull requestów od społeczności

---

## ⚠️ Ryzyka i ograniczenia

### **Ryzyka techniczne**
- **Wydajność:** Duże pliki mogą spowolnić aplikację
- **Kompatybilność:** Problemy z różnymi wersjami Python
- **Bezpieczeństwo:** Potencjalne luki w obsłudze plików

### **Ryzyka biznesowe**
- **Konkurencja:** Istniejące narzędzia kompresji
- **Adopcja:** Niska świadomość produktu
- **Utrzymanie:** Koszty długoterminowego rozwoju

### **Ograniczenia**
- **Zasoby:** Ograniczony zespół deweloperski
- **Czas:** Presja na szybkie wydanie
- **Budżet:** Brak funduszy na marketing

### **Plan zarządzania ryzykiem**
- **Monitoring:** Regularne testy wydajności
- **Backup:** Alternatywne rozwiązania techniczne
- **Komunikacja:** Transparentność z użytkownikami

---

## 📞 Kontakt i wsparcie

### **Zespół projektu**
- **Lead Developer:** [Nazwa]
- **UI/UX Designer:** [Nazwa]
- **QA Engineer:** [Nazwa]
- **Technical Writer:** [Nazwa]

### **Kanały komunikacji**
- **GitHub Issues:** Błędy i feature requests
- **Email:** support@squeezeit.com
- **Discord:** Społeczność użytkowników
- **Documentation:** docs.squeezeit.com

### **Harmonogram aktualizacji**
- **MVP:** Q1 2024
- **v1.0:** Q2 2024
- **v2.0:** Q4 2024

---

**Dokument PRD v1.0 - SqueezeIt Kompresor Plików**  
*Ostatnia aktualizacja: 2024*
