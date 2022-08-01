<template>
  <div>
    <form @submit.prevent="onSubmit">
      <div class="select-plant mb-3">
        <label for="plant"></label>
        <input type="text" id="plant" list="search-plant-list" placeholder="식물 이름을 검색하세요" class="form-control" v-model="newMyplant.name_id">
        <datalist id="search-plant-list">
          <option v-for="(plant) in plant_list" :key="plant.pk" :value="plant.pk">{{ plant.name }}</option>
        </datalist>
      </div>
      <div class="mb-3">
        <label for="myplantNickname" class="form-label">식물 닉네임</label>
        <input v-model="newMyplant.nickname" type="text" class="form-control" id="myplantNickname">
      </div>
      <div class="mb-3">
        <label for="myplantPhoto" class="form-label">식물 사진</label>
        <input v-model="newMyplant.photo" type="text" class="form-control" id="myplantPhoto">
        <!-- <input type="file" class="form-control" id="myplantPhoto"> -->
      </div>
      <div class="myplant-create-submit">
        <router-link :to="{ name: 'myplant', params: { username: currentUser.username } }">
          <button class="btn">뒤로가기</button>
        </router-link>
        <button class="btn btn-primary myplant-create-submit">등록</button>
      </div>
    </form>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'MyplantForm',
  props: {
    myplant: Object,
    action: String,
  },
  data() {
    return {
      newMyplant: {
        nickname: this.myplant.nickname,
        photo: this.myplant.photo,
        name_id: this.myplant.name_id,
      },
    }
  },
  computed: {
    ...mapGetters(['currentUser', 'plant_list'])
  },
  methods: {
    ...mapActions(['createMyplant', 'searchPlant']),
    onSubmit() {
      if (this.action === 'create') {
        console.log(this.newMyplant)
        this.createMyplant(this.newMyplant)
      }
    },
  },
  created() {
    this.searchPlant()
  }
}
</script>

<style>

</style>