import axios from 'axios'
import drf from '@/api/drf'
import router from '@/router'

export const Myplant = {
  state: {
    myplants: [],
    myplant: {},
    plant_list: [],
    temp_OTP: null,
  },
  getters: {
    myplants: state => state.myplants,
    myplant: state => state.myplant,
    plant_list: state => state.plant_list,
    temp_OTP: state => state.temp_OTP,
  },
  mutations: {
    SET_MYPLANTS: (state, myplants) => state.myplants = myplants,
    SET_MYPLANT: (state, myplant) => state.myplant = myplant,
    SET_PLANTLIST: (state, plant_list) => state.plant_list = plant_list,
    SET_OTP: (state, otp) => state.temp_OTP = otp,
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

    searchPlant({ commit, getters }) {
      axios ({
        url : drf.myplant.plantSearch(),
        method: 'get',
        headers : getters.authHeader,
      })
      .then(res => commit('SET_PLANTLIST', res.data))
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
        commit('SET_MYPLANT', res.data)
        console.log(getters.currentUser.username)
        router.push({
          name: 'myplantDetail',
          params: { username: getters.currentUser.username, plantPk: getters.myplant.id }
        })
      })
      .catch(error => {
        console.log(error.response)
      })
    },

    fetchMyplant({ commit, getters }, plantPk) {
      axios({
        url: drf.myplant.myplantDetail(plantPk),
        method: 'get',
        headers: getters.authHeader,
      })
      .then(res => commit('SET_MYPLANT', res.data))
      .catch(err => {
        console.log(err.response)
        // if (err.response.status === 404) {
        //   router.push({ name: 'NotFound404' })
        // }
      })
    },

    fetchOTP({ commit, getters }, plantPk) {
      axios({
        url: drf.myplant.plantOTP(plantPk),
        method: 'get',
        headers: getters.authHeader,
      })
      .then(res => commit('SET_OTP', res.data.otp_code))
      .catch(err => {
        console.log(err.response)
      })
    },

    resetOTP({ commit }) {
      commit('SET_OTP', null)
    },
  },
}