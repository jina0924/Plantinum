import Vue from 'vue'
import Vuex from 'vuex'

import createPersistedState from "vuex-persistedstate"

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    uid : ""
  },
  mutations: {
    changeid(state,data){
      state.uid = data;
    }
  },
  actions: {
  },
  modules: {
  },
  plugins:[
    createPersistedState({
      paths:["uid"]
    })
  ]
})
