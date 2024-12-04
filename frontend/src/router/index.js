import { createRouter, createWebHashHistory } from 'vue-router'
import Home from '@/pages/Home'
import Login from  '@/pages/Login'

const routes = [
  {
      path:'/',
      component: Home
  },
  {
      path:'/login',
      component: Login
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
