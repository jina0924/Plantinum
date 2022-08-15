//import router from '@/router'
//import axios from 'axios'
//import drf from '@/api/drf'



export const Messenger = {
  state: {
    receiver : -1,
    fromDetail:0,
  },
  getters: {
    receiver : state => state.receiver
  },
  mutations: {
    SET_RECEIVER : (state,pk) => state.receiver = pk
  },
  actions: {
    setReceiver({commit},pk){
      commit("SET_RECEIVER",pk);
    },
    // 1. 새로고침
    fetchReceiver({ dispatch },pk){
      dispatch("setReceiver",pk);
    },
  }, 
}