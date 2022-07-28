import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import LoginView from '@/views/LoginView.vue'
// import LogoutView from '@/views/LogoutView.vue'
import SignupView from '@/views/SignupView.vue'
import ProfileView from '@/views/ProfileView.vue'
import UpdatePasswordView from '@/views/UpdatePasswordView.vue'

import MyplantView from '@/views/MyplantView.vue'
import MyplantNewView from '@/views/MyplantNewView.vue'
import MyplantDetailView from '@/views/MyplantDetailView.vue'
import MyplantEditView from '@/views/MyplantEditView.vue'

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
    path: '/login',
    name: 'login',
    component: LoginView
  },
  // {
  //   path: '/logout',
  //   name: 'logout',
  //   component: LogoutView
  // },
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
    path: '/password/update',
    name: 'updatepassword',
    component: UpdatePasswordView
  },
  // 내 식물
  {
    path: '/myplant/:usernickname?',
    name: 'myplant',
    component: MyplantView
  },
  {
    path: '/myplant/new',
    name: 'myplantNew',
    component: MyplantNewView
  },
  {
    path: '/myplant/:usernickname/:plantPk',
    name: 'myplantDetail',
    component: MyplantDetailView
  },
  {
    path: '/myplant/:plantPk/edit',
    name: 'myplantEdit',
    component: MyplantEditView
  },
  // 잎팔이
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

// 페이지 이동할 때마다 검사함
// router.beforeEach((to, from, next) => {
//   store.commit('SET_AUTH_ERROR', null)

//   const { isLoggedIn } = store.getters

//   const noAuthPages = ['login', 'signup', 'home', 'leaf82', 'NotFound404',]
  
//   const isAuthRequired = !noAuthPages.includes(to.name)

//   if (isAuthRequired && !isLoggedIn) {
//     alert('로그인 필요합니다. 로그인 페이지로 이동합니다.')
//     next({ name: 'login' })
//   } else {
//     next()
//   }
// })

export default router
