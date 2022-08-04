const HOST = 'http://127.0.0.1:8000/api/v1/'

const ACCOUNTS = 'accounts/'

const PLANTS = 'plants/myplant/'

const LEAF82 = 'leaf82/'

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
    plantSearch: () => HOST + 'plants/' + 'search/',
    myplant: (username) => HOST + PLANTS + `${username}/`,
    newMyplant: () => HOST + PLANTS, 
    myplantDetail: (plantPk) => HOST + PLANTS + `${plantPk}/` + 'detail/',
    plantOTP: (plantPk) => HOST + PLANTS + `${plantPk}/` + 'otp/',
  },
  leaf82: {
    leaf82Sell: (keyword) => HOST + LEAF82 + 'sell/' + `${keyword}`,
    leaf82Buy: (keyword) => HOST + LEAF82 + 'buy/' + `${keyword}`,
    sido: () => HOST + LEAF82 + 'search/sido/',
    sigungu: (sido) => HOST + LEAF82 + `search/${sido}/` + 'sigungu' 
  }
}