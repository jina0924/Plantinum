<template>
  <div class="leaf82-new-form row">
    <!-- 여백 -->
    <div class="col-md-3 col-0"></div>
    <!-- 메인 -->
    <div class="main col-md-6 py-5 my-5">
      <div class="title-box col-12 d-flex justify-content-center py-3">
        <p class="title">잎팔이 수정하기</p>
      </div>
      <!-- 상단 -->
      <div class="left">
        <div class="img-box d-flex justify-content-center">
          <img :src="preview" alt="등록될 사진입니다.">
        </div>
        <div class="img-add-box d-flex justify-content-center pt-2">
          <label for="pic-file" class="img-add mb-0">
            <span class="material-symbols-outlined">
              photo_camera
            </span>
            <span>
              사진 변경하기
            </span>
          </label>
          <input type="file" id="pic-file" @change="onInputImage()" accept="image/*" ref="leaf82Image">
        </div>
      </div>
      <!-- 하단 -->
      <div class="right mt-3 row">
        <div class="col-md-2"></div>
        <div class="col-md-8 col-">
          <div class="title d-flex justify-content-start py-2">
            <input type="text" v-model="credentials.plantname">
          </div>
          <div class="price d-flex justify-content-start py-2">
            <input type="text" v-model="credentials.price">
          </div>
          <div class="addr d-flex justify-content-start py-2">
            <select name="sido" id="" @change="beforeFetchSigungu($event)" class="mr-1">
              <option selected>지역을 선택해주세요</option>
              <option v-for="(loc) in sido" :key="loc.pk" :value="loc.sido">{{ loc.sido }}</option>
            </select>
            <!-- 시도가 선택되면 활성화 -->
            <select name="sigungu" id="" @change="selectSigungu($event)" v-if="this.credentials.sido" class="mr-1">
              <option selected>동네를 선택해주세요</option>
              <option v-for="(loc2) in sigungu" :key="loc2.pk" :value="loc2.sigungu">{{ loc2.sigungu }}</option>
            </select>
            <!-- 비활성화 -->
            <select name="sigungu" id="" v-if="!this.credentials.sido" disabled class="mr-1">
              <option selected>동네를 선택해주세요</option>
            </select>
            <select name="category_class" id="category_class" @change="selectCategory($event)" class="mr-1">
              <option value="분양해요">분양해요</option>
              <option value="분양받아요">분앙받아요</option>
            </select>
            <select name="status_class" id="status_class" @change="selectStatus($event)" class="mr-1">
              <option value="판매중">판매중</option>
              <option value="예약중">예약중</option>
              <option value="거래완료">거래완료</option>
            </select>
          </div>
          <div class="content d-flex justify-content-start py-">
            <textarea name="content" id="content" cols="30" rows="10" v-model="credentials.content" placeholder="회원님의 식물을 소개해주세요"></textarea>
          </div>
          <div class="btns row d-flex justify-content-end py-3">
            <div class="submit col-2 d-flex justify-content-end">
              <button @click="beforeUpdateLeaf82(credentials)">등록</button>
            </div>
            <div class="cancel col-2">
              <router-link :to="{ name : 'leaf82Detail' , params : { username: info.username , posting_addr: info.posting_addr } }" class="d-flex justify-content-end">
                <button>취소</button>
              </router-link>
            </div>
          </div>
          <div class="col-md-2"></div>
        </div>
      </div>
    </div>
    <!-- 여백 -->
    <div class="col-md-3 col-0"></div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'Leaf82Edit',
  data() {
    return {
      info: {
        username: this.$route.params.username,
        posting_addr: this.$route.params.posting_addr
      },
      credentials: {
        sido: '',
        sigungu: '',
        plantname: '',
        content: '',
        price: '',
        category_class: '',
        status_class: '',
        photo: '',
      },
      preview: ''
    }
  },
  methods: {
    ...mapActions(['updateLeaf82', 'fetchSido', 'fetchSigungu',]),
    fillCredentials() {
      this.credentials.sido = this.leaf82Detail.addr.sido
      this.credentials.sigungu = this.leaf82Detail.addr.sigungu
      this.credentials.plantname = this.leaf82Detail.plantname
      this.credentials.content = this.leaf82Detail.content
      this.credentials.price = this.leaf82Detail.price
      this.credentials.category_class = this.leaf82Detail.category_class
      this.credentials.status_class = this.leaf82Detail.status_class
      this.credentials.photo = this.leaf82Detail.photo
    },
    makeImgUrl() {
      this.preview = this.credentials.photo
    },
    beforeFetchSigungu(event) {
      let tmp = event.target.value
      this.credentials.sido = tmp
      this.fetchSigungu(this.credentials.sido)
    },
    selectSigungu(event) {
      let tmp = event.target.value
      console.log(tmp)
      this.credentials.sigungu = tmp
      console.log(this.credentials.sigungu)
    },
    selectCategory(event) {
      let tmp = event.target.value
      console.log(tmp)
      this.credentials.category_class = tmp
      console.log(this.credentials.category_class)
    },
    selectStatus(event) {
      let tmp = event.target.value
      console.log(tmp)
      this.credentials.status_class = tmp
      console.log(this.credentials.status_class)
    },
    beforeUpdateLeaf82(credentials) {
      if (credentials.plantname === '') {
        alert('이름을 입력해주세요.')
      } else if (credentials.price === '' || !Number.isInteger(parseInt(credentials.price))) {
        alert('가격을 확인해주세요.')
      } else if (credentials.sigungu === '') {
        alert('주소를 선택해주세요.')
      } else if (credentials.content === '') {
        alert('식물을 소개해주세요')
      } else {
        const updateInfo = {
          credentials,
          info: this.info
        }
        this.updateLeaf82(updateInfo)
      }
    },
    onInputImage() {
      this.credentials.photo = this.$refs.leaf82Image.files[0]
      const url = URL.createObjectURL(this.credentials.photo)
      this.preview = url
    },
  },
  computed: {
    ...mapGetters(['leaf82Detail', 'sido', 'sigungu']),
  },
  created() {
    this.fetchSido()
    // this.fillCredentials()
    // console.log(this.credentials)
  },
  watch: {
    leaf82Detail() {
      this.fillCredentials()
      this.makeImgUrl()
    }
  }
}
</script>

