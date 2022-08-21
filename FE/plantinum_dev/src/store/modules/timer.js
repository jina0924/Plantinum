import axios from 'axios'
import drf from '@/api/drf'

export const Timer = {
  state: {
    otpTimer: 60,
    temp_OTP: null,
    modal: 0,
  },
  getters: {
    otpTimer: state => state.otpTimer,
    temp_OTP: state => state.temp_OTP,
    modal: state => state.modal,
  },
  mutations: {
    COUNT_TIME: (state, otptimer) => state.otpTimer = otptimer,
    SET_OTP: (state, otp) => state.temp_OTP = otp,
    SET_MODAL: (state, num) => state.modal = num,
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
      .then(res => {
        commit('SET_OTP', res.data.otp_code)
      })
      .catch(err => {
        console.log(err.response)
      })
    },

    // startTimer({ commit, dispatch, getters }, plantPk) {
    //   const interval = setInterval(() => {
    //     dispatch('checkOTP', plantPk)
    //     dispatch('countTime', getters.otpTimer - 1)
    //     if (getters.otpTimer <= 55 && getters.temp_OTP === null) {
    //       dispatch('stopTimer', interval)
    //       dispatch('fetchMyplant', plantPk)
    //       dispatch('changeModal', 0)
    //     } else if (this.myplant.is_connected===true) {
    //       dispatch('stopTimer', interval)
    //       commit('SET_OTP', null)
    //       dispatch('changeModal', 0)
    //     }
    //   }, 1000)
    //   return interval
    // },
    
    // stopTimer({ commit, dispatch }, timer) {
    //   clearInterval(timer)
    //   commit('COUNT_TIME', 60)
    //   dispatch('changeModal', 0)
    // },

    // changeModal({ commit }, num) {
    //   commit('SET_MODAL', num)
    // }
  },

}