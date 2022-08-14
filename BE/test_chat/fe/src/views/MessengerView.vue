<template>
  <nav-bar></nav-bar>
   <div class="row mx-0"> 
      <!-- 여백 -->
    <div class="col-md-1 px-0 mx-0"></div>
      <!-- 내용 담을 흰 상자 -->
    <div class="col-md-10 mb-5 pb-5 px-0 mx-0 whitebox">
      <!--채팅 목록-->
      <div class="item chat-list" >
        <div class="user-box" @click="changeReceiver(key)" v-for=" (val,key) in rooms" :key="val">
          {{ key }}
        </div> 
      </div> 
      <!-- 채팅 방-->
      <div class="item chat-room">
        <div class="chat-area" >
          <div v-for="msg in now_messages" :key="msg">
          {{ urls[msg["person"]] }}
          {{ msg["person"] }}
          {{ msg["datetime"] }}
          {{ msg["msg"] }}
          </div>
        </div>
        <div class="input-area">
          <textarea class = "input-message" v-model="message" />
          <button class="send-button" style="display: block;" @click="sendMessage">전송</button>
        </div>
      </div>
    </div>
      <!-- 여백 -->
    <div class="col-md-1 px-0 mx-0"></div>
  </div> 
  <!-- --------------------------------------------------------------------------------------- -->
 
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
      urls:{},
    }
  },
  computed: {
    // ...mapGetters(['receiver','currentUser',])
    ...mapGetters(['receiver','username',])
  },
  async created() {
      // this.id = this.currentUser.pk;
    // let userWait = await this.fetchCurrentUser()
    // console.log(userWait)
    // this.id = this.currentUser.pk
    // console.log(this.currentUser.pk);
    // console.log(this.id);
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
      // 전에 거래 기록 없을 때
      if( (this.now_receiver in this.rooms) == false ){
        this.socket.emit('startchat',this.now_receiver);
      }else{
        //전에 거래 기록 있을 때
        this.socket.emit("getMessages",this.rooms[this.now_receiver]);
      }
    }


    // 서버에서 보낸 채팅내역 받아오기
    this.socket.on('messages', (messages) => {
      this.now_messages = messages
    })
    // 서버에서 메세지 받아오기
    this.socket.on('message', (message) => {
      this.now_messages.push(message);
      console.log(message);
    })

    //채팅방 정보 받아오기
    this.socket.on('sendRooms',(data)=>{
      this.rooms[data.with_who] = data.room_num;
      this.urls[data.with_who] = data.photo_url;
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

.chat-list-img {
  width: 60px;
  margin-right: .5rem;
}

.chat-view {
  position: relative; 
  height: 500px;
  padding: 1rem 2rem 0 1rem;
  overflow-y: scroll;
  overflow-x: hidden;
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
  margin: 0 0 .3rem 1rem;
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
  margin: 0 0 1rem 1rem;
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
</style>