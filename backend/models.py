# models.py
from sqlalchemy import Column, Integer, String, Text, Float, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from database import Base
import enum
from datetime import datetime

class ServiceCategory(Base):
    """Service category model"""
    __tablename__ = "service_categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    
    # Relationship
    services = relationship("Service", back_populates="category")

class Service(Base):
    """Service model"""
    __tablename__ = "services"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(Text, nullable=False)
    price_from = Column(Float, nullable=False)
    estimated_time = Column(String(50), nullable=False)
    category_id = Column(Integer, ForeignKey("service_categories.id"))
    featured = Column(Integer, default=0)  # 0 = not featured, 1 = featured
    
    # Relationship
    category = relationship("ServiceCategory", back_populates="services")

class Testimonial(Base):
    """Customer testimonial model"""
    __tablename__ = "testimonials"

    id = Column(Integer, primary_key=True, index=True)
    author = Column(String(100), nullable=False)
    rating = Column(Integer, nullable=False)
    text = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)

class ContactStatus(str, enum.Enum):
    """Contact message status enum"""
    new = "new"
    read = "read"
    responded = "responded"

class ContactMessage(Base):
    """Contact message model"""
    __tablename__ = "contact_messages"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    phone = Column(String(20), nullable=True)
    message = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    status = Column(Enum(ContactStatus), default=ContactStatus.new, nullable=False) 