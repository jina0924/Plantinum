import axios from 'axios'
import drf from '@/api/drf'

export const Myplant = {
  state: {
    myplants: []
  },
  getters: {
    myplant: state => state.myplants,
  },
  mutations: {
    SET_MYPLANTS: (state, myplants) => state.myplants = myplants,
  },
  actions: {
    fetchMyplant({ commit, getters }, { username }) {
      axios ({
        url : drf.myplant.myplant(username),
        method : 'get',
        headers : getters.authHeader,
      })
      .then(res => commit('SET_MYPLANTS', res.data))
      .catch(err => console.log(err.response))
    }
  },  
}