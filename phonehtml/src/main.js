// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import FastClick from 'fastclick'
import VueRouter from 'vue-router'
import App from './App'
import Home from './components/HelloFromVux'
import  { LoadingPlugin, AlertPlugin} from 'vux'

import Message from '@/views/message'
import Books from '@/views/books'
import My from '@/views/my'
import store from '@/store'

Vue.use(VueRouter)

const routes = [{path: '/Message',component: Message},
{path:'/Books',component:Books},
{path:'/my',component:My},
{path:'/',component:App}]

const router = new VueRouter({
  routes
})

FastClick.attach(document.body)

Vue.config.productionTip = false


Vue.use(AlertPlugin)

/* eslint-disable no-new */
new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app-box')
