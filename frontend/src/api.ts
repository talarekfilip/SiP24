// API utility for properly handling UTF-8 responses
import axios from 'axios';

// Create axios instance with default config
const api = axios.create({
  baseURL: '/api',
  headers: {
    'Content-Type': 'application/json; charset=utf-8',
    'Accept': 'application/json; charset=utf-8',
    'Accept-Charset': 'utf-8'
  },
  responseType: 'json',
  transformResponse: [(data) => {
    // If data is a string, parse it with proper encoding handling
    if (typeof data === 'string') {
      try {
        return JSON.parse(data);
      } catch (e) {
        return data;
      }
    }
    return data;
  }]
});

// Response interceptor to handle errors
api.interceptors.response.use(
  response => response,
  error => {
    console.error('API Error:', error);
    return Promise.reject(error);
  }
);

// Request interceptor to set headers
api.interceptors.request.use(
  config => {
    // Ensure all requests have UTF-8 headers
    if (!config.headers['Content-Type']) {
      config.headers['Content-Type'] = 'application/json; charset=utf-8';
    }
    if (!config.headers['Accept']) {
      config.headers['Accept'] = 'application/json; charset=utf-8';
    }
    config.headers['Accept-Charset'] = 'utf-8';
    return config;
  },
  error => Promise.reject(error)
);

// Type interfaces
export interface Service {
  id: number;
  name: string;
  description: string;
  price_from: number;
  estimated_time: string;
  category_id: number;
  featured: number;
}

export interface ServiceCategory {
  id: number;
  name: string;
}

export interface ServiceCategoryWithServices extends ServiceCategory {
  services: Service[];
}

export interface Testimonial {
  id: number;
  author: string;
  rating: number;
  text: string;
  created_at: string;
}

export interface ContactFormData {
  name: string;
  email: string;
  phone?: string;
  message: string;
}

// App-specific interfaces
export interface NavTab {
  id: string;
  name: string;
  path: string;
}

// API functions
export const getServiceCategories = () => api.get<ServiceCategory[]>('/service-categories');
export const getServiceCategory = (id: number) => api.get<ServiceCategoryWithServices>(`/service-categories/${id}`);
export const getServices = (params?: { featured?: boolean, category_id?: number, limit?: number }) => 
  api.get<Service[]>('/services', { params });
export const getService = (id: number) => api.get<Service>(`/services/${id}`);
export const getTestimonials = (params?: { limit?: number }) => 
  api.get<Testimonial[]>('/testimonials', { params });
export const submitContactForm = (data: ContactFormData) => 
  api.post('/contact', data);

export default api; 