<style scoped>
div {
  margin: 0;
  padding: 0;
}

.main {
  background-color: white;
  border-radius: 15px;
}

.img-box img{
  height: 300px;
  width: 300px;
  border-radius: 1rem;
}

.img-add span {
  font-size: 1rem;
}

.img-add:hover {
  cursor: pointer;
}

input[type="file"] {
  position: absolute;
  width: 0;
  height: 0;
  padding: 0;
  overflow: hidden;
  border: 0;
}

/* 하단 */
.right input {
  width: 100%;
  border-radius: 0.5rem;
  height: 2.5rem;
}

.right select {
  border-radius: 0.5rem;
  display: block;
  width: 100%;
  height: 2.5rem;
  font-size: 1rem;
  line-height: 1.5;
  background-color: #fff;
  background-clip: padding-box;
  border: 1px solid #efefef;
  border-radius: 0.25rem;
  box-shadow: 0.5rem 0.5rem 0.5rem #efefef;
  transition: border-color .15s ease-in-out,box-shadow .15s ease-in-out;
}

input {
  display: block;
  width: 100%;
  font-size: 1rem;
  line-height: 1.5;
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

textarea {
  display: block;
  width: 100%;
  font-size: 1rem;
  line-height: 1.5;
  background-color: #fff;
  background-clip: padding-box;
  border: 1px solid #efefef;
  border-radius: 0.25rem;
  box-shadow: 0.5rem 0.5rem 0.5rem #efefef;
  transition: border-color .15s ease-in-out,box-shadow .15s ease-in-out;
  resize: none;
}

textarea:focus {
  outline: none;
  border-color: rgba(178, 201, 171, 20% ) ;
  box-shadow: 0.5rem 0.3rem 0.5rem rgba(178, 201, 171, 50% ); 
}

.content {
  height: 10rem;
}

.submit {
  width: 100%;
}

.submit button{
  width: 80%;
  background-color: #b2c9ab;
  border-radius: 0.5rem;
  color: white;
  border: none;
  font-size: 1rem;
  height: 2rem;
}

.submit button:hover {
  background-color: #65805d;
  transition: all 0.5s;
}

.cancel {
  width: 100%;
}

.cancel a {
  width: 100%;
  text-decoration: none;
}

.cancel a button {
  width: 80%;
  background-color: white;
  border-radius: 0.5rem;
  color: gray;
  border-width: 1px;
  border-color: rgb(170, 170, 170);
  font-size: 1rem;
  height: 2rem;
  border-style: solid;
}

button:hover {
  cursor: pointer;
}

.cancel a button:hover{
  background-color: #d2d2d2;
  transition: all 0.5s;
}
</style>