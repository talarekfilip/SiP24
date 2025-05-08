<template>
  <div class="app">
    <NavBar />
    
    <main class="main-content">
      <router-view />
    </main>
    
    <footer class="footer">
      <div class="container">
        <div class="footer-content">
          <div class="footer-logo">
            <h2>SiP24<span class="logo-accent">.pl</span></h2>
            <p>Profesjonalny serwis komputerowy</p>
          </div>
          
          <div class="footer-links">
            <h3>Szybki dostęp</h3>
            <ul>
              <li><router-link to="/">Strona główna</router-link></li>
              <li><router-link to="/uslugi">Usługi</router-link></li>
              <li><router-link to="/kontakt">Kontakt</router-link></li>
              <li><router-link to="/lokalizacja">Lokalizacja</router-link></li>
            </ul>
          </div>
          
          <div class="footer-contact">
            <h3>Kontakt</h3>
            <p>Tel: +48 123 456 789</p>
            <p>Email: kontakt@sip24.pl</p>
            <p>Adres: ul. Przykładowa 24, 00-000 Warszawa</p>
          </div>
        </div>
        
        <div class="copyright">
          <p>&copy; {{ new Date().getFullYear() }} SiP24.pl. Wszelkie prawa zastrzeżone.</p>
        </div>
      </div>
    </footer>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import NavBar from '@/components/NavBar.vue'

export default defineComponent({
  name: 'App',
  components: {
    NavBar
  }
})
</script>

<style>
/* Import main CSS */
@import './assets/main.css';

.main-content {
  min-height: calc(100vh - 250px);
  padding-bottom: 3rem;
}

.footer {
  background-color: var(--white);
  padding: 2rem 0 1rem;
  box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.05);
}

.footer-content {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
  margin-bottom: 2rem;
}

.footer-logo h2 {
  font-size: 1.8rem;
  color: var(--black);
  margin-bottom: 0.5rem;
}

.logo-accent {
  color: var(--primary-color);
}

.footer-logo p {
  color: var(--gray-dark);
}

.footer-links h3, .footer-contact h3 {
  font-size: 1.2rem;
  margin-bottom: 1rem;
  color: var(--black);
}

.footer-links ul {
  list-style: none;
  padding: 0;
}

.footer-links li {
  margin-bottom: 0.5rem;
}

.footer-links a {
  color: var(--gray-dark);
  text-decoration: none;
  transition: color 0.3s;
}

.footer-links a:hover {
  color: var(--primary-color);
}

.footer-contact p {
  margin-bottom: 0.5rem;
  color: var(--gray-dark);
}

.copyright {
  text-align: center;
  padding-top: 1.5rem;
  border-top: 1px solid var(--gray);
  color: var(--gray-dark);
  font-size: 0.9rem;
}

@media (max-width: 768px) {
  .footer-content {
    grid-template-columns: 1fr;
    text-align: center;
  }
  
  .footer-logo {
    margin-bottom: 1rem;
  }
}
</style> 