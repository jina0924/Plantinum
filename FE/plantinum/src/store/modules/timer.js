import axios from 'axios'
import drf from '@/api/drf'

export const Timer = {
  state: {
    otpTimer: 60,
    temp_OTP: null,
  },
  getters: {
    otpTimer: state => state.otpTimer,
    temp_OTP: state => state.temp_OTP,
  },
  mutations: {
    COUNT_TIME: (state, otptimer) => state.otpTimer = otptimer,
    SET_OTP: (state, otp) => state.temp_OTP = otp,
  },
  actions: {
    countTime({ commit }, otptimer) {
      commit('COUNT_TIME', otptimer)
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

    checkOTP({ commit, getters }, plantPk) {
        axios({
          url: drf.myplant.otpStatus(plantPk),
          method: 'get',
          headers: getters.authHeader,
        })
        .then(res => commit('SET_OTP', res.data.otp_code))
        .catch(err => {
          console.log(err.response)
        })
      },
  },
}