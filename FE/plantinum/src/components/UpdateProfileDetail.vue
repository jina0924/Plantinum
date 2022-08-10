<template>
  <form class="profile-detail mt-5 row" @submit.prevent="updateProfile(info)">
    <!-- 헤드부분 -->
    <div class="profile-head col-lg-4 row">
      <div class="col-2"></div>
      <!-- 프로필 사진 및 닉네임과 이메일 -->
      <div class="profile-head-content col-8">
        <!-- 프로필 사진 -->
        <div class="profile-img-box">
          <div>
            <img :src="profile.photo" alt="temporary img" class="profile-img">
          </div>
        </div>
          <div class="profile-pic d-flex justify-content-center">
            <label for="pic-file">
              <span class="material-symbols-outlined">
                photo_camera
              </span>
              <span>
                사진 변경하기
              </span>
            </label>
            <input type="file" id="pic-file">
          </div>
        <!-- 닉네임 -->
        <div class="profile-nickname">
          <p class="mb-0">{{ profile.nickname }}</p>
        </div>
        <!-- 이메일 -->
        <div class="profile-email">
          <p class="">{{ profile.email }}</p>
        </div>
        <!-- 회원정보 수정 -->
        <div class="btns row">
          <div class="profile-update-btn px-0 col-md-3 col-sm-6 d-flex justify-content-center mr-2">
              <button type="submit" class="btn">
                저장
              </button>
          </div>
          <div class="profile-cancel-btn px-0 col-md-3 col-sm-6 d-flex justify-content-center">
            <router-link :to="{ name : 'profile' }">
              <button class="btn">
                취소
              </button>
            </router-link>
          </div>
        </div>
      </div>
      <div class="col-2"></div>
    </div>
    <!-- body 부분 -->
    <div class="profile-body col-lg-8">
      <!-- 로그인/프로필 정보 - 기본형 -->
      <div class="profile-info-on mt-5 offset-0 offset-md-3 offset-lg-0">
        <span class="info pr-2">로그인 및 프로필</span>
      </div>
      <div class="comment mt-1">
        <p>계정 보안 및 로그인하는데 문제가 있을 경우 설정을 변경하고 프로필을 관리합니다.</p>
      </div>
      <div class="profile-list row mt-5">
        <div class="profile-list-left d-flex-justify-content-center col-md-6 mx-0">
          <div class="container p-0 pb-2">
            <div class="card nickname">
              <div class="card-head d-flex justify-content-between pt-3">
                <span class="kind pl-4">닉네임</span>
                <span class="material-symbols-outlined icon pr-4">spa</span>
              </div>
              <div class="card-text row pb-5 mx-0">
                <input type="text" class="card-input mx-4" v-model="info.nickname">
              </div>
            </div>
          </div>
          <div class="container p-0 pb-2">
            <div class="card email">
              <div class="card-head d-flex justify-content-between pt-3">
                <span class="kind pl-4">이메일</span>
                <span class="material-symbols-outlined icon pr-4">email</span>
              </div>
              <div class="card-text row pb-5 mx-0">
                <input type="text" class="card-input mx-4" v-model="info.email">
              </div>
            </div>
          </div>
          <div class="container p-0 pb-2">
            <div class="card nickname">
              <div class="card-head d-flex justify-content-between pt-3">
                <span class="kind pl-4">연락처</span>
                <span class="material-symbols-outlined icon pr-4">phone</span>
              </div>
              <div class="card-text pb-5">
                <input type="text" class="card-input mx-4" v-model="info.phone_number">
              </div>
            </div>
          </div>
        </div>
        <div class="profile-list-right d-flex-justify-content-center col-md-6 row mx-0">
          <div class="container p-0 pb-2">
            <div class="card nickname">
              <div class="card-head d-flex justify-content-between pt-3">
                <span class="kind pl-4">비밀번호</span>
                <span class="material-symbols-outlined icon pr-4">lock</span>
              </div>
              <div class="card-text pb-5">
                <router-link :to="{ name : 'updatepassword' }">
                  <span class="card-content pl-4">비밀번호 변경</span>
                </router-link>
              </div>
            </div>
          </div>
          <div class="container p-0 pb-2">
            <div class="card email">
              <div class="card-head d-flex justify-content-between pt-3">
                <span class="kind pl-4">주소</span>
                <span class="material-symbols-outlined icon pr-4">home</span>
              </div>
              <div class="card-text pb-5 d-flex justify-content center">
                <input type="text" class="card-addr ml-4" v-model="info.addr" id="sample6_address">
                <input type="hidden" class="card-input mx-4" v-model="info.zip_code" id="sample6_postcode">
                <input type="button" class="find-addr" @click="findAddr" value="주소찾기">
              </div>
            </div>
          </div>
          <div class="container p-0 pb-2">
            <div class="card nickname">
              <div class="card-head d-flex justify-content-between pt-3">
                <span class="kind pl-4">내 식물</span>
                <span class="material-symbols-outlined icon pr-4">potted_plant</span>
              </div>
              <div class="card-text pb-5">
                <span class="card-content pl-4">{{ profile.myplant_count }}</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </form>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'UpdateProfileDetail',
  data() {
    return {
      // oldInfo: {
      //   nickname: '',
      //   email: '',
      //   addr: '',
      //   zip_code: '',
      //   phone_number: '',
      //   dday: '',
      //   myplant_count: '',
      // },
      info: {
        nickname: '',
        email: '',
        addr: '',
        zip_code: '',
        phone_number: '',
        // dday: '',
        // myplant_count: '',
      }
    }
  },
  methods: {
    ...mapActions(['updateProfile', 'fetchCurrentUser']),
    fillOldInfo() {
      this.info = this.profile
    },
    findAddr() {
      new window.daum.Postcode({
            oncomplete: (data) => {
                // 팝업에서 검색결과 항목을 클릭했을때 실행할 코드를 작성하는 부분.

                //사용자가 선택한 주소 타입에 따라 해당 주소 값을 가져온다.
                if (data.userSelectedType === 'R') { // 사용자가 도로명 주소를 선택했을 경우
                    this.info.addr = data.roadAddress;
                } else { // 사용자가 지번 주소를 선택했을 경우(J)
                    this.info.addr = data.jibunAddress;
                }
                this.info.zip_code = data.zonecode

                // 우편번호와 주소 정보를 해당 필드에 넣는다.
                document.getElementById('sample6_postcode').value = data.zonecode;
                document.getElementById("sample6_address").value = this.info.addr;
            }
        }).open();
    }
  },
  computed: {
    ...mapGetters(['profile'])
  },
  created() {
    this.fillOldInfo()
  }
}
</script>

