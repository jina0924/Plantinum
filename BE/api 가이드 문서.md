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
http://127.0.0.1:8000/accounts/signup/
```

- Body

| Key          | Type   | Description     | Mandatory | Example        |
| ------------ | ------ | --------------- | --------- | -------------- |
| username     | String | 유저아이디      | O         | idsampleuser   |
| email        | String | 이메일          |           |                |
| password1    | String | 비밀번호        | O         | testpassword   |
| password2    | String | 비밀번호 재입력 | O         | testpassword   |
| phone_number | String | 폰넘버          | O         | 01012345678    |
| addr         | String | 주소            | O         | seoul          |
| zip_code     | String | 우편번호        | O         | 12345          |
| nickname     | String | 닉네임          | O         | samplenickname |

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
http://127.0.0.1:8000/accounts/login/
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
http://127.0.0.1:8000/accounts/logout/
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
http://127.0.0.1:8000/plants/
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
http://127.0.0.1:8000/plants/search/{식물이름}/
```

- Request Parameters

| Name     | Type   | Description                              | Mandatory | Example |
| -------- | ------ | ---------------------------------------- | --------- | ------- |
| 식물이름 | String | 한글명, 검색어를 포함하는 모든 식물 검색 | O         | 무늬    |

- Response

```
[
    {
        "name": "무늬관음죽"
    },
    {
        "name": "무늬마삭줄"
    },
    {
        "name": "무늬벤자민고무나무"
    },
    ...
]
```



### 물주기 전체 식물 조회

- 로그인 사용자 - 토큰 사용
- GET
- URL

```
http://127.0.0.1:8000/plants/myplant/
```

- Response

```
[
    {
        "id": 1,
        "user": {
            "pk": 2,
            "username": "idsampleuser",
            "nickname": "samplenickname"
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
        "nickname": "깨운이",
        "created_at": "2022-07-22T05:23:33.900553Z",
        "otp_code": "3190",
        "photo": "",
        "is_connected": false
    }
]
```



### 물주기 등록

- 물주기 등록 전 반드시 식물 이름 검색이 선행되어야 함
- 로그인 사용자 - 토큰 사용
- POST
- URL

```
http://127.0.0.1:8000/plants/myplant/{식물이름}/
```

- Request Parameters

| Name     | Type   | Description             | Mandatory | Example |
| -------- | ------ | ----------------------- | --------- | ------- |
| 식물이름 | String | 검색 후 선택한 식물이름 | O         | 개운죽  |

- Body

| Key      | Type   | Description                  | Mandatory | Example |
| -------- | ------ | ---------------------------- | --------- | ------- |
| nickname | String | 물주기 등록 대상 식물의 애칭 | O         | 깨운이  |

- Response

```
{
    "id": 1,
    "user": {
        "pk": 2,
        "username": "idsampleuser",
        "nickname": "samplenickname"
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
    "nickname": "깨운이",
    "created_at": "2022-07-22T05:23:33.900553Z",
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
http://127.0.0.1:8000/plants/myplant/{물주기 식물 pk}/otp/
```

- Request Parameters

| Name           | Type | Description             | Mandatory | Example |
| -------------- | ---- | ----------------------- | --------- | ------- |
| 물주기 식물 pk | Int  | 물주기 등록한 식물의 pk | O         | 1       |

- Response

```
{
    "otp_code": "6366"
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
http://127.0.0.1:8000/plants/myplant/{물주기 식물 pk}/disconnect/
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


