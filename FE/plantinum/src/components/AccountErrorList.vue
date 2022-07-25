<template>
  <p>다시 한번 작성해주세요.</p>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'AccountErrorList',
  computed: {
    ...mapGetters(['authError'])
  }
}
</script>

<style scoped>
  p {
    color: red;
  }
</style>