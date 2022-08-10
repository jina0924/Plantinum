<template>
  <div class="wrapper">
    <div class="form-bg col-10 col-lg-7 p-5">
      <h3 class="form-title mb-4">내 식물 등록</h3>
      <form @submit.prevent="onSubmit">
        <!-- 식물 사진 -->
        <div class="mb-3">
          <input @change="onInputImage" accept="image/*" ref="newMyplantImage" type="file" class="form-input" id="myplantPhoto">
        </div>
        <!-- 식물 닉네임 -->
        <div class="mb-3">
          <input v-model="newMyplant.nickname" type="text" class="form-input" id="myplantNickname" placeholder="식물 닉네임을 입력해주세요.">
        </div>
        <!-- 식물 이름 검색 -->
        <div class="select-plant mb-3">
          <input type="text" id="plant" list="search-plant-list" placeholder="식물 이름을 검색하세요." class="form-input" v-model="newMyplant.plantname">
          <datalist id="search-plant-list">
            <option v-for="(plant) in plant_list" :key="plant.pk">{{ plant.name }}</option>
          </datalist>
        </div>
        <!-- 등록 버튼 -->
        <div class="myplant-create-submit">
          <router-link :to="{ name: 'myplant', params: { username: currentUser.username } }">
            <button class="form-btn back-btn">뒤로가기</button>
          </router-link>
          <button class="form-btn myplant-create-submit-btn">등록</button>
        </div>
      </form>
    </div>
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
        plantname: this.myplant.plantname,
      },
    }
  },
  computed: {
    ...mapGetters(['currentUser', 'plant_list'])
  },
  methods: {
    ...mapActions(['createMyplant', 'searchPlant', 'updateMyplant']),
    onInputImage() {
      this.newMyplant.photo = this.$refs.newMyplantImage.files[0]
    },
    onSubmit() {
      // if (this.newMyplant.photo.length < 1) {
      //   // this.newMyplant.photo = '../assets/'
      // }
      console.log(this.newMyplant.photo)
      console.log(this.myplant)
      if (this.action === 'create') {
        this.createMyplant(this.newMyplant)
      } else if (this.action === 'update') {
        const payload ={
          plantPk: this.myplant.id,
          ...this.newMyplant,
        }
        this.updateMyplant(payload)
      }
    },
  },
  created() {
    this.searchPlant()
  },
}
</script>

<style scoped>
.wrapper {
  display: flex;
  justify-content: center;
}

.form-bg {
  background-color: white;
  border-radius: 15px;
}

.form-title {
  text-align: center;
  font-weight: 700;
  color: #65805D;
;
}

.form-input {
  display: block;
  width: 100%;
  padding: 0.375rem 0.75rem;
  font-size: 1rem;
  line-height: 1.5;
  margin: 2rem 0;
  background-color: #fff;
  background-clip: padding-box;
  border: 1px solid #efefef;
  border-radius: 0.25rem;
  box-shadow: 0.5rem 0.5rem 0.5rem #efefef;
  transition: border-color .15s ease-in-out,box-shadow .15s ease-in-out;
}

input:focus {
  outline: none;
  border-color: rgba(178, 201, 171, 20% ) ;
  box-shadow: 0.5rem 0.3rem 0.5rem rgba(178, 201, 171, 50% ); 
}

.myplant-create-submit {
  display: flex;
  justify-content: flex-end;
}

.form-btn{
  cursor: pointer;
  border: none;
  margin: 0.5rem 1rem 0.5rem 0;
  font-weight: 500;
  padding: 0 1rem;
  border-radius: 12px;
  height: 45px;
}

.back-btn:hover {
  background-color: #d2d2d2;
  transition: all 0.5s;
}

.back-btn:active {
  background-color: #d2d2d2;
  transition: all 0.5s;
  border: none;
}

.myplant-create-submit-btn {
  background-color: #b2c9ab;
  color: white;
  font-size: 1rem;
}

.myplant-create-submit-btn:hover {
  background-color: #65805d;
  transition: all 0.5s;
}
</style>