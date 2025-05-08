<template>
  <div class="service-card">
    <div class="service-icon">{{ getServiceIcon(service.name) }}</div>
    <h4>{{ service.name }}</h4>
    <p>{{ service.description }}</p>
    <div class="service-details" v-if="showDetails">
      <div class="service-price">Od {{ service.price_from }} zł</div>
      <div class="service-time">Szacowany czas: {{ service.estimated_time }}</div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, PropType } from 'vue';
import type { Service } from '@/api';

export default defineComponent({
  name: 'ServiceCard',
  props: {
    service: {
      type: Object as PropType<Service>,
      required: true
    },
    showDetails: {
      type: Boolean,
      default: false
    }
  },
  setup() {
    const getServiceIcon = (serviceName: string): string => {
      const nameLC = serviceName.toLowerCase();
      
      if (nameLC.includes('komputer')) return '🖥️';
      if (nameLC.includes('laptop')) return '💻';
      if (nameLC.includes('wirus')) return '🦠';
      if (nameLC.includes('diagnostyka')) return '🔍';
      if (nameLC.includes('czyszczenie')) return '🧹';
      if (nameLC.includes('instalacja')) return '💿';
      if (nameLC.includes('sieć') || nameLC.includes('siec')) return '🌐';
      if (nameLC.includes('napraw')) return '🔧';
      if (nameLC.includes('aktualizacja')) return '🔄';
      if (nameLC.includes('strona') || nameLC.includes('www')) return '🌍';
      if (nameLC.includes('aplikacja')) return '📱';
      if (nameLC.includes('matryc')) return '📺';
      if (nameLC.includes('płyta') || nameLC.includes('plyta')) return '📟';
      
      return '💼'; // Default icon
    };
    
    return {
      getServiceIcon
    };
  }
});
</script>

<style scoped>
.service-card {
  background-color: var(--white);
  border-radius: 8px;
  padding: 1.5rem;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
  transition: transform 0.3s, box-shadow 0.3s;
  height: 100%;
  display: flex;
  flex-direction: column;
}

.service-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
}

.service-icon {
  font-size: 2.5rem;
  margin-bottom: 1rem;
}

.service-card h4 {
  color: var(--black);
  margin-bottom: 0.8rem;
  font-size: 1.2rem;
}

.service-card p {
  color: var(--gray-dark);
  margin-bottom: 1rem;
  flex-grow: 1;
}

.service-details {
  margin-top: auto;
  padding-top: 1rem;
  border-top: 1px solid var(--gray);
}

.service-price {
  font-weight: 700;
  color: var(--primary-color);
  margin-bottom: 0.3rem;
}

.service-time {
  font-size: 0.9rem;
  color: var(--gray-dark);
}
</style> 