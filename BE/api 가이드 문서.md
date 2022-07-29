# 1. 관리자 페이지

```
http://127.0.0.1:8000/admin/
```



# 2. 유저 관련 페이지

### 회원가입

- 회원가입시 자동으로 로그인 상태로 변경됨
- 토큰 생성 및 리턴
- POST

- URL

```
http://127.0.0.1:8000/api/v1/accounts/signup/
```

- Body

| Key          | Type   | Description     | Mandatory | Example        |
| ------------ | ------ | --------------- | --------- | -------------- |
| username     | String | 유저아이디      | O         | idsampleuser   |
| email        | String | 이메일          | O    | abc@aa.com               |
| password1    | String | 비밀번호        | O         | testpassword   |
| password2    | String | 비밀번호 재입력 | O         | testpassword   |
| phone_number | String | 폰넘버          |           | 01012345678    |
| addr         | String | 주소            |           | seoul          |
| zip_code     | String | 우편번호        |           | 12345          |
| nickname     | String | 닉네임, default값 존재         |           | samplenickname |

- Response

```
{
    "key": "60c122934378ff59db8d4caae94a295a53d7c11a"
}
```



### 로그인

- 토큰 리턴
- POST
- URL

```
http://127.0.0.1:8000/api/v1/accounts/login/
```

- Body

| Key      | Type   | Description | Mandatory | Example      |
| -------- | ------ | ----------- | --------- | ------------ |
| username | String | 유저아이디  | O         | idsampleuser |
| password | String | 비밀번호    | O         | testpassword |

- Response

```
{
    "key": "60c122934378ff59db8d4caae94a295a53d7c11a"
}
```



- ### 로그아웃

- 로그인 사용자 - 토큰 사용

- POST

- URL

```
http://127.0.0.1:8000/api/v1/accounts/logout/
```

- Headers

| Key           | Type   | Description   | Mandatory | Example                                        |
| ------------- | ------ | ------------- | --------- | ---------------------------------------------- |
| Authorization | String | Token {token} | O         | Token 60c122934378ff59db8d4caae94a295a53d7c11a |

- Response

```
{
    "detail": "Successfully logged out."
}
```



# 3. 식물 관련 페이지

### 전체 식물 데이터 조회

- 공공데이터를 활용한 식물 데이터
- 확인용O 배포용X
- GET
- URL

```
http://127.0.0.1:8000/api/v1/plants/
```

- Response

```
[
    {
        "id": 1,
        "myplant_set": [],
        "name": "가울테리아",
        "watercycle_spring": "053003",
        "watercycle_spring_nm": "토양 표면이 말랐을때 충분히 관수함",
        "watercycle_summer": "053003",
        "watercycle_summer_nm": "토양 표면이 말랐을때 충분히 관수함",
        "watercycle_autumn": "053003",
        "watercycle_autumn_nm": "토양 표면이 말랐을때 충분히 관수함",
        "watercycle_winter": "053004",
        "watercycle_winter_nm": "화분 흙 대부분 말랐을때 충분히 관수함",
        "specl_manage_info": ""
    },
    ...
]
```



### 식물 이름 검색

- 물주기 등록시 사용
- 로그인 사용자 - 토큰 사용
- GET
- URL

```
http://127.0.0.1:8000/api/v1/plants/search/{검색어}/
```

- Request Parameters

| Name     | Type   | Description                              | Mandatory | Example |
| -------- | ------ | ---------------------------------------- | --------- | ------- |
| 검색어 | String | 한글명, 검색어를 포함하는 모든 식물 검색 | O         | 백      |

- Response

```
[
    {
        "pk": 32,
        "name": "동백"
    },
    {
        "pk": 77,
        "name": "백량금"
    },
    {
        "pk": 78,
        "name": "백정화"
    },
    {
        "pk": 79,
        "name": "백화등"
    },
    {
        "pk": 149,
        "name": "죽백나무"
    }
]
```



### 내식물 전체 식물 조회

- 로그인 사용자 - 토큰 사용
- GET
- URL

```
http://127.0.0.1:8000/api/v1/plants/myplant/{사용자 nickname}/
```

- Request Parameters

| Name            | Type   | Description | Mandatory | Example |
| --------------- | ------ | ----------- | --------- | ------- |
| 사용자 nickname | String |             | O         | 식집사1 |

- Response

```
[
    {
        "pk": 1,
        "nickname": "깨운이",
        "photo": "",
        "sensing": {
            "moisture_level": 0
        },
        "diary_count": 0
    },
    {
        "pk": 2,
        "nickname": "가울이",
        "photo": "",
        "sensing": {
            "moisture_level": 0
        },
        "diary_count": 3
    },
    {
        "pk": 3,
        "nickname": "개운개운",
        "photo": "",
        "sensing": {
            "moisture_level": 0
        },
        "diary_count": 0
    }
]
```



