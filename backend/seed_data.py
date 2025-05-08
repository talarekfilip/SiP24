# seed_data.py
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
import random
from models import ServiceCategory, Service, Testimonial
from database import SessionLocal, engine, Base

def seed_database():
    # Create tables
    Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    
    # Check if database is already seeded
    if db.query(ServiceCategory).count() > 0:
        print("Database already seeded. Skipping.")
        return
    
    try:
        # Create service categories
        categories = [
            ServiceCategory(name="Naprawa komputerów"),
            ServiceCategory(name="Serwis laptopów"),
            ServiceCategory(name="Usługi programistyczne"),
            ServiceCategory(name="Administracja sieciowa"),
        ]
        
        db.add_all(categories)
        db.commit()
        
        # Refresh to get IDs
        for category in categories:
            db.refresh(category)
        
        # Create services
        services = [
            # Naprawa komputerów
            Service(
                name="Diagnostyka komputera",
                description="Kompleksowa diagnostyka komputera stacjonarnego w celu wykrycia problemów sprzętowych lub programowych.",
                price_from=50.00,
                estimated_time="1-2 godziny",
                category_id=categories[0].id,
                featured=1
            ),
            Service(
                name="Czyszczenie komputera",
                description="Czyszczenie komputera z kurzu, wymiana pasty termoprzewodzącej, optymalizacja chłodzenia.",
                price_from=80.00,
                estimated_time="1-3 godziny",
                category_id=categories[0].id
            ),
            Service(
                name="Instalacja systemu operacyjnego",
                description="Instalacja systemu Windows lub Linux wraz z niezbędnymi sterownikami i podstawowym oprogramowaniem.",
                price_from=120.00,
                estimated_time="2-4 godziny",
                category_id=categories[0].id,
                featured=1
            ),
            Service(
                name="Modernizacja komputera",
                description="Wymiana lub rozbudowa podzespołów komputerowych (RAM, dysk, karta graficzna, itd.).",
                price_from=100.00,
                estimated_time="1-4 godziny",
                category_id=categories[0].id
            ),
            
            # Serwis laptopów
            Service(
                name="Diagnostyka laptopa",
                description="Kompleksowa diagnostyka laptopa w celu wykrycia problemów sprzętowych lub programowych.",
                price_from=60.00,
                estimated_time="1-2 godziny",
                category_id=categories[1].id,
                featured=1
            ),
            Service(
                name="Czyszczenie laptopa",
                description="Czyszczenie laptopa z kurzu, wymiana pasty termoprzewodzącej, optymalizacja chłodzenia.",
                price_from=100.00,
                estimated_time="1-3 godziny",
                category_id=categories[1].id
            ),
            Service(
                name="Wymiana matrycy",
                description="Wymiana uszkodzonej matrycy w laptopie wraz z kalibracją.",
                price_from=250.00,
                estimated_time="1-2 godziny",
                category_id=categories[1].id
            ),
            Service(
                name="Naprawa płyty głównej",
                description="Naprawa uszkodzonej płyty głównej laptopa, wymiana układów.",
                price_from=300.00,
                estimated_time="2-5 dni",
                category_id=categories[1].id
            ),
            
            # Usługi programistyczne
            Service(
                name="Tworzenie strony internetowej",
                description="Projektowanie i tworzenie responsywnych stron internetowych dostosowanych do potrzeb klienta.",
                price_from=500.00,
                estimated_time="5-15 dni",
                category_id=categories[2].id
            ),
            Service(
                name="Programowanie aplikacji",
                description="Tworzenie aplikacji desktopowych lub mobilnych na zamówienie.",
                price_from=1000.00,
                estimated_time="10-30 dni",
                category_id=categories[2].id
            ),
            
            # Administracja sieciowa
            Service(
                name="Konfiguracja sieci domowej",
                description="Konfiguracja routera, sieci WiFi, zabezpieczeń oraz urządzeń sieciowych w domu lub małym biurze.",
                price_from=150.00,
                estimated_time="2-4 godziny",
                category_id=categories[3].id
            ),
            Service(
                name="Instalacja serwera",
                description="Instalacja i konfiguracja serwera dla małych i średnich firm.",
                price_from=400.00,
                estimated_time="1-3 dni",
                category_id=categories[3].id
            ),
        ]
        
        db.add_all(services)
        db.commit()
        
        # Create testimonials
        testimonials = [
            Testimonial(
                author="Jan Kowalski",
                rating=5,
                text="Szybka i profesjonalna obsługa. Laptop działa jak nowy!",
                created_at=datetime.now() - timedelta(days=random.randint(1, 60))
            ),
            Testimonial(
                author="Anna Nowak",
                rating=4,
                text="Bardzo dobry kontakt i profesjonalne podejście do klienta.",
                created_at=datetime.now() - timedelta(days=random.randint(1, 60))
            ),
            Testimonial(
                author="Piotr Wiśniewski",
                rating=5,
                text="Polecam serwis SiP24. Fachowa pomoc i konkurencyjne ceny.",
                created_at=datetime.now() - timedelta(days=random.randint(1, 60))
            ),
            Testimonial(
                author="Magdalena Kaczmarek",
                rating=5,
                text="Naprawili mój komputer, gdy inni serwisanci twierdzili, że się nie da. Rewelacja!",
                created_at=datetime.now() - timedelta(days=random.randint(1, 60))
            ),
            Testimonial(
                author="Tomasz Zieliński",
                rating=4,
                text="Profesjonalna obsługa, choć trochę dłużej niż obiecywano. Efekt końcowy zadowalający.",
                created_at=datetime.now() - timedelta(days=random.randint(1, 60))
            ),
        ]
        
        db.add_all(testimonials)
        db.commit()
        
        print("Database seeded successfully!")
        
    except Exception as e:
        print(f"Error seeding database: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed_database() 