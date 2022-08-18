import { createStore } from 'vuex'
import { Account } from './modules/accounts'
import { Myplant } from './modules/myplant'
import { Leaf82 } from './modules/leaf82'
import { Timer } from './modules/timer'
import { Messenger } from './modules/messenger'
import createPersistedState from "vuex-persistedstate"

export default createStore({
  modules: { 
    Account, Myplant, Leaf82, Timer, Messenger,
  },
  plugins: [createPersistedState({
    paths: ['Timer',]
  })],
})