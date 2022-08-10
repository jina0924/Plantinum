<template>
  <div>
    <textarea v-model="message" />
    <button style="display: block;" @click="sendMessage">전송</button>
    <div v-for="msg in receivedMessage" :key="msg">
      {{ msg }}
    </div>
  </div>
</template>

<script>
import { io } from 'socket.io-client'

export default {
  data() {
    return {
      socket: null,
      message: '',
      receivedMessage: []
    }
  },
  async created() {
    // 소켓 서버와 연결한다.
    // 여기서 서버에서 지정해놓은 io.on('connection') 이벤트가 실행된다.
    // 그리고 생성된 소켓을 반환한다.
    this.socket = io('http://localhost:8000')

    this.socket.on('connect', () => {
      // 여기서 소켓이 생성되고 반환될 때에 코드를 적는다.
    })

    this.socket.on('messages', (messages) => {
      // 커스텀 이벤트
      this.receivedMessage = messages
    })
  },
  methods: {
    sendMessage() {
      // 소켓을 통해 서버로 메세지를 보낸다.
      this.socket.emit('send', this.message)
      this.message = ''
    }
  }
}
</script>