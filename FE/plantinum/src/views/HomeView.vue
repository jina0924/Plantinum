<template>
  <div class="boxes">
    <!-- first box -->
    <div class=first-box>
      <div class="row">
        <div class="col-md-3 home-logo">
          <router-link :to="{ name: 'home' }">
            <span>
              Plantinum
            </span>
          </router-link>
        </div>
      </div>
      <!-- 글귀 부분 -->
      <div class="row col-md-6 d-flex justify-content-center">
        <div class="contentbox">
          <div class="text-main">
            <p>반려식물 통합 관리 플랫폼</p>
            <p>플랜티넘</p>
          </div>
          <div class="text-detail">
            <p>다이어리 작성부터 분양정보까지,</p>
            <p>사람들과 함께 아름다운 집을 만들어요.</p>
          </div>
          <div class="text-hello" v-if="isLoggedIn">
          <!-- <div class="text-hello"> -->
            <!-- user 정보 받아와야 함 -->
            <p>안녕하세요, *** 님</p>
        </div>
        <!-- 버튼 -->
        <div class="btnbox" v-if="!isLoggedIn">
        <!-- <div class="btnbox row"> -->
          <div class="btn-border">
            <div class="login d-flex justify-content-center">
              <router-link :to="{ name: 'login' }">
                <button class="btn">로그인 / 회원가입</button>
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
    </div>

    <!-- second box -->
    <div class="second-box row">
      <div class="col-md-6 col-sm d-flex align-items-center">
        <img src="../assets/HomeView/main_pic_2.jpg" alt="">
      </div>
      <div class="row col-md-6 d-flex justify-content-center">
        <div class="contentbox">
          <div class="text-main">
            <p>식물과의 이야기,</p>
            <p>다이어리</p>
          </div>
          <div class="text-detail">
            <p>그동안 하지 못했던 말,</p>
            <p>다이어리를 통해 전달해주세요.</p>
            <br>
            <br>
            <p>따뜻한 마음을 남겨 반려식물과 소통합니다.</p>
          </div>
        <!-- 버튼 -->
        <div class="btnbox">
          <div class="btn-border">
            <div class="login d-flex justify-content-center">
              <router-link :to="{ name: 'myplant' }" v-if="isLoggedIn">
                <button class="btn">내 식물</button>
              </router-link>
              <router-link :to="{ name: 'login' }" v-if="!isLoggedIn">
                <button class="btn">내 식물</button>
              </router-link>
            </div>
          </div>
        </div>
        </div>
      </div>
    </div>

    <!-- third box -->
    <div class="third-box row">
      <div class="row col-md-6 d-flex justify-content-center">
        <div class="contentbox">
          <div class="text-main">
            <p>여러분의 식물을</p>
            <p>분양해주세요</p>
          </div>
          <div class="text-sub">
            <span>"보내는 마음은 아쉬웠지만,</span>
            <br>
            <span class="d-flex justify-content-end">좋은 분을 만난거 같았어요."</span>
          </div>
          <div class="text-detail">
            <p>서울에 거주하시는 진아님은</p>
            <p>얼마전 아비스를 유민님께 분양해주었답니다.</p>
          </div>
        <!-- 버튼 -->
        <!-- <div class="btnbox" v-if="!isLoggedIn"> -->
        <div class="btnbox">
          <div class="btn-border">
            <div class="login d-flex justify-content-center">
              <router-link :to="{ name: 'leaf82' }">
                <button class="btn">잎팔이</button>
              </router-link>
            </div>
          </div>
        </div>
        </div>
      </div>
      <div class="col-md-6 col-sm d-flex align-items-center justify-content-center">
        <img src="../assets/HomeView/main_pic_3.jpg" alt="">
      </div>
    </div>

    <!-- fourth box -->
    <div class="fourth-box">
      <div class="title-supool d-flex justify-content-center align-items-center">
        <p>Supool</p>
      </div>
      <div class="row">
      <div class="col-md-6 col-sm d-flex align-items-center justify-content-center">
        <img src="../assets/HomeView/main_pic_2.jpg" alt="">
      </div>
      <div class="row col-md-6 d-flex justify-content-center">
        <div class="contentbox">
          <div class="text-main">
            <p>토양상태를 파악해</p>
            <p>자동으로 길러주는 나만의</p>
            <p>수풀</p>
          </div>
          <div class="text-detail">
            <p>수풀은 토양의 습도, 주변의 온도를 분석하여</p>
            <p>자동 급수하며 식집사들을 도와주고 있습니다.</p>
            <br>
            <br>
            <p>스마트한 반려식물 키우기</p>
            <span class="supool">수풀</span>
            <span class="extra">이 함께합니다.</span>
          </div>
        <!-- 버튼 -->
        <div class="btnbox">
          <div class="btn-border">
            <div class="login d-flex justify-content-center">
              <router-link :to="{ name: 'home' }">
                <button class="btn">comming soon</button>
              </router-link>
            </div>
          </div>
        </div>
      </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
export default {
  name: 'HomeView',
  components: {
  }
}
</script>

<style scoped>
  .first-box {
    height: 1117px;
    background: url("../assets/HomeView/background_img.jpg") bottom right;
    background-size: cover ;
  }

  .second-box {
    height: 1117px;
  }

  .third-box {
    height: 1117px;
    background-color: #F3F3F3;
  }

  .fourth-box {
    height: 1117px;
    background-color: #F8F5EE;
  }

  .home-logo {
    text-align: center;
    padding-top: 1rem;
    padding-bottom: 1rem;
    text-decoration: none;
  }

  .home-logo span {
    font-family: 'Dancing Script', cursive;
    font-size: 4rem;
    color: black;
  }

  a {
    text-decoration-line: none;
  }

  .contentbox {
    margin-top: 12rem;
    margin-bottom: 3rem;
    font-family: 'SUIT', sans-serif;
  }

  .second-box .contentbox {
    margin-top: 20rem;
    margin-bottom: 3rem;
    font-family: 'SUIT', sans-serif;
  }
  
  .third-box .contentbox {
    margin-top: 20rem;
    margin-bottom: 3rem;
    font-family: 'SUIT', sans-serif;
  }

  .fourth-box .contentbox {
    margin-top: 10rem;
    margin-bottom: 3rem;
    font-family: 'SUIT', sans-serif;
  }

  .text-main {
    margin-bottom: 5rem;
  }

  .text-main p {
    margin-bottom: 0;
    font-size: 3rem;
    font-weight: bold;
  }

  .text-sub {
    margin-bottom: 5rem;
    font-size: 1.8rem;
    font-weight: bold;
  }

  .text-detail {
    margin-bottom: 7rem;
  }

  .text-detail p {
    margin-bottom: 0;
    font-size: 1.5rem;
  }

  .text-detail span {
    font-size: 1.5rem;
  }

  .text-detail .supool {
    font-weight: bold;
  }

  .text-hello {
    font-size: 1.5rem;
  }

  .btn{
    border-radius: 5px;
    height: 44px;
    font-size: 1rem;
    background-color: #b2c9ab;
    color: white;
    width: 100%;
  }

  .btnbox a {
    width: 50%;
  }

  .fourth-box .btn a {
    width: 75%
  }

  .second-box img {
    width: 100%;
    height: 50%;
  }

  .third-box img {
    width: 70%;
    height: 70%;
  }

  .fourth-box img {
    width: 70%;
  }
  
  .title-supool {
    height: 5rem;
  }

  .title-supool p {
    margin-top: 5rem;
    margin-bottom: 0;
    font-size: 4rem;
    font-family: 'Dancing Script', cursive;
  }
</style>>