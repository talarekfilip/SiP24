# Instrukcja uruchomienia aplikacji SiP24.pl

## Przygotowanie bazy danych PostgreSQL

1. **Utwórz bazę danych**:
   - Uruchom pgAdmin lub narzędzie wiersza poleceń psql
   - Utwórz nową bazę danych o nazwie `sip24db` z kodowaniem UTF-8:
     ```sql
     CREATE DATABASE sip24db WITH ENCODING = 'UTF8';
     ```

2. **Zaimportuj dane**:
   - Połącz się z bazą danych `sip24db`
   - Uruchom skrypt SQL z pliku `database_export.sql`
   - W pgAdmin: prawy przycisk na bazie danych → Query Tool → wklej zawartość pliku → uruchom

## Uruchomienie backendu (FastAPI)

1. **Skonfiguruj środowisko wirtualne** (w folderze `backend`):
   ```bash
   # Windows
   cd backend
   python -m venv venv
   venv\Scripts\activate

   # Linux/Mac
   cd backend
   python -m venv venv
   source venv/bin/activate
   ```

2. **Zainstaluj zależności**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Uruchom serwer** (upewnij się, że jesteś w folderze `backend`):
   ```bash
   uvicorn main:app --reload
   ```

   Po uruchomieniu, API będzie dostępne pod adresem: http://localhost:8000

4. **Sprawdź dokumentację API**:
   - Swagger UI: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

## Uruchomienie frontendu (Vue.js)

1. **Zainstaluj zależności** (w folderze `frontend`):
   ```bash
   cd frontend
   npm install
   ```

2. **Uruchom serwer deweloperski**:
   ```bash
   npm run dev
   ```

   Po uruchomieniu, strona będzie dostępna pod adresem: http://localhost:5173

## Uwagi dotyczące konfiguracji

- **Baza danych**: Backend jest skonfigurowany do łączenia się z bazą PostgreSQL na localhost z użytkownikiem `postgres` i hasłem `zaq1@WSX`. Jeśli masz inne dane dostępowe, zmodyfikuj plik `backend/database.py`.

- **API**: Frontend jest skonfigurowany do łączenia się z API na `http://localhost:8000`.

- **Polskie znaki**: Aplikacja została skonfigurowana do obsługi kodowania UTF-8 dla poprawnego wyświetlania polskich znaków. Jeśli nadal występują problemy:
  - Upewnij się, że wszystkie pliki są zapisane w kodowaniu UTF-8
  - Sprawdź, czy baza danych PostgreSQL używa kodowania UTF-8
  - W przeglądarce sprawdź kodowanie strony (powinno być ustawione na UTF-8)

## Rozwiązywanie problemów

1. **Problem z połączeniem do bazy danych**:
   - Sprawdź, czy PostgreSQL jest uruchomiony
   - Upewnij się, że dane logowania w `database.py` są poprawne

2. **Problem z uruchomieniem backendu**:
   - Upewnij się, że wszystkie zależności zostały zainstalowane
   - Sprawdź, czy Python jest w wersji 3.8 lub nowszej

3. **Problem z uruchomieniem frontendu**:
   - Upewnij się, że Node.js jest zainstalowany (wersja 14+)
   - Sprawdź, czy wszystkie zależności zostały zainstalowane

4. **Problem z polskimi znakami**:
   - Zrestartuj serwer backend i frontend po wprowadzeniu zmian
   - Wyczyść pamięć podręczną przeglądarki (Ctrl+F5)
   - Sprawdź, czy wszystkie pliki źródłowe są zapisane w kodowaniu UTF-8 