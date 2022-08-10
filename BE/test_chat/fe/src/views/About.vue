<template>
  <div>
    <h3> ID : {{ uid }} </h3>

    <input v-model="receiver" placeholder="보낼 사람을 입력하세요">
    <!-- 이 채팅 시작이 잎팔이에서 채팅하러가기 가 될 것 같아요-->
    <button style="display: block;" @click="start">채팅 시작</button>

    <textarea v-model="message" />
    <button style="display: block;" @click="sendMessage">전송</button>
    <div v-for="msg in receivedMessage" :key="msg">
      {{ msg }}
    </div>
  </div>
</template>

<script>
import { io } from 'socket.io-client'
import { mapState } from "vuex"

export default {
  data() {
    return {
      socket: null,
      message: '',
      //받은 메세지들
      receivedMessage: [],
      // 메세지를 받는 사람 == 현재 채팅자
      // 아마 클릭으로 pk 주면 될 것 같습니다.      
      receiver: null,
      // key-value
      // 채팅자 - 룸넘버
      // 룸넘버를 저장하는 이유는 서버에서 룸넘버를 알아야 빠른 접근이 가능하기 때문.
      rooms:{},
    }
  },
  async created() {
    //id지정
    // 소켓 서버와 연결한다.
    // 여기서 서버에서 지정해놓은 io.on('connection') 이벤트가 실행된다.
    // 그리고 생성된 소켓을 반환한다.
    this.socket = io('http://localhost:8000')

    this.socket.on('connect', () => {
      // 여기서 소켓이 생성되고 반환될 때에 코드를 적는다.
    })
    //소켓연결후 id(pk) 건내줌
    this.socket.emit('makeSocketName',this.$store.state.uid);
    
    // 여기까지 3줄이 회원가입 시 줄것 : uid대신 pk로 주면 될 것 같아요
    
    // 서버로 부터 메세지를 받음, 리스트 형태로 지금까지 룸의 내용들.
    // 이게 너무 그러면 하나씩 줘서 push로 해도 되요 이건 일단 나중에 논의.
    // 앞에 []안에 닉네임 구분해서 본인 메세지인지 판별해서 구성.
    this.socket.on('messages', (messages) => {
      // 커스텀 이벤트
      this.receivedMessage = messages
    })

    // 상대가 채팅을 눌렀을 때 나에게도 채팅방 생성 신호를 알려주는 것
    // 내가 누구와 어떤 방에서 채팅하는지 알기 위함.
    // 어디에 둘지 애매함 - 최상위에 둬야 할 것 같슴다........
    // 아니면 자신이 속한 채팅방 목록을 한번 불러오는 것도 나쁘지 않을 것 같은데
    // 그건 이제 코드를 새로 짜야함
    this.socket.on('getRooms',(data)=>{
      this.rooms[data.with_who] = data.room_num;
    })
  },
  computed : {
    //이건 그냥 아이디 보기 편하려고 놓은 겁니다.... 무시해도 되요
    ...mapState(['uid'])
  },
  methods: {
    // 받을 사람, 메세지내용,룸넘버
    // 룸넘버는 rooms와 받는 사람을 통해서 알아옴
    // rooms 딕셔너리 형태로 받는 사람이 key, 룸넘버가 value
    sendMessage() {
      // 소켓을 통해 서버로 메세지를 보낸다.
      this.socket.emit('send', {receiver:this.receiver , msg: this.message, room_num:this.rooms[this.receiver]});
      this.message = ''
    },

    // 채팅 시작시
    // 잎팔이 채널에 있으면 됩니다.
    // 채팅하려는 상대와의 방이 존재하지 않는 경우에만 emit
    // rooms로 판별. 
    start(){
      if( (this.receiver in this.rooms) == false){
        this.socket.emit('startchat',{receiver:this.receiver});
      }
    }
  }
}
</script>