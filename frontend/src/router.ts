import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'home',
    component: () => import('./views/HomeView.vue')
  },
  {
    path: '/uslugi',
    name: 'service',
    component: () => import('./views/ServiceView.vue')
  },
  {
    path: '/kontakt',
    name: 'contact',
    component: () => import('./views/ContactView.vue')
  },
  {
    path: '/lokalizacja',
    name: 'localization',
    component: () => import('./views/LocalizationView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior() {
    // Always scroll to top
    return { top: 0 }
  }
})

export default router 