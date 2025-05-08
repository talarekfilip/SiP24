<template>
  <div class="localization-view">
    <div class="container">
      <h2>Lokalizacja</h2>
      
      <div class="location-container">
        <div class="address-info">
          <div class="card">
            <h3>Znajdziesz nas pod adresem</h3>
            
            <div class="address">
              <p>SiP24.pl - Serwis Komputerowy</p>
              <p>ul. Przykładowa 24</p>
              <p>00-000 Warszawa</p>
            </div>
            
            <div class="directions">
              <h4>Jak do nas dojechać:</h4>
              
              <div class="direction-item">
                <h5>Komunikacja miejska</h5>
                <ul>
                  <li>Autobusy: 175, 178, 504, 518</li>
                  <li>Tramwaje: 10, 14, 18</li>
                  <li>Metro: stacja "Centrum Techniczne" (linia M2)</li>
                </ul>
              </div>
              
              <div class="direction-item">
                <h5>Samochodem</h5>
                <p>Parking dostępny przed budynkiem (bezpłatny dla klientów).</p>
              </div>
            </div>
          </div>
        </div>
        
        <div class="map-container">
          <div class="card">
            <div class="map-wrapper">
              <!-- Tu w rzeczywistości powinien być osadzony Google Maps lub inny serwis map -->
              <div class="map-placeholder">
                <p>Mapa lokalizacji SiP24.pl</p>
                <p class="map-address">ul. Przykładowa 24, 00-000 Warszawa</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'LocalizationView'
});
</script>

<style scoped>
.localization-view {
  padding: 2rem 0;
}

.localization-view h2 {
  text-align: center;
  margin-bottom: 2rem;
  color: var(--black);
  font-size: 2rem;
}

.location-container {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
}

.address-info h3 {
  color: var(--black);
  margin-bottom: 1.5rem;
  font-size: 1.5rem;
}

.address {
  margin-bottom: 2rem;
}

.address p {
  margin-bottom: 0.5rem;
  color: var(--gray-dark);
}

.address p:first-child {
  font-weight: 700;
  color: var(--black);
}

.directions h4 {
  color: var(--primary-color);
  margin-bottom: 1rem;
  font-size: 1.2rem;
}

.direction-item {
  margin-bottom: 1.5rem;
}

.direction-item h5 {
  color: var(--black);
  margin-bottom: 0.5rem;
  font-size: 1rem;
}

.direction-item ul {
  padding-left: 1.2rem;
  color: var(--gray-dark);
}

.direction-item ul li {
  margin-bottom: 0.3rem;
}

.direction-item p {
  color: var(--gray-dark);
}

.map-wrapper {
  height: 400px;
  width: 100%;
  border-radius: 8px;
  overflow: hidden;
}

.map-placeholder {
  height: 100%;
  background-color: #e9ecef;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  color: var(--gray-dark);
  font-size: 1.2rem;
}

.map-address {
  margin-top: 1rem;
  font-size: 1rem;
}

@media (max-width: 768px) {
  .location-container {
    grid-template-columns: 1fr;
  }
  
  .address-info {
    margin-bottom: 1rem;
  }
  
  .map-wrapper {
    height: 300px;
  }
}
</style> 