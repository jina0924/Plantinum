import { createStore } from 'vuex'
import { Account } from './modules/accounts'
import { Myplant } from './modules/myplant'
import { Leaf82 } from './modules/leaf82'
import { Timer } from './modules/timer'
import { Messenger } from './modules/messenger'
import createPersistedState from "vuex-persistedstate"
import { Viewport } from './modules/viewport'

// import accounts from './modules/accounts'

export default createStore({
  modules: { 
    Account, Myplant, Leaf82, Timer, Messenger, Viewport
  },
  plugins: [createPersistedState({
    // paths: ['Account', 'Myplant',]
    paths: ['Timer',]
    // storage: window.sessionStorage,
    // reducer : state => ({
    //   otptimer: 20,
    // })
  })],
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