### 내식물 등록

- 물주기 등록 전 반드시 식물 이름 검색이 선행되어야 함
- 로그인 사용자 - 토큰 사용
- POST
- URL

```
http://127.0.0.1:8000/api/v1/plants/myplant/
```

- Body

| Key      | Type   | Description                  | Mandatory | Example |
| -------- | ------ | ---------------------------- | --------- | ------- |
| nickname | String | 물주기 등록 대상 식물의 애칭 | O         | 깨운이  |
| photo    | String | 물주기 등록 대상 식물의 사진 | 임시 X    |         |
| name_id    | Int | 식물의 pk | O    | 2        |

- Response

```
{
    "id": 1,
    "user": {
        "pk": 1,
        "username": "test1",
        "nickname": "촉촉한귤나무123"
    },
    "name": {
        "pk": 2,
        "name": "개운죽",
        "watercycle_spring_nm": "흙을 촉촉하게 유지함(물에 잠기지 않도록 주의)",
        "watercycle_summer_nm": "흙을 촉촉하게 유지함(물에 잠기지 않도록 주의)",
        "watercycle_autumn_nm": "흙을 촉촉하게 유지함(물에 잠기지 않도록 주의)",
        "watercycle_winter_nm": "토양 표면이 말랐을때 충분히 관수함",
        "specl_manage_info": "수경은 물주기가 필요 없으나, 화분은 1-2주에 한번씩 충분히 관수한다."
    },
    "sensing": {
        "id": 1,
        "remaining_water": false,
        "state_led": false,
        "moisture_level": 0,
        "last_watering": "",
        "my_plant": 1
    },
    "diary_set": [],
    "diary_count": 0,
    "nickname": "깨운이",
    "created_at": "2022-07-26T07:08:54.928651Z",
    "otp_code": "",
    "photo": "",
    "is_connected": false
}
```



### 내식물 상세페이지

- 물주기 식물 별 상세페이지
- 로그인 사용자 - 토큰 사용
- GET
- PUT/DELETE는 추후 추가 예정
- URL

```
http://127.0.0.1:8000/api/v1/plants/myplant/{물주기 식물 pk}/detail/
```

- Request Parameters

| Name           | Type | Description             | Mandatory | Example |
| -------------- | ---- | ----------------------- | --------- | ------- |
| 물주기 식물 pk | Int  | 물주기 등록한 식물의 pk | O         | 2       |

- Response

```
{
    "id": 2,
    "user": {
        "pk": 1,
        "username": "test1",
        "nickname": ""
    },
    "name": {
        "pk": 1,
        "name": "가울테리아",
        "watercycle_spring_nm": "토양 표면이 말랐을때 충분히 관수함",
        "watercycle_summer_nm": "토양 표면이 말랐을때 충분히 관수함",
        "watercycle_autumn_nm": "토양 표면이 말랐을때 충분히 관수함",
        "watercycle_winter_nm": "화분 흙 대부분 말랐을때 충분히 관수함",
        "specl_manage_info": ""
    },
    "sensing": {
        "id": 2,
        "remaining_water": false,
        "state_led": false,
        "moisture_level": 0,
        "last_watering": "",
        "my_plant": 2
    },
    "diary_set": [
        {
            "id": 1,
            "my_plant": {
                "pk": 2,
                "nickname": "가울이"
            },
            "content": "첫 번째 일지",
            "photo": "",
            "diary_created_at": "2022-07-26T08:15:09.427783Z",
            "public_private": false
        },
        {
            "id": 2,
            "my_plant": {
                "pk": 2,
                "nickname": "가울이"
            },
            "content": "두 번째 일지",
            "photo": "",
            "diary_created_at": "2022-07-26T08:16:08.831901Z",
            "public_private": false
        },
        {
            "id": 3,
            "my_plant": {
                "pk": 2,
                "nickname": "가울이"
            },
            "content": "쑥쑥 자라는 가울이",
            "photo": "",
            "diary_created_at": "2022-07-26T08:32:50.126572Z",
            "public_private": false
        }
    ],
    "diary_count": 3,
    "nickname": "가울이",
    "created_at": "2022-07-26T07:25:42.426355Z",
    "otp_code": "",
    "photo": "",
    "is_connected": false
}
```



### OTP 생성

- 기기와 연결되지 않았고 OTP도 없는 상태에서 OTP 발급
- 5분 후 자동으로 삭제 (blank)

- 로그인 사용자 - 토큰 사용
- POST

- URL

```
http://127.0.0.1:8000/api/v1/plants/myplant/{물주기 식물 pk}/otp/
```

