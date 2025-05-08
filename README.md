# SiP24.pl - Serwis Komputerowy

Aplikacja strony internetowej dla serwisu komputerowego SiP24.pl. Zawiera frontend zbudowany w Vue.js oraz backend w FastAPI.

## Zawartość projektu

- `frontend/` - Aplikacja Vue.js z TypeScript
- `backend/` - API RESTful zbudowane przy użyciu FastAPI

## Wymagania

### Frontend
- Node.js 14+
- npm 6+

### Backend
- Python 3.8+
- PostgreSQL 12+

## Instalacja i uruchomienie

### Baza danych

1. Zainstaluj i uruchom PostgreSQL.
2. Utwórz bazę danych dla aplikacji:

```sql
CREATE DATABASE sip24db;
```

### Backend

1. Przejdź do katalogu backend:

```bash
cd backend
```

2. Utwórz i aktywuj wirtualne środowisko Python:

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python -m venv venv
source venv/bin/activate
```

3. Zainstaluj zależności:

```bash
pip install -r requirements.txt
```

4. Konfiguracja środowiska (opcjonalnie):
   
   Utwórz plik `.env` w katalogu backend z następującymi zmiennymi:

   ```
   DATABASE_URL=postgresql://postgres:password@localhost/sip24db
   API_HOST=0.0.0.0
   API_PORT=8000
   ENVIRONMENT=development
   ```

5. Zainicjuj bazę danych przykładowymi danymi:

```bash
python seed_data.py
```

6. Uruchom serwer API:

```bash
uvicorn main:app --reload
```

Server API będzie dostępny pod adresem http://localhost:8000

### Frontend

1. Przejdź do katalogu frontend:

```bash
cd frontend
```

2. Zainstaluj zależności:

```bash
npm install
```

3. Konfiguracja środowiska (opcjonalnie):
   
   Utwórz plik `.env` w katalogu frontend z następującymi zmiennymi:

   ```
   VITE_API_URL=http://localhost:8000
   ```

4. Uruchom serwer deweloperski:

```bash
npm run dev
```

Frontend będzie dostępny pod adresem http://localhost:5173

## Funkcjonalności

- Nawigacja z zakładkami: "Strona główna", "Usługi", "Kontakt", "Lokalizacja"
- Strona główna z prezentacją usług i opiniami klientów
- Szczegółowy wykaz usług z kategoryzacją
- Formularz kontaktowy
- Informacje o lokalizacji serwisu

## Dokumentacja API

Po uruchomieniu backendu, dokumentacja API dostępna jest pod adresem:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc 