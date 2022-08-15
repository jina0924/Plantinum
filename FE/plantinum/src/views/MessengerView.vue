<template>
  <nav-bar></nav-bar>
  <!-- <div class="row mx-0"> -->
      <!-- 여백 -->
    <!-- <div class="col-md-1 px-0 mx-0"></div> -->
      <!-- 내용 담을 흰 상자 -->
    <!-- <div class="col-md-10 mb-5 pb-5 px-0 mx-0 whitebox"> -->
      <!--채팅 목록-->
      <!-- <div class="item chat-list" >
        <div class="user-box" @click="changeReceiver(key)" v-for=" (val,key) in rooms" :key="val">
          {{ key }}
        </div> 
      </div> -->
      <!-- 채팅 방-->
      <!-- <div class="item chat-room">
        <div class="chat-area" >
          <div v-for="msg in now_messages" :key="msg">
          {{ msg }}
          </div>
        </div>
        <div class="input-area">
          <textarea class = "input-message" v-model="message" />
          <button class="send-button" style="display: block;" @click="sendMessage">전송</button>
        </div>
      </div>
    </div> -->
      <!-- 여백 -->
    <!-- <div class="col-md-1 px-0 mx-0"></div>
  </div> -->
  <!-- --------------------------------------------------------------------------------------- -->
  <section>
    <div class="container py-4">

      <div class="row">
        <div class="col-md-12">

          <div class="card" id="chat3">
            <div class="card-body">

              <div class="row">
                <div class="col-md-6 col-lg-5 col-xl-4 mb-4 mb-md-0">

                  <div class="p-3">

                    <div class="profile-div mb-3">
                      <span>내 프로필 자리</span>
                    </div>

                    <div class="chat-list-view">
                      <ul class="mb-0 list-unstyled">
                        <li class="p-2 border-bottom">
                          <div @click="changeReceiver(key)" v-for=" (val,key) in rooms" :key="val" class="d-flex justify-content-between chat-list-item">
                            <div class="d-flex flex-row">
                              <div>
                                <img
                                  src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-chat/ava1-bg.webp"
                                  alt="avatar" class="d-flex align-self-center chat-list-img">
                              </div>
                              <div class="pt-1">
                                <p class="your-name">{{ key }}</p>
                                <p class="wish-leaf">귤나무</p>
                              </div>
                            </div>
                            <div class="pt-1">
                              <p class="mb-1 time-cnt">Just now</p>
                            </div>
                          </div>
                        </li>

                        <li class="p-2 border-bottom">
                          <div class="d-flex justify-content-between">
                            <div class="d-flex flex-row">
                              <div>
                                <img
                                  src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-chat/ava1-bg.webp"
                                  alt="avatar" class="d-flex align-self-center chat-list-img">
                              </div>
                              <div class="pt-1">
                                <p class="your-name">김상덕</p>
                                <p class="wish-leaf">귤나무</p>
                              </div>
                            </div>
                            <div class="pt-1">
                              <p class="mb-1 time-cnt">Just now</p>
                            </div>
                          </div>
                        </li>
                      </ul>
                    </div>

                  </div>

                </div>
                <!-- 채팅 내용 -->
                <div class="col-md-6 col-lg-7 col-xl-8">
                  <div class="you-username">상대방 이름</div>
                  <div class="chat-view">
                    <!-- 상대가 적은 메시지 -->
                    <div class="d-flex flex-row justify-content-start" v-for="msg in now_messages" :key="msg">
                      <!-- <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-chat/ava6-bg.webp"
                        alt="avatar 1" class="chat-profile-img"> -->
                      <div>
                        <p class="your-message">{{ msg }}</p>
                        <p class="message-time">12:00 PM | Aug 13</p>
                      </div>
                    </div>
                    <!-- 내가 적은 메시지 -->
                    <div class="d-flex flex-row justify-content-end">
                      <div>
                        <p class="my-message">판다 판다</p>
                        <p class="message-time">12:00 PM | Aug 13</p>
                      </div>
                    </div>
                  </div>
                  <!-- 채팅 메시지 적는 부분 -->
                  <div class="d-flex justify-content-start align-items-center">
                    <input v-model="message" type="text" class="form-input" id="exampleFormControlInput2"
                      placeholder="Type message">
                    <span @click="sendMessage" class="material-symbols-outlined send-btn">send</span>
                  </div>

                </div>
              </div>

            </div>
          </div>

        </div>
      </div>

    </div>
  </section>
</template>

<script>
import NavBar from '@/components/NavBar.vue'
import { mapActions, mapGetters } from "vuex"
import { io } from 'socket.io-client'

export default {
  name: 'MessengerView',
  components:{
    NavBar,
  },
  data(){
    return {
      socket: null,
      id: -1,
      message: '',
      now_messages:[],
      now_receiver: -1, // 새로고침 했거나, 거래탭에서 채팅하기로 넘어오지 않았을 경우
      rooms:{},
    }
  },
  computed: {
    // ...mapGetters(['receiver','currentUser',])
    ...mapGetters(['receiver','username',])
  },
  async created() {
    // this.id = this.currentUser.pk
    // this.id = localStorage.getItem('username')
    this.id = this.username

    if( this.receiver !== -1 ){
      this.now_receiver=this.receiver;
    }
    //console.log(this.receiver)

    console.log(this.rooms)

    // 소켓 생성 - 서버주소
    this.socket = io('http://localhost:3000')
    this.socket.on('connect', () => {
    })
    // 소켓연결후 id(pk) 건내줌
    this.socket.emit('makeSocketName',this.id);
    // 현재 채팅방 리스트 불러오기
    this.socket.emit('getRooms',this.id);
    console.log(this.rooms)

    //-1이 아니면 거래에서 건너온것_start
    if(this.now_receiver !== -1){
      if( (this.now_receiver in this.rooms) == false ){
        this.socket.emit('startchat',this.now_receiver);
      }else{
        this.socket.emit("getMessages",this.rooms[this.now_receiver]);
      }
    }


    // 서버에서 보낸 채팅내역 받아오기
    this.socket.on('messages', (messages) => {
      this.now_messages = messages
    })
    // 서버에서 메세지 받아오기
    this.socket.on('message', (message) => {
      this.now_messages.push(message)
    })

    //채팅방 정보 받아오기
    this.socket.on('sendRooms',(data)=>{
      this.rooms[data.with_who] = data.room_num;
    })
    

    
  },
  methods : {
    ...mapActions(['fetchReceiver','setReceiver',]),

    changeReceiver(data){
      console.log(data);
      //현재 채팅자와 같을때 - 아무일도 일어나지 않음
      if(this.now_receiver === data){
        return;
      }else{
        // 다를때
        
        // 상대 변경
        this.now_receiver=data;
        // 채팅시작
        //start();
        this.socket.emit("getMessages",this.rooms[this.now_receiver]);

      }
    },

    sendMessage() {
      // 소켓을 통해 서버로 메세지를 보낸다.
      if(this.now_receiver == -1){
        return;
      }
      this.socket.emit('send', {receiver:this.now_receiver , msg: this.message, room_num:this.rooms[this.now_receiver]});
      this.message = ''
    },

    start(){
      //이미 채팅 진행중인 상대면 채팅 내역 가져오기
      //아니면 채팅방 만들기 신호
      if( (this.receiver in this.rooms) == false ){
        this.socket.emit('startchat',{receiver:this.receiver});
      }else{
        
        this.socket.emit("getMessages",this.rooms[this.receiver]);
      }
    }


  },

  beforeRouteLeave(to,from,next){
    console.log("socket disconnect")
    this.socket.disconnect();
    this.now_receiver=-1;
    this.rooms={};
    this.setReceiver(-1);
    next();
  }
  
}
</script>


<style scoped>
.whitebox{
  background-color: #FFFFFFCC;
  height: 500px;
	width: 300px;
  display: flex;
  flex-direction: row;
  justify-content: space-around;
}

.item{
  position: relative;
  background-color: aliceblue;
  width : 48%;
  height: 100%;
  top: 30px;
}

.chat-list{
  display:flex;
  flex-direction: column;
}
.user-box{
  margin: 5px;
  border: 1px solid black;
  height: 10%;
  text-align: center;
}

.chat-rooms{
  display:flex;
  flex-direction: column;
  justify-items:center;
}

.chat-area{
  position:relative;
  width: 95%;
  height: 80%;
  top:5px;
  margin-bottom:10px;
  background-color: rgb(230,230,200);
}
.input-area{
  position:relative;
  display:flex;
  flex-direction: row;
}

.input-message {
  margin-left:5px;
  width: 70%;
}

/* ----------------------------------------------------------------------------------------------- */
.card {
  border-radius: 15px;
  border: 1px solid white;
  box-shadow: 0 0 .5rem #edeae2;
}

.chat-list-view {
  position: relative;
  height: 500px;
  overflow-y: scroll;
  overflow-x: hidden;
  padding: 0 1rem 0 0;
}

.chat-list-view::-webkit-scrollbar {
  width: 10px;
}
.chat-list-view::-webkit-scrollbar-thumb {
  background-color: #EFEFEF;
  border-radius: 10px;
  background-clip: padding-box;
  border: 2px solid transparent;
}
.chat-list-view::-webkit-scrollbar-track {
  background-color: white;
  border-radius: 10px;
  /* box-shadow: inset 0px 0px 5px white; */
}

.chat-list-img {
  width: 60px;
  margin-right: .5rem;
}

.chat-list-item:hover {
  cursor: pointer;
  background-color: #EFEFEF;
}

.chat-list-item:focus {
  background-color: #EFEFEF;
}

.chat-view {
  position: relative; 
  height: 500px;
  padding: 1rem 2rem 0 1rem;
  overflow-y: scroll;
  overflow-x: hidden;
}

.you-username {
  margin: .5rem;
  text-align: center;
  font-size: 1.3rem;
  font-weight: 600;
}

.chat-view::-webkit-scrollbar {
  width: 10px;
}
.chat-view::-webkit-scrollbar-thumb {
  background-color: #EFEFEF;
  border-radius: 10px;
  background-clip: padding-box;
  border: 2px solid transparent;
}
.chat-view::-webkit-scrollbar-track {
  background-color: white;
  border-radius: 10px;
  /* box-shadow: inset 0px 0px 5px white; */
}

.chat-profile-img {
  width: 45px;
  height: 100%;
}

.your-name {
  font-weight: 600;
  margin-bottom: 0;
}

.wish-leaf {
  font-size: .8rem;
  font-weight: 400;
  color: rgb(73, 73, 73);
  margin-top: .2rem;
}

.time-cnt{
  font-size: .8rem;
  font-weight: 400;
  color: rgb(73, 73, 73);
}

.your-message {
  background-color: #f5f6f7;
  border-radius: 10px;
  margin-bottom: .3rem;
  padding: 1rem;
}

.my-message {
  background-color: #b2c9ab;
  border-radius: 10px;
  margin-bottom: .3rem;
  padding: 1rem;
}

.message-time {
  font-size: .9rem;
  font-weight: 200;
  color: rgb(73, 73, 73);
  float: inline-end;
  margin: 0 1rem;
}

.form-input {
  display: block;
  width: 93%;
  padding: 0.375rem 0.75rem;
  font-size: 1rem;
  line-height: 1.75rem;
  margin: 1.3rem .5rem 1.5rem 0;
  background-color: #fff;
  background-clip: padding-box;
  border: 1px solid #efefef;
  border-radius: 0.25rem;
  box-shadow: 0.5rem 0.5rem 0.5rem #efefef;
  transition: border-color .15s ease-in-out,box-shadow .15s ease-in-out;
}

.form-input:focus {
  outline: none;
  border-color: rgba(178, 201, 171, 20% ) ;
  box-shadow: 0.5rem 0.3rem 0.5rem rgba(178, 201, 171, 50% ); 
}

.send-btn:hover {
  color: #65805d;
  cursor: pointer;
}
</style>