import axios from 'axios'
import drf from '@/api/drf'
// import router from '@/router'

export const Leaf82 = {
  state: {
    leaf82Sell: [],
    leaf82Buy: [],
    sido: [],
    sigungu: [],
    searchList: []
    // 상세정보는 url로 created로 받아오자
  },
  getters: {
    sido: state => state.sido,
    sigungu: state => state.sigungu,
    searchList: state => state.searchList
  },
  mutations: {
    SET_SIDO: (state, sido) => state.sido = sido,
    SET_SIGUNGU: (state, sigungu) => state.sigungu = sigungu,
    SET_SEARCHLIST: (state, searchList) => state.searchList = searchList
  },
  actions: {
    fetchLeaf82({ commit }, params) {
      // sell
      axios({
        url: drf.leaf82.leaf82Sell(),
        method: 'get',
        params,
      })
      .then(res => {
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
        commit('SET_SIGUNGU', res.data)
      })
    },
    searchAll({ commit }, params) {
      axios({
        url: drf.leaf82.searchAll(),
        method: 'get',
        params
      })
      .then(res => {
        commit('SET_SEARCHLIST', res.data)
      })
    }
  },
}