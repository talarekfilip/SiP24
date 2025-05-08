<template>
  <div class="home-view">
    <section class="hero">
      <div class="container">
        <h2>Profesjonalny serwis komputerowy</h2>
        <p>Naprawa komputerów, laptopów oraz urządzeń peryferyjnych.</p>
        <router-link to="/kontakt" class="btn-primary">Skontaktuj się z nami</router-link>
      </div>
    </section>

    <section class="services-preview">
      <div class="container">
        <h3>Nasze usługi</h3>
        <div class="grid service-cards">
          <ServiceCard 
            v-for="service in featuredServices" 
            :key="service.id" 
            :service="service" 
          />
        </div>
        <div class="text-center">
          <router-link to="/uslugi" class="btn-secondary">Zobacz wszystkie usługi</router-link>
        </div>
      </div>
    </section>

    <section class="testimonials">
      <div class="container">
        <h3>Opinie klientów</h3>
        <div class="grid testimonial-container">
          <TestimonialCard 
            v-for="testimonial in testimonials" 
            :key="testimonial.id" 
            :testimonial="testimonial" 
          />
        </div>
      </div>
    </section>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from 'vue';
import ServiceCard from '@/components/ServiceCard.vue';
import TestimonialCard from '@/components/TestimonialCard.vue';
import { getServices, getTestimonials } from '@/api';
import type { Service, Testimonial } from '@/api';

export default defineComponent({
  name: 'HomeView',
  components: {
    ServiceCard,
    TestimonialCard
  },
  setup() {
    const featuredServices = ref<Service[]>([]);
    const testimonials = ref<Testimonial[]>([]);
    const isLoading = ref(true);

    const fetchFeaturedServices = async () => {
      try {
        const response = await getServices({ featured: true, limit: 3 });
        featuredServices.value = response.data;
      } catch (error) {
        console.error('Błąd podczas pobierania usług:', error);
      }
    };

    const fetchTestimonials = async () => {
      try {
        const response = await getTestimonials({ limit: 3 });
        testimonials.value = response.data;
      } catch (error) {
        console.error('Błąd podczas pobierania opinii:', error);
      } finally {
        isLoading.value = false;
      }
    };

    onMounted(() => {
      fetchFeaturedServices();
      fetchTestimonials();
    });

    return {
      featuredServices,
      testimonials,
      isLoading
    };
  }
});
</script>

<style scoped>
.hero {
  background-color: var(--white);
  padding: 4rem 0;
  text-align: center;
  margin-bottom: 2rem;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
}

.hero h2 {
  color: var(--black);
  margin-bottom: 1rem;
  font-size: 2.5rem;
}

.hero p {
  font-size: 1.2rem;
  margin-bottom: 2rem;
  color: var(--gray-dark);
  max-width: 600px;
  margin-left: auto;
  margin-right: auto;
}

.services-preview, .testimonials {
  padding: 3rem 0;
  margin-bottom: 2rem;
}

.services-preview h3, .testimonials h3 {
  text-align: center;
  margin-bottom: 2rem;
  color: var(--black);
  font-size: 1.8rem;
}

.service-cards {
  margin-bottom: 2rem;
}

.text-center {
  text-align: center;
}

.btn-secondary {
  display: inline-block;
  padding: 0.8rem 1.5rem;
}
</style> 