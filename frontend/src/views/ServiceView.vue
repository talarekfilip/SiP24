<template>
  <div class="service-view">
    <div class="container">
      <h2>Nasze usługi</h2>
      
      <div v-if="isLoading" class="loading">
        <p>Ładowanie usług...</p>
      </div>
      
      <div v-else>
        <div v-for="category in categories" :key="category.id" class="service-category">
          <h3>{{ category.name }}</h3>
          <div class="grid service-grid">
            <ServiceCard 
              v-for="service in getServicesByCategory(category.id)" 
              :key="service.id" 
              :service="service"
              :showDetails="true"
            />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, computed, onMounted } from 'vue';
import ServiceCard from '@/components/ServiceCard.vue';
import { getServices, getServiceCategories } from '@/api';
import type { Service, ServiceCategory } from '@/api';

export default defineComponent({
  name: 'ServiceView',
  components: {
    ServiceCard
  },
  setup() {
    const services = ref<Service[]>([]);
    const categories = ref<ServiceCategory[]>([]);
    const isLoading = ref(true);

    const fetchServices = async () => {
      try {
        const [servicesResponse, categoriesResponse] = await Promise.all([
          getServices(),
          getServiceCategories()
        ]);
        
        services.value = servicesResponse.data;
        categories.value = categoriesResponse.data;
      } catch (error) {
        console.error('Błąd podczas pobierania usług:', error);
      } finally {
        isLoading.value = false;
      }
    };

    const getServicesByCategory = (categoryId: number) => {
      return services.value.filter(service => service.category_id === categoryId);
    };

    onMounted(() => {
      fetchServices();
    });

    return {
      services,
      categories,
      isLoading,
      getServicesByCategory
    };
  }
});
</script>

<style scoped>
.service-view {
  padding: 2rem 0;
}

.service-view h2 {
  text-align: center;
  margin-bottom: 2rem;
  color: var(--black);
  font-size: 2rem;
}

.loading {
  text-align: center;
  padding: 3rem 0;
  color: var(--gray-dark);
}

.service-category {
  margin-bottom: 3rem;
}

.service-category h3 {
  color: var(--primary-color);
  margin-bottom: 1.5rem;
  font-size: 1.5rem;
  padding-bottom: 0.5rem;
  border-bottom: 2px solid var(--gray);
}

.service-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1.5rem;
}

@media (max-width: 768px) {
  .service-grid {
    grid-template-columns: 1fr;
  }
}
</style> 