const HOST = 'http://127.0.0.1:8000/api/v1/'

const ACCOUNTS = 'accounts/'

const PLANTS = 'plants/myplant/'

export default {
  accounts: {
    signup: () => HOST + ACCOUNTS + 'signup/',
    login: () => HOST + ACCOUNTS + 'login/',
    logout: () => HOST + ACCOUNTS + 'logout/',
    currentUserInfo: () => HOST + ACCOUNTS + 'user/',
    profile: () => HOST + ACCOUNTS + 'profile/',
    updateProfile: () => HOST + ACCOUNTS + 'userinformation/',
    changePassword: () => HOST + ACCOUNTS + 'password/' + 'change/'
  },
  myplant: {
    plantSearch: (keyword) => HOST + PLANTS + 'search/' + `${keyword}`,
    myplantList: (usernickname) => HOST + PLANTS + `${usernickname}`,
    newMyplant: () => HOST + PLANTS, 
    myplantDetail: (plantPk) => HOST + PLANTS + `${plantPk}` + 'detail/',
    plantOTP: (plantPk) => HOST + PLANTS + `${plantPk}` + 'otp/',
  }
}