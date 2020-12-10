import Vue from 'vue'
import Vuesax from 'vuesax'
import 'vuesax/dist/vuesax.css'
import VueRouter from 'vue-router'
import App from './App.vue'
import { library } from '@fortawesome/fontawesome-svg-core'
import { fas } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import YmapPlugin from 'vue-yandex-maps'
import MainPage from "@/components/pages/main/MainPage";
import SignupPage from "@/components/pages/signup/SignupPage";
import UpdateSignupPage from "@/components/pages/updsignup/UpdateSignupPage";
import CancelSignupPage from "@/components/pages/cancelsignup/CancelSignupPage";
import ViewSignupPage from "@/components/pages/viewsignup/ViewSignupPage";

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

const routes = [
  {path: '/', component: MainPage},
  {path: '/Signup', component: SignupPage},
  {path: '/Signup/:id/Update', component: UpdateSignupPage, props: true},
  {path: '/Signup/:id/Cancel', component: CancelSignupPage, props: true},
  {path: '/Signup/:id', component: ViewSignupPage, props: true},
]

const router = new VueRouter({
  mode: 'history',
  routes,
})

new Vue({
  router: router,
  render: h => h(App)
}).$mount('#app')
