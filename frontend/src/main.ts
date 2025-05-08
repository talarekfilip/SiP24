import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import './assets/main.css'
import axios from 'axios'

// Konfiguracja Axios dla poprawnego kodowania
axios.defaults.headers.common['Accept'] = 'application/json;charset=UTF-8'
axios.defaults.headers.post['Content-Type'] = 'application/json;charset=UTF-8'

const app = createApp(App)
app.use(router)
app.mount('#app') 