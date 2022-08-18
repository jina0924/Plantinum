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
    username: localStorage.getItem('username') || '',
    leaf82Set: [],
    nickname: ''
  },

  getters: {
    isLoggedIn: state => !!state.token,
    currentUser: state => state.currentUser,
    authError: state => state.authError,
    authHeader: state => ({ Authorization: `Token ${state.token}`}),
    profile: state => state.profile,
    username: state => state.username,
    leaf82Set: state => state.leaf82Set,
    nickname: state => state.nickname
  },

  mutations: {
    SET_TOKEN: (state, token) => state.token = token,
    SET_CURRENT_USER: (state, user) => {
      state.currentUser = user
      state.username = user.username
    },
    SET_AUTH_ERROR: (state, error) => state.authError = error,
    SET_PROFILE: (state, profile) => {
      state.profile = profile,
      state.leaf82Set = profile.leaf82_set
    },
    SET_NICKNAME: (state, nickname) => state.nickname = nickname
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
        console.log()
        if(!!err.response.data.username && err.response.data.username[0] === '해당 사용자 이름은 이미 존재합니다.') {
          alert('해당 사용자 이름은 이미 존재합니다.')
        } else if (!!err.response.data.email && err.response.data.email[0] === '유효한 이메일 주소를 입력하십시오.') {
          alert('유효한 이메일 주소를 입력하십시오.')
        } else if (!!err.response.data.email && err.response.data.email[0] === '이미 이 이메일 주소로 등록된 사용자가 있습니다.') {
          alert('이미 등록된 메일입니다.')
        } else if (!!err.response.data.non_field_errors && err.response.data.non_field_errors[0] === '두 개의 패스워드 필드가 서로 맞지 않습니다.') {
          alert('패스워드가 일치하지 않습니다.')
        } else if (!!err.response.data.password1 && err.response.data.password1[0] === '비밀번호가 너무 일상적인 단어입니다.') {
          alert('비밀번호가 단순합니다. 복잡한 비밀번호를 입력해주세요.')
        } else if (!!err.response.data.password1 && err.response.data.password1[0] === '비밀번호가 전부 숫자로 되어 있습니다.') {
          alert('비밀번호가 전부 숫자로 되어 있습니다.')
        }else {
          alert('다시 입력해주세요.')
        }
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
        alert('다시 한 번 작성해주세요.')
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
        .then(res => {
          commit('SET_CURRENT_USER', res.data)
          localStorage.setItem('username', res.data.username)
        })
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
          console.log(err.response.data)
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
    },
    signout({ dispatch , getters }) {
      if (confirm('정말로 탈퇴하시겠습니까?')) {
        axios({
          url: drf.accounts.signout(),
          method: 'delete',
          headers: getters.authHeader
        })
        .then(() =>{
          dispatch('removeToken')
          dispatch('resetCurrentUser')
          dispatch('resetProfile')
          alert('성공적으로 탈퇴되었습니다.')
          router.push({ name: 'home' })          
        })
        .catch(err => {
          console.log(err)
        })
      }
    },

    fetchNickname({ getters }, username) {
      axios({
        url: drf.accounts.nickname(username),
        method: 'get',
        headers: getters.authHeader,
      })
      // .then(res => {
      //   commit('SET_NICKNAME', res.data)
      // })
      // .catch(err => console.log(err))
      .then(res => {
        return res.data
      })
    },
  }
}