- Request Parameters

| Name           | Type | Description             | Mandatory | Example |
| -------------- | ---- | ----------------------- | --------- | ------- |
| 물주기 식물 pk | Int  | 물주기 등록한 식물의 pk | O         | 1       |

- Response

```
{
    "otp_code": "636631"
}
```

```
{
    "result": "이미 발급되었거나 연결되었습니다."
}
```



### 연결 해제

- 기기와 연결상태가 True인 경우 연결 해제
- 로그인 사용자 - 토큰 사용

- POST
- URL

```
http://127.0.0.1:8000/api/v1/plants/myplant/{물주기 식물 pk}/disconnect/
```

- Request Parameters

| Name           | Type | Description             | Mandatory | Example |
| -------------- | ---- | ----------------------- | --------- | ------- |
| 물주기 식물 pk | Int  | 물주기 등록한 식물의 pk | O         | 1       |

- Response

```
{
	"is_connected": false
}
```

```
{
    "result": "연결상태를 확인해주세요."
}
```



### 식물 일지

- 나의 식물 별 일지 전체 조회, 일지 작성
- 로그인 사용자 - 토큰 사용
- GET, POST
- PUT/DELETE는 추후 추가 예정
- URL

```
http://127.0.0.1:8000/api/v1/plants/myplant/{물주기 식물 pk}/diary/
```

- Request Parameters

| Name           | Type | Description             | Mandatory | Example |
| -------------- | ---- | ----------------------- | --------- | ------- |
| 물주기 식물 pk | Int  | 물주기 등록한 식물의 pk | O         | 2       |

- Body: POST

| Key            | Type   | Description                   | Mandatory | Example            |
| -------------- | ------ | ----------------------------- | --------- | ------------------ |
| content        | String |                               | O         | 쑥쑥 자라는 가울이 |
| photo          | String |                               | 임시 X    |                    |
| public_private | Bool   | default=False<br />False=공개 |           |                    |

- Response

```
# GET
[
    {
        "id": 1,
        "my_plant": {
            "pk": 2,
            "nickname": "가울이"
        },
        "content": "첫 번째 일지",
        "photo": "",
        "diary_created_at": "2022-07-26T08:15:09.427783Z",
        "public_private": false
    },
    {
        "id": 2,
        "my_plant": {
            "pk": 2,
            "nickname": "가울이"
        },
        "content": "두 번째 일지",
        "photo": "",
        "diary_created_at": "2022-07-26T08:16:08.831901Z",
        "public_private": false
    }
]
```

```
# POST
{
    "id": 3,
    "my_plant": {
        "pk": 2,
        "nickname": "가울이"
    },
    "content": "쑥쑥 자라는 가울이",
    "photo": "",
    "diary_created_at": "2022-07-26T08:32:50.126572Z",
    "public_private": false
}
```



### 마이페이지(프로필)
- 플랜티넘과 함께한 날 수, 잎팔이 글 전체 조회 추가예정
- 나의 프로필만 확인 가능, 다른 사람의 프로필 확인 X
- 로그인 사용자 - 토큰 사용
- GET
- URL

```
http://127.0.0.1:8000/api/v1/accounts/profile/
```

- Response
```
{
    "pk": 1,
    "nickname": "",
    "email": "test1@ssafy.com",
    "phone_number": "",
    "addr": "",
    "zip_code": "",
    "myplant_count": 2
}
```



### 회원정보수정
- 닉네임, 이메일, 핸드폰번호, 주소, 우편번호만 수정 가능
- 비밀번호 변경은 별개의 요청
- 로그인 사용자 - 토큰 사용
- PUT
- URL

```
http://127.0.0.1:8000/api/v1/accounts/userinformation/
```

- Body

| Key            | Type   | Description                   | Mandatory | Example            |
| -------------- | ------ | ----------------------------- | --------- | ------------------ |
| nickname        | String |                               |          | 새로운닉네임 |
| email          | String |                               |     | ssafy@naver.com                   |
| phone_number | Bool   |  |           | 01012341234                   |
| addr | Bool   |  |           | seoul                   |
| zip_code | String   |  |           | 12345                   |

- Response
```
{
    "pk": 1,
    "nickname": "새로운닉네임",
    "email": "ssafy@naver.com",
    "phone_number": "01012341234",
    "addr": "seoul",
    "zip_code": "12345"
}
```




---------------------------------------------------------
### 마이페이지 (로그인정보+잎팔이정보)


내 잎팔이 글 전체 조회

=> 잎팔이 글 pk와 이미지url만 받아오기 (임시로 이미지 주소 보내기)


휴대폰번호 형식 지정



### 잎팔이

