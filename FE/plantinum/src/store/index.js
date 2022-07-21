import { createStore } from 'vuex'
import { Account } from './modules/accounts'

// import accounts from './modules/accounts'

export default createStore({
  modules: { 
    Account
  }
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
