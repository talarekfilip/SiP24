<template>
  <div class="contact-view">
    <div class="container">
      <h2>Kontakt</h2>
      
      <div class="contact-container">
        <div class="contact-info">
          <div class="card">
            <h3>Dane kontaktowe</h3>
            
            <div class="contact-item">
              <h4>Telefon</h4>
              <p>+48 123 456 789</p>
            </div>
            
            <div class="contact-item">
              <h4>Email</h4>
              <p><a href="mailto:kontakt@sip24.pl">kontakt@sip24.pl</a></p>
            </div>
            
            <div class="contact-item">
              <h4>Godziny otwarcia</h4>
              <ul class="hours-list">
                <li>
                  <span>Poniedziałek - Piątek:</span>
                  <span>9:00 - 17:00</span>
                </li>
                <li>
                  <span>Sobota:</span>
                  <span>10:00 - 14:00</span>
                </li>
                <li>
                  <span>Niedziela:</span>
                  <span>Zamknięte</span>
                </li>
              </ul>
            </div>
            
            <div class="contact-social">
              <h4>Media społecznościowe</h4>
              <div class="social-links">
                <a href="#" target="_blank" aria-label="Facebook" class="social-link">Facebook</a>
                <a href="#" target="_blank" aria-label="Instagram" class="social-link">Instagram</a>
              </div>
            </div>
          </div>
        </div>
        
        <div class="contact-form-wrapper">
          <ContactForm />
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import ContactForm from '@/components/ContactForm.vue';

export default defineComponent({
  name: 'ContactView',
  components: {
    ContactForm
  }
});
</script>

<style scoped>
.contact-view {
  padding: 2rem 0;
}

.contact-view h2 {
  text-align: center;
  margin-bottom: 2rem;
  color: var(--black);
  font-size: 2rem;
}

.contact-container {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
}

.contact-info {
  display: flex;
  flex-direction: column;
}

.contact-item {
  margin-bottom: 1.5rem;
}

.contact-item h4 {
  color: var(--primary-color);
  margin-bottom: 0.5rem;
  font-size: 1.1rem;
}

.contact-item p {
  color: var(--gray-dark);
}

.hours-list {
  list-style: none;
  padding: 0;
}

.hours-list li {
  display: flex;
  justify-content: space-between;
  padding: 0.3rem 0;
  border-bottom: 1px solid var(--gray);
}

.hours-list li:last-child {
  border-bottom: none;
}

.contact-social {
  margin-top: 1rem;
}

.social-links {
  display: flex;
  gap: 1rem;
  margin-top: 0.5rem;
}

.social-link {
  padding: 0.4rem 0.8rem;
  border-radius: 4px;
  background-color: var(--gray);
  color: var(--black);
  transition: background-color 0.3s, color 0.3s;
}

.social-link:hover {
  background-color: var(--primary-color);
  color: var(--white);
}

@media (max-width: 768px) {
  .contact-container {
    grid-template-columns: 1fr;
  }
  
  .contact-info {
    margin-bottom: 2rem;
  }
}
</style> 