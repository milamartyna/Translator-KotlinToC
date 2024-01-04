# Translator Kodu z Kotlin na C

## Przegląd
Projekt ten jest translacją kodu z Kotlin na C. Czyta kod źródłowy Kotlin i przekłada go na równoważny kod źródłowy C. Translator został zaimplementowany w Pythonie z wykorzystaniem biblioteki PLY (Python Lex-Yacc).

## Wymagania
- Python 3.x
- Biblioteka PLY

## Instalacja

1. **Python 3**: Upewnij się, że masz zainstalowanego Pythona 3.x na swoim systemie. Możesz pobrać go [tutaj](https://www.python.org/downloads/).

2. **Biblioteka PLY**: Po zainstalowaniu Pythona, zainstaluj bibliotekę PLY za pomocą pip:

    ```bash
    pip install ply
    ```

## Użycie

1. **Przygotuj Plik Kotlin**: Napisz kod Kotlin, który chcesz przetłumaczyć i zapisz go jako `input.kt`.

2. **Uruchom Translator**: Wykonaj skrypt translacyjny w Pythonie:

    ```bash
    python main.py
    ```

   Upewnij się, że Twój plik `input.kt` znajduje się w tym samym katalogu co skrypt translacyjny.

3. **Sprawdź Wynik**: Po uruchomieniu skryptu sprawdź wygenerowany kod C w pliku `inputTranslated.c`.

## Jak To Działa

- **Analiza Leksykalna**: Skrypt najpierw wykonuje analizę leksykalną pliku Kotlin z użyciem modułu `lex` z PLY. Tokenizuje wejściowy kod Kotlin.

- **Parsowanie**: Następnie moduł `yacc` z PLY jest używany do parsowania. Przetwarza tokeny z leksera i stosuje dostarczone reguły gramatyki, aby wygenerować równoważny kod C.

- **Generacja Wyników**: Przetłumaczony kod C jest następnie zapisywany do pliku `inputTranslated.c`.

## Dostosowanie

- **Pliki Wejściowe/Wyjściowe**: Możesz zmienić ścieżki plików wejściowych i wyjściowych w skrypcie:

    ```python
    input_kotlin = "ścieżka/do/twójego/input.kt"
    output_file = "ścieżka/do/twójego/output.c"
    ```

- **Tokeny i Gramatyka**: Możesz modyfikować tokeny i reguły gramatyczne według swoich potrzeb translacyjnych w skrypcie.

## Ograniczenia

- Translator obsługuje podstawowe konstrukty Kotlin. Skomplikowane funkcje i konstrukcje specyficzne dla Kotlin mogą nie być poprawnie przetłumaczone lub mogą wymagać dodatkowych reguł i logiki.

- Obsługa błędów jest podstawowa, a translacja może nie powieść się lub wygenerować nieprawidłowe wyniki dla składniowo niepoprawnego lub złożonego kodu Kotlin.



