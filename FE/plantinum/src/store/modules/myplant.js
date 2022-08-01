import axios from 'axios'
import drf from '@/api/drf'

export const Myplant = {
  state: {
    myplants: [],
    myplant: {},
  },
  getters: {
    myplants: state => state.myplants,
    mypalnt: state => state.myplant,
  },
  mutations: {
    SET_MYPLANTS: (state, myplants) => state.myplants = myplants,
    SET_MYPLANT: (state, myplant) => state.myplant = myplant,
  },
  actions: {
    fetchMyplants({ commit, getters }, { username }) {
      axios ({
        url : drf.myplant.myplant(username),
        method : 'get',
        headers : getters.authHeader,
      })
      .then(res => commit('SET_MYPLANTS', res.data))
      .catch(err => console.log(err.response))
    },

    createMyplant({ commit, getters }, myplant) {
      axios({
        url: drf.myplant.newMyplant(),
        method: 'post',
        data: myplant,
        headers: getters.authHeader,
      })
      .then(res => {
        console.log(res.data)
        console.log(commit)
        // commit('SET_MYPLANT', res.data)
      })
      .catch(error => {
        console.log(error.response)
      })
    }
  },
}