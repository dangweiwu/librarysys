import Vue from 'vue'
import App from './App.vue'


import VueRouter from 'vue-router';
import Routers from './router.js';
import iView from 'iview';
import 'iview/dist/styles/iview.css';

Vue.use(VueRouter);
Vue.use(iView);

const RouterConfig = {
    routes: Routers
};

const router = new VueRouter(RouterConfig);

new Vue({
  el: '#app',
  router: router,
  render: h => h(App)
})
