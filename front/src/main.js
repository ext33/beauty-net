import Vue from 'vue'
import Vuesax from 'vuesax'
import 'vuesax/dist/vuesax.css'
import VueRouter from 'vue-router'
import App from './App.vue'
import { library } from '@fortawesome/fontawesome-svg-core'
import { fas } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import YmapPlugin from 'vue-yandex-maps'
import {routes} from './router'

const settings = {
  apiKey: '',
  lang: 'ru_RU',
  coordorder: 'latlong',
  version: '2.1'
}

Vue.use(YmapPlugin, settings)
Vue.use(VueRouter)
library.add(fas)
Vue.component('font-awesome-icon', FontAwesomeIcon)
Vue.config.productionTip = false

Vue.use(Vuesax, {
  colors:{
    primary:'#3E454D',
    dark:'#1E2327',
  }
})

const router = new VueRouter({
  mode: 'history',
  routes,
})

new Vue({
  router: router,
  render: h => h(App)
}).$mount('#app')
