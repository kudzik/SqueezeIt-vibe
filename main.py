# === GŁÓWNY PLIK APLIKACJI SQUEEZEIT ===
"""
SqueezeIt - Kompresor Plików
Główny plik aplikacji - punkt wejścia programu.

Ten plik importuje i uruchamia główną aplikację GUI.
Wszystka logika została przeniesiona do odpowiednich modułów:
- gui.py - interfejs użytkownika
- core.py - logika kompresji
- utils.py - funkcje pomocnicze (planowany)
"""

# Import głównej funkcji GUI
from gui import uruchom_aplikacje

# === PUNKT WEJŚCIA APLIKACJI ===
if __name__ == "__main__":
    """
    Uruchomienie aplikacji SqueezeIt.
    
    Ta funkcja jest wywoływana gdy plik main.py jest uruchamiany
    bezpośrednio (nie jako moduł).
    """
    print("Uruchamianie SqueezeIt - Kompresor Plikow")
    print("Aplikacja edukacyjna do nauki programowania w Pythonie")
    print("=" * 50)

    try:
        # Uruchomienie głównej aplikacji GUI
        uruchom_aplikacje()
    except KeyboardInterrupt:
        print("\nAplikacja zostala przerwana przez uzytkownika")
    except Exception as e:
        print(f"Blad aplikacji: {e}")
        print("Sprawdz czy wszystkie wymagane biblioteki sa zainstalowane")
    finally:
        print("Aplikacja zostala zamknieta")
