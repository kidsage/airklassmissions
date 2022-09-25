# airklassmission 제출
 * 지원자 : 김석주
 
## 실행 가능한 방법
##### local server settings
```
cd [workspace]
git clone [git address]
cd djangomisstion
python3 manage.py runserver <- drf server 실행 코드
```

### accounts
##### singup [POST] http://127.0.0.1:8000/accounts/signup/dividiaul(or master)
- request
```json
{
  "username" : "str",
  "email" : "email address",
  "password" : "str",
  "password2" : "str"
}
```
- response

##### login [POST] http://127.0.0.1:8000/accounts/login
- require
```json
{
  "username" : "str",
  "email" : "email address",
  "password" : "str",
  "password2" : "str"
}
```

##### 개인페이지 [GET] http://127.0.0.1:8000/accounts/individual(or master)/dashboard
- require
header
> KEY : Authoriztion  
  VALUE : Token [signup 또는 login시 보이는 token value 기입]
- individual, master 사이 각 dashboard는 볼 수 없습니다(수정 가능).


### contentshub
##### klass list [GET] http://127.0.0.1:8000/contentshub/klass/list
- require : 없습니다.

##### create klass [POST] http://127.0.0.1:8000/contentshub/klass/create
- require
```json
{
  "title" : "str",
  "content" : "str"
}
```

##### klass detail [GET, PUT(UPDATE), DELETE] http://127.0.0.1:8000/contentshub/klass/detail/[id] <- pk는 klass_id 번호를 넣어주시면 됩니다.
- require : 없습니다.

##### (요구사항 외) comment는 구현 중에 시간이 부족해 진행하지 못했습니다.

### community
##### question list [GET] http://127.0.0.1:8000/community/question/list
- require : 없습니다

##### create question [GET] http://127.0.0.1:8000/community/question/create/[id] <- id는 klass_id 번호를 넣어주시면 됩니다.
- require
```json
{
  "content" : "str"
}
```

##### question detail [GET, PUT(UPDATE), DELETE] http://127.0.0.1:8000/community/question/create/[id] <- id는 question_id 번호를 넣어주시면 됩니다.
- require : GET, DELETE는 없습니다.
```json
{
  "content" : "str"
}
```

##### create answer [GET] http://127.0.0.1:8000/community/answer/create/[id] <- id는 question_id 번호를 넣어주시면 됩니다.
- require
```json
{
  "content" : "str"
}
```



## 구현 스펙
* DRF back-end 부분만 진행이 가능했습니다.
* 구현 기능 및 설명은 위 부분에 작성하였습니다.
* 기술 스택
  Python:3, Django:3.1.14, DRF:3.13.1



## 최종 구현 범위
  - 수강생, 강사, 강의, 질문, 답변 모델간의 관계를 구현.
  - 강의 생성 기능.
  - 강의 리스트 조회 가능
  - 강의는 강사만 생성이 가능.
  - 유저 및 강사 모두 질문 및 답변 가능.
  - 질문 리스트 조회 가능    
    - klass_id 확인 가능
    - 답변도 하위 depth에 같이 보임.
  - 유저는 모든 강의에 질문을 남길 수 있도록 진행.
  - 질문 삭제 가능.  
    > case 1) individual user, 답변 없음 = 삭제 가능  
      case 2) individual user, 답변 있음 = 삭제 불가능  
      case 3) master user = 삭제 가능  

모든 사용자는 특정 강의에 작성된 질문과 답변을 확인할 수 있습니다

## 가장 신경쓴 부분
 * MultiUser : User -> Individual/Master  
  두 유저로 나누어 bool값을 받아 나중에도 확장성 있는 개발을 할 수 있도록 적용했습니다.
  
 * Authenticated : permission을 기존 지원되는 isauthenticated와 함께 isindividualuser, ismasteruser로 유저들을 분리해 사용할 수 있게끔 적용했습니다
 
 * Serializer, View의 세분화 : 추후 수정 시 보다 직관적이로 확장성 있도록 serializer와 view를 세분화해서 진행했습니다.
 
 * model related_name : 1:N 관계에서 역참조 시 편하게 찾을 수 있도록 작성했습니다. 
