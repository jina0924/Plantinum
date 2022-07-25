import axios from 'axios'
import drf from '@/api/drf'

export const Myplant = {
  state: {
    myplant: []
  },
  getters: {
    myplant: state => state.myplant,
  },
  mutations: {
    SET_MYPLANT: (state, myplant) => state.myplant = myplant,
  },
  actions: {
    setMyplant({ commit, getters }, usernickname) {
      axios ({
        url : drf.myplant.all(usernickname),
        method : 'get',
        headers : getters.authHeader,
      })
      .then(res => commit('SET_MYPLANT', res.data))
      .catch(err => console.log(err.response))
    }
  },  
}