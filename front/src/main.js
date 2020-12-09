import Vue from 'vue'
import Vuesax from 'vuesax'
import 'vuesax/dist/vuesax.css'
import App from './App.vue'
import { library } from '@fortawesome/fontawesome-svg-core'
import { fas } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import YmapPlugin from 'vue-yandex-maps'

const settings = {
  apiKey: '',
  lang: 'ru_RU',
  coordorder: 'latlong',
  version: '2.1'
}

Vue.use(YmapPlugin, settings)
library.add(fas)
Vue.component('font-awesome-icon', FontAwesomeIcon)
Vue.config.productionTip = false
Vue.use(Vuesax, {
  colors:{
    primary:'#3E454D',
    dark:'#1E2327',
  }
})

new Vue({
  render: h => h(App),
}).$mount('#app')
