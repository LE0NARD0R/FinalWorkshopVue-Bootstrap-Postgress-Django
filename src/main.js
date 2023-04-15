import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import '@/assets/bootstrap.min.css'
import '@/assets/bootstrap.bundle.min.js'
import 'material-icons/iconfont/material-icons.css'

const variables = {
    API_URL: 'http://127.0.0.1:8000/',
    PHOTO_URL : 'http://127.0.0.1:8000/photos/',
}

createApp(App).use(store).use(router).mount('#app')
