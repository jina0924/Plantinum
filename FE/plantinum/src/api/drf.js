const HOST = 'http://127.0.0.1:8000/api/v1/'

const ACCOUNTS = 'accounts/'

const MYPLANT = 'plants/'

export default {
  accounts: {
    signup: () => HOST + ACCOUNTS + 'signup/',
    login: () => HOST + ACCOUNTS + 'login/',
    logout: () => HOST + ACCOUNTS + 'logout/',
    currentUserInfo: () => HOST + ACCOUNTS + 'user/',
    profile: username => HOST + ACCOUNTS + 'profile/' + `${username}/`,
    updateProfile: () => HOST + ACCOUNTS + 'profile/' + 'update/',
    changePassword: () => HOST + ACCOUNTS + 'password/' + 'change/'
  },
  myplant: {
    all : (usernickname) => HOST + MYPLANT + 'myplant/' + `${usernickname}`
  }
}