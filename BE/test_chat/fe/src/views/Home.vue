<template>
  <div class="home">
    <h1>hello vue.js</h1>
    <input v-model="id" placeholder="ID를 입력하세요">
    <button style="display: block;" @click="changeId">아이디 입력</button>
  </div>
</template>

<script>
import {mapMutations} from "vuex";
export default {
  name: "Home",
  data(){
    return{
      id: "",
    }
  },
  methods:{
    ...mapMutations(['changeid']),
    changeId(){
      this.changeid(this.id);
      console.log("change ID!")
    }
  }
}
</script>

<style scoped>

</style>