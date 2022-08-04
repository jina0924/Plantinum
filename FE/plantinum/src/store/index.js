import { createStore } from 'vuex'
import { Account } from './modules/accounts'
import { Myplant } from './modules/myplant'
import { Leaf82 } from './modules/leaf82'
// import createPersistedState from "vuex-persistedstate"

// import accounts from './modules/accounts'

export default createStore({
  modules: { 
    Account, Myplant, Leaf82
  },
  // plugins: [createPersistedState({
  //   paths: ['Account', 'Myplant',]
  // })],
})


// import Vue from 'vue'
// import Vuex from 'vuex'

// Vue.use(Vuex)

// export default new Vuex.Store({
//   state: {
//   },
//   getters: {
//   },
//   mutations: {
//   },
//   actions: {
//   },
//   modules: {
//   }
// })
