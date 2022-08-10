//import express from 'express'
//import { Server } from 'socket.io'
//import { createServer } from 'http'
const express = require("express");
const { Server } = require("socket.io");
const { createServer } = require("http");

// express 초기화
const app = express()
// socket.io 지원을 위해 http 모듈에서 제공하는 메서드로 서버를 초기화한다.
const http = createServer(app)
// 웹 소켓 서버를 초기화한다. 두번째로 서버를 초기화할 때 여러 옵션을 줄 수 있다.
const io = new Server(http, {
  cors: {
    origin: ['http://localhost:8080']
  }
})

let rooms_count = 0;
const messages_send = [];
const chattingRooms = [];
//연결된 소켓 관리, {id,uid}
let sockets_count = 0;
// pk - socket
const connected_sockets={};


class ChatInfo{
  constructor(id1,id2){
    this.room_number = rooms_count;
    this.participation = new Set();
    this.participation.add(id1);
    this.participation.add(id2);
    this.messages = ["------- start chatting --------"];
  }
}

// 앞단에서 요청이 오고 소켓이 생성되면 이벤트를 발생시킨다.
// 두번째 인자인 콜백함수에 생성된 소켓이 담겨져온다.
// 소켓에는 해당 소켓에 연결된 모든 클라이언트들에게 broadcast를 하거나,
// 이벤트를 발생 혹은 수신할 수 있는 메서드가 있다.
io.on('connection', socket => {
  console.log("Socket is connect!! : " ,socket.id);

  //소켓이랑 이름 매칭
  //나중에 db로 저장필요
  socket.on('makeSocketName',data=>{
    //let isexist = 0;
    // pk - socket 형태
    connected_sockets[data] = socket;
    socket.user_name = data;
    console.log(data);
    //기존 소켓 존재 
    /*
    for (let i=0;i<sockets_count;i++){
    
      if(connected_sockets[i].user_name === data){
        isexist = 1;
        socket.user_name = data;
        connected_sockets[i] = socket;
        break;
      }
    }
    
    //새거일때
    if(isexist == 0){
      socket.user_name = data;
      connected_sockets.push(socket);
      sockets_count++;
    }
    */
  });

  socket.on('startchat',(data)=>{
    console.log("make chattingrooms");
    //처음 채팅방이 만들어짐
    chattingRooms.push(new ChatInfo(socket.user_name,data.receiver));
    //보낸 소켓 먼저 채팅방 참여
    socket.join(String(rooms_count));
    socket.emit('getRooms',{with_who:data.receiver , room_num:rooms_count});
    //상대 채팅방 참여
    connected_sockets[data.receiver].join(String(rooms_count));
    connected_sockets[data.receiver].emit('getRooms',{with_who:socket.user_name, room_num:rooms_count});
    //받은 유저 탐색후 그 소켓 채팅방 참여
    /*
    for (let i=0 ; i<sockets_count;i++){
      if(connected_sockets[i].user_name == data.receiver){
        connected_sockets[i].join(String(rooms_count));
        connected_sockets[i].emit('getRooms',{with_who : socket.user_name, room_num:rooms_count});
        break;
      }
    }*/

    
    //해당 채팅 시작알림 메세지 보내기
    msg = ["------- start chatting --------"]
    io.to(String(rooms_count)).emit('messages', msg);
    //만들어진 룸넘버 제공
    
    rooms_count++;
  });

  socket.on('send', data => {
    
    message = "["+socket.user_name+"] "+data.msg;
    console.log(message);
    console.log(data.room_num, chattingRooms[data.room_num])
    chattingRooms[data.room_num].messages.push(message);
    //chattingRooms[data.room_num].messages.push(message);
    //messages_send.push(message);
    io.to(String(data.room_num)).emit('messages', chattingRooms[data.room_num].messages);
  });


  socket.on('disconnect', () => {
    console.log("socket disconnect : ",socket.id,socket.user_name);
  });
})


app.get("/", (req,res) => {
  res.send(messages);
})
// app.listen이 아닌 http.listen를 사용한다.
http.listen(8000, () => {
  console.log('started server')
})