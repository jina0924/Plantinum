import { createRouter, createWebHistory } from 'vue-router'
<<<<<<< HEAD
import HomeView from '../views/HomeView.vue'
=======
import HomeView from '@/views/HomeView.vue'
import MyplantView from '@/views/MyplantView.vue'
import LoginView from '@/views/LoginView.vue'
import LogoutView from '@/views/LogoutView.vue'
import SignupView from '@/views/SignupView.vue'
import ProfileView from '@/views/ProfileView.vue'
import Leaf82View from '@/views/Leaf82View.vue'
import MessengerView from '@/views/MessengerView.vue'
>>>>>>> feature/login

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
<<<<<<< HEAD
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  }
=======
    path: '/myplant',
    name: 'myplant',
    component: MyplantView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/logout',
    name: 'logout',
    component: LogoutView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignupView
  },
  {
    path: '/profile',
    name: 'profile',
    component: ProfileView
  },
  {
    path: '/leaf82',
    name: 'leaf82',
    component: Leaf82View
  },
  {
    path: '/messenger',
    name: 'messenger',
    component: MessengerView
  },
>>>>>>> feature/login
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
