-- SiP24.pl Database Export

-- Ustawienie kodowania
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET datestyle = 'iso, mdy';
SET server_encoding = 'UTF8';
SET lc_messages = 'pl_PL.UTF-8';
SET lc_monetary = 'pl_PL.UTF-8';
SET lc_numeric = 'pl_PL.UTF-8';
SET lc_time = 'pl_PL.UTF-8';

-- Tworzenie bazy danych - te komendy wykonujemy ręcznie przez pgAdmin
-- DROP DATABASE IF EXISTS sip24db;
-- CREATE DATABASE sip24db WITH ENCODING = 'UTF8' LC_COLLATE = 'pl_PL.UTF-8' LC_CTYPE = 'pl_PL.UTF-8';
-- Następnie łączymy się z bazą sip24db i wykonujemy resztę skryptu

-- Tworzenie tabel
CREATE TABLE IF NOT EXISTS service_categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS services (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    price_from FLOAT NOT NULL,
    estimated_time VARCHAR(50) NOT NULL,
    category_id INTEGER REFERENCES service_categories(id),
    featured INTEGER DEFAULT 0
);

-- Sprawdzamy czy istnieje już typ contact_status
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'contact_status') THEN
        CREATE TYPE contact_status AS ENUM ('new', 'read', 'responded');
    END IF;
END$$;

CREATE TABLE IF NOT EXISTS testimonials (
    id SERIAL PRIMARY KEY,
    author VARCHAR(100) NOT NULL,
    rating INTEGER NOT NULL,
    text TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS contact_messages (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    phone VARCHAR(20),
    message TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    status contact_status NOT NULL DEFAULT 'new'
);

-- Wstawianie danych tylko jeśli tabele są puste
INSERT INTO service_categories (name)
SELECT 'Naprawa komputerów' WHERE NOT EXISTS (SELECT 1 FROM service_categories);
INSERT INTO service_categories (name)
SELECT 'Serwis laptopów' WHERE NOT EXISTS (SELECT 1 FROM service_categories WHERE name = 'Serwis laptopów');
INSERT INTO service_categories (name)
SELECT 'Usługi programistyczne' WHERE NOT EXISTS (SELECT 1 FROM service_categories WHERE name = 'Usługi programistyczne');
INSERT INTO service_categories (name)
SELECT 'Administracja sieciowa' WHERE NOT EXISTS (SELECT 1 FROM service_categories WHERE name = 'Administracja sieciowa');

-- Usługi - wstawiamy tylko jeśli nie ma żadnych usług
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM services) THEN
        -- Usługi - Naprawa komputerów
        INSERT INTO services (name, description, price_from, estimated_time, category_id, featured) VALUES
        ('Diagnostyka komputera', 'Kompleksowa diagnostyka komputera stacjonarnego w celu wykrycia problemów sprzętowych lub programowych.', 50.00, '1-2 godziny', 1, 1),
        ('Czyszczenie komputera', 'Czyszczenie komputera z kurzu, wymiana pasty termoprzewodzącej, optymalizacja chłodzenia.', 80.00, '1-3 godziny', 1, 0),
        ('Instalacja systemu operacyjnego', 'Instalacja systemu Windows lub Linux wraz z niezbędnymi sterownikami i podstawowym oprogramowaniem.', 120.00, '2-4 godziny', 1, 1),
        ('Modernizacja komputera', 'Wymiana lub rozbudowa podzespołów komputerowych (RAM, dysk, karta graficzna, itd.).', 100.00, '1-4 godziny', 1, 0);

        -- Usługi - Serwis laptopów
        INSERT INTO services (name, description, price_from, estimated_time, category_id, featured) VALUES
        ('Diagnostyka laptopa', 'Kompleksowa diagnostyka laptopa w celu wykrycia problemów sprzętowych lub programowych.', 60.00, '1-2 godziny', 2, 1),
        ('Czyszczenie laptopa', 'Czyszczenie laptopa z kurzu, wymiana pasty termoprzewodzącej, optymalizacja chłodzenia.', 100.00, '1-3 godziny', 2, 0),
        ('Wymiana matrycy', 'Wymiana uszkodzonej matrycy w laptopie wraz z kalibracją.', 250.00, '1-2 godziny', 2, 0),
        ('Naprawa płyty głównej', 'Naprawa uszkodzonej płyty głównej laptopa, wymiana układów.', 300.00, '2-5 dni', 2, 0);

        -- Usługi - Usługi programistyczne
        INSERT INTO services (name, description, price_from, estimated_time, category_id, featured) VALUES
        ('Tworzenie strony internetowej', 'Projektowanie i tworzenie responsywnych stron internetowych dostosowanych do potrzeb klienta.', 500.00, '5-15 dni', 3, 0),
        ('Programowanie aplikacji', 'Tworzenie aplikacji desktopowych lub mobilnych na zamówienie.', 1000.00, '10-30 dni', 3, 0);

        -- Usługi - Administracja sieciowa
        INSERT INTO services (name, description, price_from, estimated_time, category_id, featured) VALUES
        ('Konfiguracja sieci domowej', 'Konfiguracja routera, sieci WiFi, zabezpieczeń oraz urządzeń sieciowych w domu lub małym biurze.', 150.00, '2-4 godziny', 4, 0),
        ('Instalacja serwera', 'Instalacja i konfiguracja serwera dla małych i średnich firm.', 400.00, '1-3 dni', 4, 0);
    END IF;
END$$;

-- Opinie klientów - wstawiamy tylko jeśli nie ma żadnych opinii
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM testimonials) THEN
        INSERT INTO testimonials (author, rating, text, created_at) VALUES
        ('Jan Kowalski', 5, 'Szybka i profesjonalna obsługa. Laptop działa jak nowy!', NOW() - INTERVAL '15 days'),
        ('Anna Nowak', 4, 'Bardzo dobry kontakt i profesjonalne podejście do klienta.', NOW() - INTERVAL '30 days'),
        ('Piotr Wiśniewski', 5, 'Polecam serwis SiP24. Fachowa pomoc i konkurencyjne ceny.', NOW() - INTERVAL '45 days'),
        ('Magdalena Kaczmarek', 5, 'Naprawili mój komputer, gdy inni serwisanci twierdzili, że się nie da. Rewelacja!', NOW() - INTERVAL '20 days'),
        ('Tomasz Zieliński', 4, 'Profesjonalna obsługa, choć trochę dłużej niż obiecywano. Efekt końcowy zadowalający.', NOW() - INTERVAL '10 days');
    END IF;
END$$; 