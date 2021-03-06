import Vue from 'vue'
import Router from 'vue-router'
import Home from './components/Home.vue'

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/about',
      name: 'about',
      component: () => import('./components/About.vue')
    },
    {
      path: "/Contactt",
      name: "Contactt",
      component: () => import('./components/Contactt.vue')
    },
    {
      path: "/list",
      name: "list",
      component: () => import('./components/List.vue')
    },
    {
      path: "/manysearchlist",
      name: "manysearchlist",
      component: () => import("./components/Manysearchlist.vue")
    }
  ]
})
