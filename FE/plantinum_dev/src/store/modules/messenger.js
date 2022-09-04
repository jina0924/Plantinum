//import router from '@/router'
//import axios from 'axios'
//import drf from '@/api/drf'



export const Messenger = {
  state: {
    receiver : -1,
    fromDetail:0,
    leaf82_plant : -1,
  },
  getters: {
    receiver : state => state.receiver,
    leaf82_plant : state => state.leaf82_plant

  },
  mutations: {
    SET_RECEIVER : (state,pk) => state.receiver = pk,
    SET_LEAF82_PLANT : (state, plantname) => state.leaf82_plant = plantname
  },
  actions: {
    setReceiver({commit},pk){
      commit("SET_RECEIVER",pk);
    },
    // 1. 새로고침
    fetchReceiver({ dispatch },pk){
      dispatch("setReceiver",pk);
    },

    setLeaf82Plant({ commit }, plantname) {
      commit("SET_LEAF82_PLANT", plantname)
    }
  }, 
}