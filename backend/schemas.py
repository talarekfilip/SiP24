# schemas.py
from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime

class BaseConfigClass:
    """Base configuration class for all Pydantic models"""
    orm_mode = True
    from_attributes = True
    json_encoders = {
        str: lambda v: v
    }
    anystr_strip_whitespace = True
    # These ensure proper string encoding
    str_strip_whitespace = True
    str_to_lower = False
    str_to_upper = False
    str_min_length = 1
    
# Service Category schemas
class ServiceCategoryBase(BaseModel):
    name: str

class ServiceCategoryCreate(ServiceCategoryBase):
    pass

class ServiceCategory(ServiceCategoryBase):
    id: int

    class Config(BaseConfigClass):
        pass

# Service schemas
class ServiceBase(BaseModel):
    name: str
    description: str
    price_from: float
    estimated_time: str
    category_id: int
    featured: Optional[int] = 0

class ServiceCreate(ServiceBase):
    pass

class Service(ServiceBase):
    id: int

    class Config(BaseConfigClass):
        pass

# Category with services
class ServiceCategoryWithServices(ServiceCategory):
    services: List[Service] = []

    class Config(BaseConfigClass):
        pass

# Testimonial schemas
class TestimonialBase(BaseModel):
    author: str
    rating: int
    text: str

class TestimonialCreate(TestimonialBase):
    pass

class Testimonial(TestimonialBase):
    id: int
    created_at: datetime

    class Config(BaseConfigClass):
        pass

# Contact message schemas
class ContactFormBase(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str] = None
    message: str

class ContactFormCreate(ContactFormBase):
    pass

class ContactMessage(ContactFormBase):
    id: int
    created_at: datetime
    status: str

    class Config(BaseConfigClass):
        pass 