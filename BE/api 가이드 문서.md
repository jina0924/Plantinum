# 0. 목차

### 목차
[TOC]

### 시작하기

```python
python manage.py migrate
python manage.py loaddata plants.json juso.json
```



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



### 로그아웃

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



### 비밀번호 변경

- 로그인 사용자 - 토큰 사용
- POST
- URL

```
http://127.0.0.1:8000/api/v1/accounts/password/change/
```

- Body

| Key           | Type   | Description | Mandatory | Example |
| ------------- | ------ | ----------- | --------- | ------- |
| new_password1 | String |             | O         |         |
| new_password1 | String |             | O         |         |

- Response

```
{
    "detail": "New password has been saved."
}
```



### 마이페이지(프로필)

- 잎팔이 글 전체 조회 추가예정
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
    "nickname": "늘푸른소나무9865",
    "email": "test1@test.com",
    "phone_number": "",
    "addr": "",
    "zip_code": "",
    "myplant_count": 0,
    "dday": 1,
    "photo": "https://url.kr/s38eg6"
}
```



### 회원정보수정

- 닉네임, 이메일, 핸드폰번호, 주소, 우편번호, 사진만 수정 가능
- 비밀번호 변경은 별개의 요청
- 로그인 사용자 - 토큰 사용
- PUT
- URL

```
http://127.0.0.1:8000/api/v1/accounts/userinformation/
```

- Body

| Key          | Type   | Description | Mandatory | Example         |
| ------------ | ------ | ----------- | --------- | --------------- |
| nickname     | String |             | O         | 새로운닉네임    |
| email        | String |             | O         | 12345@naver.com |
| phone_number | String |             | O         | 01012341234     |
| addr         | String |             | O         | seoul           |
| zip_code     | String |             | O         | 12345           |
| photo        | Text   |             | O         |                 |

- Response

```
{
    "pk": 1,
    "nickname": "새로운닉네임",
    "email": "12345@naver.com",
    "phone_number": "01012341234",
    "addr": "seoul",
    "zip_code": "12345",
    "myplant_count": 0,
    "dday": 1,
    "photo": "https://url.kr/s38eg6"
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



### 등록용 식물 검색

- 물주기 등록시 사용
- 로그인 사용자 - 토큰 사용
- GET
- URL

```
http://127.0.0.1:8000/api/v1/plants/search/
```

- Response

```
[
    {
        "pk": 1,
        "name": "가울테리아"
    },
    {
        "pk": 2,
        "name": "개운죽"
    },
    {
        "pk": 3,
        "name": "골드크레스트 윌마"
    },
    {
        "pk": 4,
        "name": "공작야자"
    },
    ...
]
```



### ~~식물 이름 검색~~

- ~~물주기 등록시 사용~~
- ~~로그인 사용자 - 토큰 사용~~
- ~~GET~~
- ~~URL~~

```
http://127.0.0.1:8000/api/v1/plants/search/{검색어}/
```

- ~~Request Parameters~~

| ~~Name~~ | ~~Type~~ | ~~Description~~                          | ~~Mandatory~~ | ~~Example~~ |
| -------- | ------ | ---------------------------------------- | --------- | ------- |
| ~~검색어~~ | ~~String~~ | ~~한글명, 검색어를 포함하는 모든 식물 검색~~ | ~~O~~     | ~~백~~  |

- ~~Response~~

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



### 내식물 전체 조회

- 로그인 사용자 - 토큰 사용
- GET
- URL

```
http://127.0.0.1:8000/api/v1/plants/myplant/{username}/
```

- Request Parameters

| Name     | Type   | Description | Mandatory | Example  |
| -------- | ------ | ----------- | --------- | -------- |
| username | String | 유저id      | O         | testuser |

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
| photo    | String | 물주기 등록 대상 식물의 사진 | 기본값존재 |         |
| plantname | String | 사용자가 선택한 식물 이름 | O    | 개운죽     |

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
    "photo": "https://url.kr/d1acln",
    "is_connected": false
}
```



### 내식물 상세페이지

- 물주기 식물 별 상세페이지
- 로그인 사용자 - 토큰 사용
- GET
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



### 내식물 수정

- 닉네임과 사진만 수정 가능

- 로그인 사용자 - 토큰 사용

- PUT
- URL

```
http://127.0.0.1:8000/api/v1/plants/myplant/{물주기 식물 pk}/detail/
```

- Request Parameters

| Name           | Type | Description             | Mandatory | Example |
| -------------- | ---- | ----------------------- | --------- | ------- |
| 물주기 식물 pk | Int  | 물주기 등록한 식물의 pk | O         | 2       |

- Body

| Key      | Type   | Description                  | Mandatory | Example |
| -------- | ------ | ---------------------------- | --------- | ------- |
| nickname | String | 물주기 등록 대상 식물의 애칭 | O         | 깨운이  |
| photo    | String | 물주기 등록 대상 식물의 사진 | ?         |         |

- Response

```
{
    "id": 1,
    "user": {
        "pk": 2,
        "username": "test2",
        "nickname": "싱싱한올리브나무6759"
    },
    "plant_info": {
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
    "created_at": "2022-08-05T04:54:49.012014Z",
    "otp_code": null,
    "photo": "https://url.kr/d1acln",
    "is_connected": false
}
```



### 내식물 삭제

- 로그인 사용자 - 토큰 사용

- DELETE
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
    "result": "내식물이 삭제되었습니다."
}
```



### OTP 생성

- 기기와 연결되지 않았고 OTP도 없는 상태에서 OTP 발급
- 연결이 되지 않았는데 OTP가 있다면 현재 있는 값 보여주기
- 5분 후 자동으로 삭제 (NULL)

- 로그인 사용자 - 토큰 사용
- GET

- URL

```
http://127.0.0.1:8000/api/v1/plants/myplant/{내식물 식물 pk}/otp/
```

- Request Parameters

| Name           | Type | Description             | Mandatory | Example |
| -------------- | ---- | ----------------------- | --------- | ------- |
| 내식물 식물 pk | Int  | 내식물 등록한 식물의 pk | O         | 1       |

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



### OTP 상태 조회

- 식물의 OTP 상태 조회
- 값이 있으면 해당 값 리턴, 없으면 null 리턴
- 로그인 사용자 - 토큰 사용
- GET
- URL

```
http://127.0.0.1:8000/api/v1/plants/myplant/{내식물 식물 pk}/otp/status/
```

- Request Parameters

| Name           | Type | Description             | Mandatory | Example |
| -------------- | ---- | ----------------------- | --------- | ------- |
| 내식물 식물 pk | Int  | 내식물 등록한 식물의 pk | O         | 1       |

- Response

```
{
    "otp_code": "636631"
}
```

```
{
    "otp_code": null
}
```



### 연결 해제

- 기기와 연결상태가 True인 경우 연결 해제
- 로그인 사용자 - 토큰 사용

- GET
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

| Name      | Type | Description | Mandatory | Example |
| --------- | ---- | ----------- | --------- | ------- |
| 내식물 pk | Int  |             | O         | 2       |

- Body: POST

| Key            | Type   | Description                   | Mandatory | Example            |
| -------------- | ------ | ----------------------------- | --------- | ------------------ |
| content        | String |                               | O         | 쑥쑥 자라는 가울이 |
| photo          | String | **수정 예정**                 | 임시 X    |                    |
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



# 4. 잎팔이 관련 페이지

### 지역(시도) 조회

- GET
- URL

```
http://127.0.0.1:8000/api/v1/leaf82/search/sido/
```

- Response

```
[
    {
        "sido": "서울특별시"
    },
    {
        "sido": "부산광역시"
    },
    {
        "sido": "대구광역시"
    },
    {
        "sido": "인천광역시"
    },
    {
        "sido": "광주광역시"
    },
    {
        "sido": "대전광역시"
    },
    {
        "sido": "울산광역시"
    },
    {
        "sido": "경기도"
    },
    {
        "sido": "강원도"
    },
    {
        "sido": "충청북도"
    },
    {
        "sido": "충청남도"
    },
    {
        "sido": "전라북도"
    },
    {
        "sido": "전라남도"
    },
    {
        "sido": "경상북도"
    },
    {
        "sido": "경상남도"
    },
    {
        "sido": "제주특별자치도"
    }
]
```



### 동네(시군구) 조회

- GET
- URL

```
http://127.0.0.1:8000/api/v1/leaf82/search/{시도}/sigungu/
```

- Request Parameters

| Name | Type   | Description | Mandatory | Example        |
| ---- | ------ | ----------- | --------- | -------------- |
| 시도 | String | 한글명      | O         | 제주특별자치도 |

- Response

```
[
    {
        "pk": 259,
        "sigungu": "제주시"
    },
    {
        "pk": 260,
        "sigungu": "서귀포시"
    }
]
```



### 잎팔이 글 생성

- 시도/시군구 순차적 검색 필요
- 로그인 사용자 - 토큰 사용
- POST
- URL

```
http://127.0.0.1:8000/api/v1/leaf82/new/
```

- Body

| Key            | Type   | Description                                | Mandatory  | Example    |
| -------------- | ------ | ------------------------------------------ | ---------- | ---------- |
| sido           | String | 시도                                       | O          | 서울특별시 |
| sigungu        | String | 시군구                                     | O          | 종로구     |
| plantname      | String | 식물이름                                   | O          | 산세베리아 |
| content        | Text   | 내용                                       | O          | 채팅주세요 |
| price          | Int    | 가격                                       | O          | 20000      |
| category_class | String | 분양해요/분양받아요                        | O          | 분양해요   |
| status_class   | String | 판매중/거래완료/예약중<br />default=판매중 |            |            |
| photo          | Text   |                                            | 기본값존재 |            |

- Response

```
{
    "id": 3,
    "user": {
        "pk": 1,
        "username": "test1",
        "nickname": "새내기참나무4979"
    },
    "addr": {
        "id": 108,
        "sido": "경기도",
        "sigungu": "용인시 처인구"
    },
    "plantname": "싱고니움",
    "photo": "https://url.kr/d1acln",
    "created_at": "2022-08-04T06:25:01.655280Z",
    "content": "연락주세요",
    "price": 15000,
    "category_class": "분양해요",
    "status_class": "판매중",
    "posting_addr": 207303
}
```



### 잎팔이 글  전체 조회

- 잎팔이 글 전체 조회 (지역 상관 X)
- 최신순으로 조회
- GET
- URL

```
http://127.0.0.1:8000/api/v1/leaf82/
```

- Response

```
[
    {
        "pk": 4,
        "plantname": "싱고니움",
        "photo": "https://url.kr/d1acln",
        "price": 15000,
        "category_class": "분양해요",
        "status_class": "판매중",
        "addr": {
            "id": 108,
            "sido": "경기도",
            "sigungu": "용인시 처인구"
        },
        "posting_addr": 426408,
        "user": {
            "pk": 1,
            "username": "test1"
        }
    },
    {
        "pk": 3,
        "plantname": "싱고니움",
        "photo": "https://url.kr/d1acln",
        "price": 15000,
        "category_class": "분양해요",
        "status_class": "판매중",
        "addr": {
            "id": 108,
            "sido": "경기도",
            "sigungu": "용인시 처인구"
        },
        "posting_addr": 207303,
        "user": {
            "pk": 1,
            "username": "test1"
        }
    },
    {
        "pk": 2,
        "plantname": "싱고니움",
        "photo": "https://url.kr/d1acln",
        "price": 15000,
        "category_class": "분양해요",
        "status_class": "판매중",
        "addr": {
            "id": 108,
            "sido": "경기도",
            "sigungu": "용인시 처인구"
        },
        "posting_addr": 426408,
        "user": {
            "pk": 1,
            "username": "test1"
        }
    }
]
```



### ~~잎팔이 글 특정 지역/동네별 조회~~

- ~~시도(지역)과 시군구(동네)를 함께 요청~~
- ~~`경기도 용인시` 같은 경우, `용인시`를 입력하면 `용인시/용인시 처인구/용인시 기흥구/용인시 수지구` 모두 검색~~
- ~~최신순으로 조회~~
- ~~GET~~
- ~~URL~~

```
http://127.0.0.1:8000/api/v1/leaf82/{시도}/{시군구}/
```

- ~~Request Parameters~~

| Name   | Type   | Description | Mandatory | Example |
| ------ | ------ | ----------- | --------- | ------- |
| 시도   | String | 한글명      | O         | 경기도  |
| 시군구 | String | 한글명      | O         | 용인시  |

- Response

```
[
    {
        "id": 7,
        "user": {
            "pk": 3,
            "username": "test3",
            "nickname": "촉촉한올리브나무5182"
        },
        "addr": {
            "id": 109,
            "sido": "경기도",
            "sigungu": "용인시 기흥구"
        },
        "plantname": "루스커스",
        "photo": "https://url.kr/d1acln",
        "created_at": "2022-08-02T15:37:44.139568Z",
        "content": "연락주세요",
        "price": 15000,
        "category_class": "분양해요",
        "status_class": "판매중"
    },
    {
        "id": 6,
        "user": {
            "pk": 2,
            "username": "test2",
            "nickname": "싱싱한귤나무1120"
        },
        "addr": {
            "id": 108,
            "sido": "경기도",
            "sigungu": "용인시 처인구"
        },
        "plantname": "싱고니움",
        "photo": "https://url.kr/d1acln",
        "created_at": "2022-08-02T15:37:32.734002Z",
        "content": "연락주세요",
        "price": 15000,
        "category_class": "분양해요",
        "status_class": "판매중"
    },
    {
        "id": 5,
        "user": {
            "pk": 1,
            "username": "test1",
            "nickname": "새내기야자나무9690"
        },
        "addr": {
            "id": 107,
            "sido": "경기도",
            "sigungu": "용인시"
        },
        "plantname": "호야",
        "photo": "https://url.kr/d1acln",
        "created_at": "2022-08-02T15:37:22.502227Z",
        "content": "연락주세요",
        "price": 15000,
        "category_class": "분양해요",
        "status_class": "판매중"
    }
]
```



### 잎팔이 검색

- 선택한 식물이름/시도/시군구에 해당하는 모든 글 조회
- 식물이름은 `무늬`만 입력해도 `무늬관음죽`, `무늬산호수` 등을 모두 포함하여 조회
- 시도는 반드시 일치하는 값만 조회
- 시군구는 `용인시`를 검색한다면 `용인시`, `용인시 처인구` `용인시 기흥구` 등을 모두 포함하여 조회
- 검색어/시도/시군구 하나만 선택 가능, 중복선택 가능
- 값이 있는 것만 키와 값을 담아 요청
- 최신순으로 조회

- GET
- URL

```
http://127.0.0.1:8000/api/v1/leaf82/search
```

- Params

| Key       | Type   | Description      | Mandatory | Example |
| --------- | ------ | ---------------- | --------- | ------- |
| plantname | String | 식물이름(검색어) |           |         |
| sido      | String | 시도             |           | 경기도  |
| sigungu   | String | 시군구           |           | 용인시  |

- Response

```
[
    {
        "pk": 7,
        "plantname": "산세베리아",
        "photo": "https://url.kr/d1acln",
        "price": 15000,
        "category_class": "분양해요",
        "status_class": "판매중",
        "addr": {
            "id": 108,
            "sido": "경기도",
            "sigungu": "용인시 기흥구"
        },
        "posting_addr": 336921,
        "user": {
            "pk": 2,
            "username": "test2"
        }
    },
    {
        "pk": 6,
        "plantname": "산세베리아",
        "photo": "https://url.kr/d1acln",
        "price": 15000,
        "category_class": "분양해요",
        "status_class": "판매중",
        "addr": {
            "id": 107,
            "sido": "경기도",
            "sigungu": "용인시"
        },
        "posting_addr": 615947,
        "user": {
            "pk": 2,
            "username": "test2"
        }
    },
    {
        "pk": 2,
        "plantname": "싱고니움",
        "photo": "https://url.kr/d1acln",
        "price": 15000,
        "category_class": "분양해요",
        "status_class": "판매중",
        "addr": {
            "id": 108,
            "sido": "경기도",
            "sigungu": "용인시 처인구"
        },
        "posting_addr": 426408,
        "user": {
            "pk": 1,
            "username": "test1"
        }
    }
]
```



### 잎팔이 글 상세 조회

- 특정 잎팔이 글 pk에 해당하는 글 상세 조회
- GET
- URL

```
http://127.0.0.1:8000/api/v1/leaf82/{username}/{posting_addr}/
```

- Request Parameters

| Name         | Type   | Description                                                  | Mandatory | Example |
| ------------ | ------ | ------------------------------------------------------------ | --------- | ------- |
| username     | String | 유저id                                                       | O         | test1   |
| posting_addr | Int    | 잎팔이 글 작성시 부여되는 랜덤 값<br />한 유저 내에서 중복되지 않음 | O         | 426408  |

- Response

```
{
    "id": 2,
    "user": {
        "pk": 1,
        "username": "test1",
        "nickname": "새내기참나무4979"
    },
    "addr": {
        "id": 108,
        "sido": "경기도",
        "sigungu": "용인시 처인구"
    },
    "plantname": "싱고니움",
    "photo": "https://url.kr/d1acln",
    "created_at": "2022-08-04T05:08:32.067416Z",
    "content": "연락주세요",
    "price": 15000,
    "category_class": "분양해요",
    "status_class": "판매중",
    "posting_addr": 426408
}
```



### 잎팔이 글 수정

- 로그인 사용자 - 토큰 사용

- PUT
- URL

```
http://127.0.0.1:8000/api/v1/leaf82/{username}/{posting_addr}/
```

- Request Parameters

| Name         | Type   | Description                                                  | Mandatory | Example |
| ------------ | ------ | ------------------------------------------------------------ | --------- | ------- |
| username     | String | 유저id                                                       | O         | test1   |
| posting_addr | Int    | 잎팔이 글 작성시 부여되는 랜덤 값<br />한 유저 내에서 중복되지 않음 | O         | 426408  |

- Body

| Key            | Type   | Description                                | Mandatory | Example    |
| -------------- | ------ | ------------------------------------------ | --------- | ---------- |
| sido           | String | 시도                                       | O         | 서울특별시 |
| sigungu        | String | 시군구                                     | O         | 종로구     |
| plantname      | String | 식물이름                                   | O         | 싱고니움   |
| content        | Text   | 내용                                       | O         | 연락주세요 |
| price          | Int    | 가격                                       | O         | 15000      |
| category_class | String | 분양해요/분양받아요                        | O         | 분양해요   |
| status_class   | String | 판매중/거래완료/예약중<br />default=판매중 | O         | 거래완료   |
| photo          | Text   |                                | ?         ||

- Response

```
{
    "id": 1,
    "user": {
        "pk": 1,
        "username": "test1",
        "nickname": "새내기참나무4979",
        "photo": "https://url.kr/s38eg6"
    },
    "addr": {
        "id": 1,
        "sido": "서울특별시",
        "sigungu": "종로구"
    },
    "plantname": "싱고니움",
    "photo": "https://url.kr/d1acln",
    "created_at": "2022-08-04T04:20:42.359078Z",
    "content": "연락주세요",
    "price": 15000,
    "category_class": "분양해요",
    "status_class": "거래완료",
    "posting_addr": 323845
}
```

```
{
    "result": "잘못된 접근입니다."
}
```



### 잎팔이 글 삭제

- 로그인 사용자 - 토큰 사용

- DELETE
- URL

```
http://127.0.0.1:8000/api/v1/leaf82/{username}/{posting_addr}/
```

- Request Parameters

| Name         | Type   | Description                                                  | Mandatory | Example |
| ------------ | ------ | ------------------------------------------------------------ | --------- | ------- |
| username     | String | 유저id                                                       | O         | test1   |
| posting_addr | Int    | 잎팔이 글 작성시 부여되는 랜덤 값<br />한 유저 내에서 중복되지 않음 | O         | 426408  |

- Response

```
{
    "result": "게시글이 삭제되었습니다."
}
```

```
{
    "result": "잘못된 접근입니다."
}
```



# 5. 추가 예정

### 마이페이지 (로그인정보+잎팔이정보)


내 잎팔이 글 전체 조회

=> 잎팔이 글 pk와 이미지url만 받아오기 (임시로 이미지 주소 보내기)

휴대폰번호 형식 지정



accounts/user/ 했을 때 나오는 정보 수정 가능한지





