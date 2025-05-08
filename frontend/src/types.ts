// src/types.ts

export interface Service {
  id: number;
  name: string;
  description: string;
  price_from: number;
  estimated_time: string;
  category_id: number;
}

export interface ServiceCategory {
  id: number;
  name: string;
  services?: Service[];
}

export interface Testimonial {
  id: number;
  author: string;
  rating: number;
  text: string;
  created_at: string;
}

export interface ContactForm {
  name: string;
  email: string;
  phone?: string;
  message: string;
}

export interface ContactMessage extends ContactForm {
  id: number;
  created_at: string;
  status: 'new' | 'read' | 'responded';
}

export interface NavTab {
  id: string;
  name: string;
  path: string;
} 