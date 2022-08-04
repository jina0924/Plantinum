import axios from 'axios'
import drf from '@/api/drf'
import router from '@/router'

export const Leaf82 = {
  state: {
    sido: [],
    sigungu: [],
    searchList: [],
    leaf82Detail: {}
    // 상세정보는 url로 created로 받아오자
  },
  getters: {
    sido: state => state.sido,
    sigungu: state => state.sigungu,
    searchList: state => state.searchList,
    leaf82Detail: state => state.leaf82Detail
  },
  mutations: {
    SET_SIDO: (state, sido) => state.sido = sido,
    SET_SIGUNGU: (state, sigungu) => state.sigungu = sigungu,
    SET_SEARCHLIST: (state, searchList) => state.searchList = searchList,
    SET_LEAF82DETAIL: (state, leaf82Detail) => state.leaf82Detail = leaf82Detail
  },
  actions: {
    resetSigungu({ commit }) {
      commit('SET_SIGUNGU', [])
    },

    fetchLeaf82({ commit }) {
      axios({
        url: drf.leaf82.leaf82(),
        method: 'get',
      })
      .then(res => {
        console.log(res)
        commit('SET_SEARCHLIST', res.data)
      })
      .catch(err => {
        console.log(err)
      })
    },

    fetchSido({ commit }) {
      axios({
        url: drf.leaf82.sido(),
        method: 'get'
      })
      .then (res => {
        commit('SET_SIDO', res.data)
      })
    },

    fetchSigungu({ commit }, sido) {
      axios({
        url: drf.leaf82.sigungu(sido),
        method: 'get'
      })
      .then(res=> {
        console.log(res)
        commit('SET_SIGUNGU', res.data)
      })

    },
    search({ commit }, params) {
      axios({
        url: drf.leaf82.search(),
        method: 'get',
        params
      })
      .then(res => {
        console.log(res)
        commit('SET_SEARCHLIST', res.data)
      })
    },

    // 게시글 등록
    createLeaf82({ commit, getters }, credentials) {
      axios({
        url: drf.leaf82.new(),
        method: 'post',
        data: credentials,
        headers: getters.authHeader
      })
      .then(res => {
        console.log(res)
        commit('SET_LEAF82DETAIL', res.data)
        router.push({
          name: 'leaf82Detail',
          params: { username: getters.currentUser.username , posting_addr: getters.leaf82Detail.posting_addr }
        })
      })
      .catch(err => {
        alert('잘못된 접근입니다.')
        console.log(err)
      })
    },

    fetchLeaf82Detail({ commit, }, info) {
      axios({
        url: drf.leaf82.detail(info),
        method: 'get',
      })
      .then(res => {
        console.log(res)
        commit('SET_LEAF82DETAIL', res.data)
      })
      .catch(err => {
        console.log(err)
      })
    }
  },
}