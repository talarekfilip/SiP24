<template>
  <div class="testimonial-card">
    <div class="stars">
      <span v-for="n in 5" :key="n" :class="{ 'star-filled': n <= testimonial.rating }">★</span>
    </div>
    <p class="review-text">"{{ testimonial.text }}"</p>
    <p class="review-author">- {{ testimonial.author }}</p>
    <p class="review-date" v-if="showDate">{{ formatDate(testimonial.created_at) }}</p>
  </div>
</template>

<script lang="ts">
import { defineComponent, PropType } from 'vue';
import type { Testimonial } from '@/api';

export default defineComponent({
  name: 'TestimonialCard',
  props: {
    testimonial: {
      type: Object as PropType<Testimonial>,
      required: true
    },
    showDate: {
      type: Boolean,
      default: false
    }
  },
  setup() {
    const formatDate = (dateString: string): string => {
      const date = new Date(dateString);
      return new Intl.DateTimeFormat('pl-PL', { 
        year: 'numeric', 
        month: 'long', 
        day: 'numeric' 
      }).format(date);
    };
    
    return {
      formatDate
    };
  }
});
</script>

<style scoped>
.testimonial-card {
  background-color: var(--white);
  border-radius: 8px;
  padding: 1.5rem;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
  transition: transform 0.3s;
}

.testimonial-card:hover {
  transform: translateY(-5px);
}

.stars {
  color: var(--gray);
  font-size: 1.2rem;
  margin-bottom: 1rem;
}

.star-filled {
  color: var(--primary-color);
}

.review-text {
  color: var(--black);
  font-style: italic;
  margin-bottom: 1rem;
  line-height: 1.5;
}

.review-author {
  color: var(--gray-dark);
  font-weight: 600;
  text-align: right;
}

.review-date {
  color: var(--gray-dark);
  font-size: 0.8rem;
  text-align: right;
  margin-top: 0.5rem;
}
</style> 