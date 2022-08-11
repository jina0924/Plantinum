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

    resetCurrentUser({ commit }) {
      commit('SET_CURRENT_USER', {})
    },

    resetProfile({ commit }) {
      commit('SET_PROFILE', {})
    },

    resetAuthError({ commit }) {
      commit('SET_AUTH_ERROR', null)
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
        dispatch('fetchProfile')
        dispatch('resetAuthError')
        router.push({ name: 'home' })
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
        dispatch('fetchProfile')
        dispatch('resetAuthError')
        router.push({ name: 'home' })
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
        dispatch('resetCurrentUser')
        dispatch('resetProfile')
        alert('logout 되었습니다')
        router.push({ name: 'home' })
      })
      // 에러 발생 시 어떻게 할 지 고민해야 함
      .catch(err => {
        alert('잘못된 접근입니다.')
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

    fetchAuthError({ commit }, authState) {
      commit('SET_AUTH_ERROR', authState)
    },

    fetchProfile({ commit, getters },) {
      axios({
        url: drf.accounts.profile(),
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
    
    updateProfile({ commit, getters, }, info) {
      axios({
        url: drf.accounts.updateProfile(),
        method: 'put',
        data: info,
        headers: {
          ...getters.authHeader,
          'Content-Type': 'multipart/form-data',
        },
      })
        .then(res => {
          commit('SET_PROFILE', res.data)
          router.push({ name: 'profile' })
        })
        // .then(() => {
        //   dispatch('fetchProfile')
        //   router.push({ name: 'profile' })
        // })
        .catch(err => {
          commit('SET_AUTH_ERROR', err.response.data)
          router.push({ name: 'updateProfile' })
          if (err.response.status === 401) {
            router.push({ name: 'updateProfile' })
          }
        })
    },

    changePassword({getters, dispatch}, credentials) {
      axios({
        url : drf.accounts.changePassword(),
        method : 'post',
        data : credentials,
        headers : getters.authHeader
      })
        .then(res => {
          const token = res.data.key
          dispatch('saveToken', token)
          dispatch('fetchCurrentUser')
          router.push({ name: 'profile' })
          alert('비밀번호가 변경되었습니다.')
        })
        .catch(err => {
          console.log(err)
          if (err.response.status === 401) {
            router.push({ name: 'updatepassword' })
          }
        })
    } 
  }
}