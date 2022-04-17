# Django_project_like_lion - mission 2 ✍️

## modeling - Advanced_mission

![image1](/Image/mission2_1.PNG)
![image1](/Image/mission2_2.PNG)

### <mark>Inquiry class</mark>

* category : CharField(최대길이 지정 필수)
    - 최대길이 10
    - choices으로 선택지 내려오는 옵션 구성. cate 튜플 참조
    - null은 default로 필수요소.
* subject : CharField
    - 최대길이 50
* email : EmailField
    - 최대 길이 254
    - null = True -> NULL(정보없음) 가능 -> 필수 요소 X.
    - blank = True -> 빈 문자열 가능
* email_receive : BooleanField (체크박스)
    - default = False : 기본값 체크 X
* message : CharField
    - 최대길이 500
    - null = True -> NULL(정보없음) 가능 -> 필수 요소 X.
    - blank = True -> 빈 문자열 가능
* message_receive : BooleanField
* content : TextField
    - null, blank 없음 -> 공백이나, NULL 불가 -> 필수요소
* Image : ImageField
    - null = True -> NULL(정보없음) 가능 -> 필수 요소 X.
    - blank = True -> 빈 문자열 가능

<br>

### <mark>Answer class</mark>
* content : TextField
* reference : URLField
    - null = True -> NULL(정보없음) 가능 -> 필수 요소 X.
    - blank = True -> 빈 문자열 가능
* create_date : DateTimeField
    - auto_now_add = True -> 생성일자 자동으로 받아옴
* final_modify_date : DateTimeField
    - auto_now = True -> 수정일자 자동으로 받아옴.
* final_modifier : CharField
    - 최대길이 20
    - null = True -> NULL(정보없음) 가능 -> 필수 요소 X.
    - blank = True -> 빈 문자열 가능
* writer : ForeignKey
    - 작성자와 답변의 관계는 1 : N의 관계 이므로, N에 해당하는 답변이 ForeignKey를 가짐.
* inquiry : ForeignKey
     - 작성자와 답변의 관계는 1 : N의 관계 이므로, N에 해당하는 답변이 ForeignKey를 가짐.


<br><br><br><br><br>

---

# Django_project_like_lion - mission 1 😃
Django 시작!

### * 127.0.0.1:8000/ -> 뒤에 꼭 url 파일에 설정한 url적기!!!! (자꾸 깜빡함..)

## 1. basic_mission

- 기본값은 모두 0으로 초기화.
![basic1](https://user-images.githubusercontent.com/102863300/162603068-e5f52bd5-290c-43a2-842e-e745640488f2.PNG)

- 1~45까지의 번호 랜덤 추출.
![basic2](https://user-images.githubusercontent.com/102863300/162603076-d722de90-e1bb-47ff-90f6-85ccefe1b049.PNG)



## 2. challenge_mission

- form 데이터를 config.urls를 통해 해당 views파일의 함수로 전달.
![challenge1](https://user-images.githubusercontent.com/102863300/162603083-4a7b1c9b-9f8d-43a4-a526-d3a7d1c61981.PNG)

- 해당 숫자만큼을 list로 번호 출력.
![challenge2](https://user-images.githubusercontent.com/102863300/162603088-3a7bca4b-2e09-4ba9-8a06-7f4fbae94832.PNG)
