import router from '@/router'
import axios from 'axios'
import drf from '@/api/drf'

export const Account = {
  // state: {
  // },
  // getters: {
  // },
  // mutations: {
  // },
  // actions: {
  // },
  state: {
    token: localStorage.getItem('token') || '' ,
    currentUser: {},
    authError: null,
    profile: {},
  },

  getters: {
    isLoggedIn: state => !!state.token,
    currentUser: state => state.currentUser,
    authError: state => state.authError,
    authHeader: state => ({ Authorization: `Token ${state.token}`}),
    profile: state => state.profile,
  },

  mutations: {
    SET_TOKEN: (state, token) => state.token = token,
    SET_CURRENT_USER: (state, user) => state.currentUser = user,
    SET_AUTH_ERROR: (state, error) => state.authError = error,
    SET_PROFILE: (state, profile) => state.profile = profile,
  },

  actions: {
    saveToken({ commit }, token) {
      commit('SET_TOKEN', token)
      localStorage.setItem('token', token)
    },

    removeToken({ commit }) {
      commit('SET_TOKEN', '')
      localStorage.setItem('token', '')
    },

    signup({ commit, dispatch }, credentials) {
      axios({
        url: drf.accounts.signup(),
        method: 'post',
        data: credentials
      })
      .then(res => {
        const token = res.data.key
        dispatch('saveToken', token)
        dispatch('fetchCurrentUser')
        // router.push({ name: '' })
      })
      .catch(err => {
        console.error(err.response.data)
        commit('SET_AUTH_ERROR', err.response.data)
      })
    },

    login({ commit, dispatch }, credentials) {
      axios ({
        url: drf.accounts.login(),
        method: 'post',
        data: credentials
      })
      .then(res => {
        const token = res.data.key
        dispatch('saveToken', token)
        dispatch('fetchCurrentUser')
        // router.push({ name: '' })
      })
      .catch(err => {
        console.error(err.response.data)
        commit('SET_AUTH_ERROR', err.response.data)
      })
    },

    logout({ getters, dispatch }) {
      axios({
        url: drf.accounts.logout(),
        method: 'post',
        headers: getters.authHeader,
      })
      .then(() => {
        dispatch('removeToken')
        // alert('logout 되었습니다')
        // router.push({ name: '' })
      })
      // 에러 발생 시 어떻게 할 지 고민해야 함
      .catch(err => {
        console.log(err.response)
      })
    },

    fetchCurrentUser({ commit, getters, dispatch }) {
      if (getters.isLoggedIn) {
        axios({
          url: drf.accounts.currentUserInfo(),
          method: 'get',
          headers: getters.authHeader,
        })
        .then(res => commit('SET_CURRENT_USER', res.data))
        .catch(err => {
          if (err.response.status === 401) {
            dispatch('removeToken')
            router.push({ name: 'login' })
          }
        })
      }
    },

    fetchProfile({ commit, getters }, { nickname }) {
      axios({
        url: drf.accounts.profile(nickname),
        method: 'get',
        headers: getters.authHeader,
      })
      .then(res => {
        commit('SET_PROFILE', res.data)
      })
      .catch(err => {
        if (err.response.status === 404) {
          router.push({ name: 'NotFound404' })
        }
      })
    },
    
    updateProfile({ commit, getters }, { nickname, email, address, phone_number, profile_img }) {
      const info = { nickname, email, address, phone_number, profile_img }
      axios({
        url: drf.accounts.updateProfile(),
        method: 'put',
        data: info,
        headers: getters.authHeader
      })
        .then(res => {
          commit('SET_PROFILE', res.data)
        })
        .catch(err => {
          if (err.response.status === 401) {
            router.push({ name: 'updateProfile' })
          }
        })
    },

    changePassword({getters, dispatch}, user_pk, new_password1, new_password2) {
      console.log(credentials)
      const credentials = {
        user_pk : user_pk,
        new_password1 : new_password1,
        new_password2 : new_password2,
      }
      axios({
        url : drf.accounts.changePassword(),
        method : 'post',
        data : credentials,
        headers : getters.authHeader
      })
        .then(res => {
          console.log(res)
          const token = res.data.key
          dispatch('saveToken', token)
          dispatch('fetchCurrentUser')
        })
        .catch(err => {
          if (err.response.status === 401) {
            router.push({ name: 'changePassword' })
          }
        })
    } 
  }
}