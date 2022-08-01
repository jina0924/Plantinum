<template>
  <!-- <div class="container-fluid"> -->
    <!-- <div class="card shadow mb-4"> -->
      <!-- <div class="card-header py-3"> -->
        <!-- <form action="GET" class="plant-search-form">
          <input type="search" class="plant-search" placeholder="식물 이름을 검색하세요">
          <button class="mx-2">검색</button>
        </form> -->
        <form @submit.prevent="onSubmit">
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
            <button class="btn myplant-create-submit">등록</button>
          </div>
        </form>
      <!-- </div> -->
    <!-- </div> -->
  <!-- </div> -->
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
    ...mapGetters(['currentUser'])
  },
  methods: {
    ...mapActions(['createMplant']),
    onSubmit() {
      if (this.action === 'create') {
        this.createMyplant(this.newMyplant)
      }
    },
    onSearch() {

    }
  }
}
</script>

<style>

</style>