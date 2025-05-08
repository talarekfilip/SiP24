<template>
  <header class="navbar">
    <div class="container">
      <div class="logo-container">
        <router-link to="/" class="logo">SiP24<span class="logo-accent">.pl</span></router-link>
      </div>
      <nav>
        <ul class="nav-links">
          <li v-for="tab in tabs" :key="tab.id">
            <router-link :to="tab.path" active-class="active">
              {{ tab.name }}
            </router-link>
          </li>
        </ul>
      </nav>
    </div>
  </header>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import type { NavTab } from '@/api'

export default defineComponent({
  name: 'NavBar',
  setup() {
    const tabs: NavTab[] = [
      { id: 'home', name: 'Strona główna', path: '/' },
      { id: 'service', name: 'Usługi', path: '/uslugi' },
      { id: 'contact', name: 'Kontakt', path: '/kontakt' },
      { id: 'localization', name: 'Lokalizacja', path: '/lokalizacja' }
    ]
    
    return {
      tabs
    }
  }
})
</script>

<style scoped>
.navbar {
  background-color: var(--white);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  padding: 1rem 0;
  position: sticky;
  top: 0;
  z-index: 100;
}

.navbar .container {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo-container {
  display: flex;
  align-items: center;
}

.logo {
  font-size: 1.8rem;
  font-weight: 700;
  color: var(--black);
  text-decoration: none;
}

.logo-accent {
  color: var(--primary-color);
}

.nav-links {
  display: flex;
  list-style: none;
  gap: 1.5rem;
}

.nav-links a {
  color: var(--gray-dark);
  font-weight: 500;
  text-decoration: none;
  transition: color 0.3s;
  padding: 0.5rem 0;
}

.nav-links a:hover, .nav-links a.active {
  color: var(--primary-color);
}

@media (max-width: 768px) {
  .navbar .container {
    flex-direction: column;
    gap: 1rem;
  }
  
  .nav-links {
    gap: 1rem;
  }
}
</style> 