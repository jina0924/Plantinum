<template>
  <div><nav-bar></nav-bar></div>
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
          {{ msg }}
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
    ...mapGetters(['receiver','currentUser',])
  },
  async created() {
      // this.id = this.currentUser.pk;
    // let userWait = await this.fetchCurrentUser()
    // console.log(userWait)
    // this.id = this.currentUser.pk
    // console.log(this.currentUser.pk);
    // console.log(this.id);
    this.id = localStorage.getItem('username')

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

</style>