<style scoped>
.profile-detail {
  font-family: 'SUIT' sans-serif;
  background-color: #FFFFFFCC;
  padding-top: 7rem;
}

  /* profile-head 부분 */

.profile-img-box {
  position: relative;
  width: 100%;
  padding-bottom: 100%;
}

.profile-img-box img {
  width: 100%;
  height: 100%;
  position: absolute;
  border-radius: 50%;
}

.profile-pic span {
  font-size: 1rem;
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

/* .profile-img {
  width: 100%;
  height: 100%;
  border-radius: 10rem;
} */

.profile-update-btn .btn{
  border-radius: 15px;
  height: 44px;
  font-size: 1rem;
  background-color: #b2c9ab;
  color: white;
  width: 100%;
}

.profile-update-btn .btn:hover {
  cursor: pointer;
  background-color: #65805d;
  transition: all 0.5s;
}

.profile-cancel-btn a {
  width: 100%;
}

.profile-cancel-btn .btn{
  border-radius: 15px;
  height: 44px;
  font-size: 1rem;
  color: black;
  width: 100%;
}

.profile-cancel-btn .btn:hover {
  cursor: pointer;
  background-color: #d2d2d2;
  transition: all 0.5s;
}

.profile-nickname {
  font-size: 1.2rem;
  font-weight: bold;
  padding-top: 2rem;
}

.profile-email {
  font-size: 1rem;
  color: #7E7E7E;
}

/* profile-body 부분 */

.profile-info-on .info {
  font-size: 2rem;
  font-weight: bold;
}

.container {
  margin: 0;
}

.comment {
  color: #7E7E7E;
}

.card {
  border-radius: 15px;
  box-shadow: 0.2rem 0.2rem 0.2rem #CDCDCD;
  width: 100%;
}

.card-head .kind {
  font-weight: bold;
  font-size: 1.1rem;
}

.icon {
  font-size: 1.5rem;
  color: #b2c9ab;
}

.card-text .card-input {
  color: #7E7E7E;
  font-size: 0.9rem;
  width: 80%;
}

.card-text .card-addr {
  color: #7E7E7E;
  font-size: 0.9rem;
  width: 50%;
}

.find-addr {

}


.card-text .card-input-nickname {
  color: #7E7E7E;
  font-size: 0.9rem;
  width: 50%;
}

.card-text .card-input-email {
  color: #7E7E7E;
  font-size: 0.9rem;
  width: 50%;
}

.myleaf-pic {
  padding: 0;
}

.myleaf-pic img {
  width: 10rem;
  height: 10rem;
  border-radius: 5%;
}

.card-content {
  color: #7E7E7E;
  font-size: 0.9rem;
}

.card-text a {
  text-decoration: none;
}
</style>