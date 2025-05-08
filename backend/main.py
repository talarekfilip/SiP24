from fastapi import FastAPI, Depends, HTTPException, Query, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse as FastAPIJSONResponse
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime
import json

import models
import schemas
from database import engine, get_db

# Custom JSON Response class for proper UTF-8 handling
class JSONResponse(FastAPIJSONResponse):
    media_type = "application/json; charset=utf-8"
    
    def render(self, content) -> bytes:
        return json.dumps(
            content,
            ensure_ascii=False,
            allow_nan=False,
            indent=None,
            separators=(",", ":"),
        ).encode("utf-8")

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="SiP24 API", 
    description="API dla serwisu komputerowego SiP24.pl",
    default_response_class=JSONResponse
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Middleware dla nagłówków UTF-8
@app.middleware("http")
async def add_charset_header(request, call_next):
    response = await call_next(request)
    
    # Set Content-Type header with charset for all response types
    content_type = response.headers.get("Content-Type", "")
    if "charset" not in content_type:
        if "application/json" in content_type:
            response.headers["Content-Type"] = "application/json; charset=utf-8"
        elif "text/html" in content_type:
            response.headers["Content-Type"] = "text/html; charset=utf-8"
        elif "text/plain" in content_type:
            response.headers["Content-Type"] = "text/plain; charset=utf-8"
        elif not content_type:
            response.headers["Content-Type"] = "application/json; charset=utf-8"
    
    # Additional headers for proper encoding
    response.headers["Accept-Charset"] = "utf-8"
    return response

# Service Category Endpoints
@app.get("/api/service-categories", response_model=List[schemas.ServiceCategory])
def get_service_categories(db: Session = Depends(get_db)):
    """Get all service categories"""
    return db.query(models.ServiceCategory).all()

@app.get("/api/service-categories/{category_id}", response_model=schemas.ServiceCategoryWithServices)
def get_service_category(category_id: int, db: Session = Depends(get_db)):
    """Get a service category by ID with all its services"""
    category = db.query(models.ServiceCategory).filter(models.ServiceCategory.id == category_id).first()
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

# Service Endpoints
@app.get("/api/services", response_model=List[schemas.Service])
def get_services(
    featured: Optional[bool] = Query(None, description="Filter by featured services"), 
    category_id: Optional[int] = Query(None, description="Filter by category ID"),
    limit: Optional[int] = Query(None, description="Limit number of results"),
    db: Session = Depends(get_db)
):
    """Get all services with optional filtering"""
    query = db.query(models.Service)
    
    if featured:
        query = query.filter(models.Service.featured == 1)
    
    if category_id:
        query = query.filter(models.Service.category_id == category_id)
    
    if limit:
        query = query.limit(limit)
        
    return query.all()

@app.get("/api/services/{service_id}", response_model=schemas.Service)
def get_service(service_id: int, db: Session = Depends(get_db)):
    """Get a service by ID"""
    service = db.query(models.Service).filter(models.Service.id == service_id).first()
    if service is None:
        raise HTTPException(status_code=404, detail="Service not found")
    return service

# Testimonial Endpoints
@app.get("/api/testimonials", response_model=List[schemas.Testimonial])
def get_testimonials(
    limit: Optional[int] = Query(None, description="Limit number of results"),
    db: Session = Depends(get_db)
):
    """Get all testimonials with optional limit"""
    query = db.query(models.Testimonial).order_by(models.Testimonial.created_at.desc())
    
    if limit:
        query = query.limit(limit)
        
    return query.all()

# Contact Form Endpoint
@app.post("/api/contact", response_model=schemas.ContactMessage)
def create_contact_message(contact: schemas.ContactFormCreate, db: Session = Depends(get_db)):
    """Submit a contact form"""
    db_contact = models.ContactMessage(
        name=contact.name,
        email=contact.email,
        phone=contact.phone,
        message=contact.message,
        created_at=datetime.utcnow(),
        status=models.ContactStatus.new
    )
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) 