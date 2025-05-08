<template>
  <div class="contact-form-container">
    <h3>Formularz kontaktowy</h3>
    <form @submit.prevent="submitForm" class="contact-form">
      <div class="form-group">
        <label for="name">Imię i nazwisko</label>
        <input 
          type="text" 
          id="name" 
          v-model="form.name" 
          required
          placeholder="Wprowadź imię i nazwisko"
        >
      </div>
      
      <div class="form-group">
        <label for="email">Adres e-mail</label>
        <input 
          type="email" 
          id="email" 
          v-model="form.email" 
          required
          placeholder="Wprowadź adres e-mail"
        >
      </div>
      
      <div class="form-group">
        <label for="phone">Telefon (opcjonalnie)</label>
        <input 
          type="tel" 
          id="phone" 
          v-model="form.phone" 
          placeholder="Wprowadź numer telefonu"
        >
      </div>
      
      <div class="form-group">
        <label for="message">Wiadomość</label>
        <textarea 
          id="message" 
          v-model="form.message" 
          rows="5" 
          required
          placeholder="Opisz swój problem lub zapytanie"
        ></textarea>
      </div>
      
      <div class="form-actions">
        <button type="submit" class="btn-primary" :disabled="isSubmitting">
          <span v-if="isSubmitting">Wysyłanie...</span>
          <span v-else>Wyślij wiadomość</span>
        </button>
      </div>
      
      <div v-if="submitStatus" class="submit-status" :class="submitStatus.type">
        {{ submitStatus.message }}
      </div>
    </form>
  </div>
</template>

<script lang="ts">
import { defineComponent, reactive, ref } from 'vue';
import { submitContactForm } from '@/api';
import type { ContactFormData } from '@/api';

interface SubmitStatus {
  type: 'success' | 'error';
  message: string;
}

export default defineComponent({
  name: 'ContactForm',
  setup() {
    const form = reactive<ContactFormData>({
      name: '',
      email: '',
      phone: '',
      message: ''
    });
    
    const isSubmitting = ref(false);
    const submitStatus = ref<SubmitStatus | null>(null);
    
    const submitForm = async () => {
      isSubmitting.value = true;
      submitStatus.value = null;
      
      try {
        await submitContactForm(form);
        submitStatus.value = {
          type: 'success',
          message: 'Dziękujemy! Twoja wiadomość została wysłana. Skontaktujemy się tak szybko, jak to możliwe.'
        };
        
        // Reset form after successful submission
        form.name = '';
        form.email = '';
        form.phone = '';
        form.message = '';
        
      } catch (error) {
        submitStatus.value = {
          type: 'error',
          message: 'Przepraszamy, wystąpił problem podczas wysyłania wiadomości. Proszę spróbować ponownie później.'
        };
        console.error('Error submitting contact form:', error);
      } finally {
        isSubmitting.value = false;
      }
    };
    
    return {
      form,
      isSubmitting,
      submitStatus,
      submitForm
    };
  }
});
</script>

<style scoped>
.contact-form-container {
  background-color: var(--white);
  border-radius: 8px;
  padding: 2rem;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
}

.contact-form-container h3 {
  margin-bottom: 1.5rem;
  color: var(--black);
  text-align: center;
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 500;
  color: var(--black);
}

.form-actions {
  margin-top: 2rem;
}

.btn-primary {
  width: 100%;
  padding: 0.8rem;
  font-size: 1rem;
}

.btn-primary:disabled {
  background-color: var(--gray);
  cursor: not-allowed;
  transform: none;
}

.submit-status {
  margin-top: 1.5rem;
  padding: 1rem;
  border-radius: 4px;
  text-align: center;
}

.submit-status.success {
  background-color: #e7f7e7;
  color: #2e7d32;
}

.submit-status.error {
  background-color: #fdeded;
  color: #d32f2f;
}
</style> 