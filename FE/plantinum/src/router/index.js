import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import MyplantView from '@/views/MyplantView.vue'
import LoginView from '@/views/LoginView.vue'
import LogoutView from '@/views/LogoutView.vue'
import SignupView from '@/views/SignupView.vue'
import ProfileView from '@/views/ProfileView.vue'
import Leaf82View from '@/views/Leaf82View.vue'
import MessengerView from '@/views/MessengerView.vue'
import UpdateProfileView from '@/views/UpdateProfileView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
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
    path: '/profile/update',
    name: 'updateprofile',
    component: UpdateProfileView
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
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
