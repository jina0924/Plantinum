<template>
  <h1>Login</h1>
  <div>
    <form action="">
      <account-error-list v-if="authError"></account-error-list>
      <input v-model="credentials.username" type="text" placeholder="Your ID">
      <input v-model="credentials.password" type="text" placeholder="Your password">
      <button type="submit">로그인</button>
    </form>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import AccountErrorList from '@/components/AccountErrorList.vue'

export default {
  name: 'LoginView',
  components: {
    AccountErrorList,
  },
  data() {
    return {
      credentials: {
        username: '',
        password: '',
      }
    }
  },
  computed: {
    ...mapGetters(['authError'])
  },
  methods: {
    ...mapActions(['login'])
  }
}
</script>

<style>

</style>