# Send.U.Scent | 빅데이터 기반 향수 추천 서비스
> 당신의 향을 보내면, 그와 맞는 향을 보냅니다.


[Send.U.Sccent 바로가기](https://j5c204.p.ssafy.io/)

[팀 노션 바로가기](https://www.notion.so/2C204-2074811e7e5f4be1941bb8beb4dfd17a)

[와이어프레임 바로가기](https://www.figma.com/file/nOYwQvGCuQm6wn4ViNsOC4/ssafy_bigdata)

[ERD바로가기](https://www.erdcloud.com/d/uR88eXDqtNW94szqT) 

[UCC 바로가기](https://www.youtube.com/watch?v=122BitBJkXI)

[기능명세, 사이트맵 바로가기](https://docs.google.com/spreadsheets/d/1LIR8_5KgDMEcU9p-PB4OfCF3BUwijQTWsk4rQ5JHxT0/edit#gid=0)

### **목차**

---

0. [팀 소개](#0.-팀-소개)

1. [서비스 소개](#1.-서비스-소개)

2. [기술스택](#2.-기술-스택)

3. [데이터 수집 및 추천 알고리즘](#3.-데이터-수집-및-추천-알고리즘)

4. [아키텍처 상세](#4.-아키덱처-상세)

5. [레이아웃 및 디자인](#5.-레이아웃-및-디자인)

---

## 0. 팀 소개

기능별로 역할을 나누었고 프론트엔드는 Vue.js ,원하는 백엔드 프레임 워크를 사용하였습니다.

- **팀장** 이태성 : 백엔드(Node.js)/프론트엔드
- 팀원 권예빈 : 백엔드(Django)/프론트엔드, 향수 테스트,메인페이지, about페이지
- 팀원 박세영 : 백엔드(SpringBoot)/프론트엔드, 향수 리스트
- 팀원 윤소영 : 백엔드(SpringBoot)/프론트엔드, 마이페이지, 로그인/회원가입
- 팀원 이연지: 백엔드(Django)/프론트엔드, 데이터가공, 향수 상세페이지, 추천알고리즘

### 🗓️구현 기간

2021.8.30 - 10.8

## 1. 서비스 소개

> 빅데이터 기반 개인 맞춤 향수 추천 서비스
> 

![image](https://user-images.githubusercontent.com/32251962/136781069-97a7afb7-082f-4a5c-b438-ca6670a56c64.png)

![image](https://user-images.githubusercontent.com/32251962/136781139-f466b36f-eff5-4cc6-98f1-fbf76a3d1010.png)


고객이 원하는 향수를 쉽게 찾고, 자신의 취향에 맞는 향수를 추천받을 수 있도록 하여 구매에 도움을 주는 웹 서비스입니다.

### 1.1. 타겟 고객군

- **향수에 대해 잘 모르는 사람**
    
    향에 대해 잘 몰라서 자신에게 맞는 향을 모르는 사람, 향을 직접 맡으러 오프라인 매장에 가기엔 귀찮은 고객
    
- **시향하러 가고싶은 사람**
    
    많은 향수 중에 추천을 받아 직접 시향하러 가고 싶은 사람
    
- **향수 선물을 하고 싶은 사람**
    
    받는 사람의 향수 취향을 잘 몰라서 고르기 어려운 사람
    

### 1.2. 주요 기능

### 1.2.1. 성향테스트로 맞춤 향수 추천

1. 8가지 질문에 대한 답을 통해 나온 결과로 3만여가지 데이터베이스에서 SQL로 SELECT하여 추출된 5가지 향수를 추천해드립니다.
- 질문 화면

![image](https://user-images.githubusercontent.com/32251962/136781169-98d322ed-2dfc-49a3-8558-cdbfedd2eb79.png)

- 향수 추천 결과 화면

![image](https://user-images.githubusercontent.com/32251962/136781176-b4f4505b-4835-4085-84a9-6e406a5f1ff0.png)
![image](https://user-images.githubusercontent.com/32251962/136781184-c2480fdc-fb07-436b-aa27-c3a1defa7dfb.png)
![image](https://user-images.githubusercontent.com/32251962/136781197-aed55ddc-a34b-493c-8251-8a9c2a1ec406.png)

2. 8가지 문항에 대한 결과를 가지고 추천을 한 5가지 향수와 4가지 문항으로만 추천을 한 5가지 향수 총 10가지 향수에서 Accord를 뽑아 가장 많이 누적된 횟수를 내림차순 정렬하여 보여줍니다.
    
    1.1 가장 상위 Accord 3개를 상단 제목 아래에 보여줍니다.
    
3. Accord들을 시각적으로 표현하기 위해 글자들이 원 안에 움직이도록 하여 역동적인 공처럼 구현하였습니다.
- 남을 위한 테스트

![image](https://user-images.githubusercontent.com/32251962/136781240-d7a4b92c-ab15-422f-bd4d-3fe663746234.png)

향수 선물을 위한 상대를 위한 추천 테스트는  받는 사람의 이름을 입력하고 테스트 가능하도록 했습니다.

### 1.2.2. 향수 상세 정보 제공

1. **31,987개**의 향수 정보를 확인할 수 있습니다.
향수명, 향수 사진, 브랜드, 성별, 탑 노트, 미들 노트,베이스 노트, 평점 정보를 제공합니다.
하트버튼을 클릭하면 관심목록에 추가할 수 있습니다.

![image](https://user-images.githubusercontent.com/32251962/136781263-06b2dc74-b56c-4ae1-b1ab-51f2fa179245.png)

2. 향수의 지속력(longevity)과 잔향(sillage) 정도, 계절별 추천도와 낮/밤 추천도를 시각적으로 확인할 수 있습니다.

![image](https://user-images.githubusercontent.com/32251962/136781277-3837f005-30ac-4d56-816d-103fe00f4ba1.png)

![image](https://user-images.githubusercontent.com/32251962/136781286-b70eaf00-f7b0-4cce-9a0c-6d3b950cc30c.png)

3. **코사인 유사도**를 기반으로 향수간 유사도가 높은 상위 10개의 향수를 보여줍니다.
마음에 드는 향수와 유사한 향수를 추천 받을 수 있습니다.

![image](https://user-images.githubusercontent.com/32251962/136781304-e204c600-8316-4d4d-a7b5-e75d8e71e7c1.png)

4. 이미지로 분위기를 느낄 수 있도록 향의 핵심 조화(accord)를 표현하였습니다.

![image](https://user-images.githubusercontent.com/32251962/136781452-4dafe420-75a9-42bc-84a4-d083d72ff0a1.png)

5. 향의 노트들도 상위 3개씩 이미지로 나타내어 원재료를 한눈에 파악할 수 있도록 했습니다.

![image](https://user-images.githubusercontent.com/32251962/136781483-8dfaad74-1fe6-40b9-9e02-73ccfadd6f4c.png)

6. 향수를 보유하고 있는 회원들의 리뷰를 보여줍니다.

![image](https://user-images.githubusercontent.com/32251962/136781506-11c84b9f-fa2c-49d4-94cd-a387820d3b0a.png)

### 1.2.3. 사이트 보유 향수 리스트 및 필터 기능

1. 사이트에서 제공하고 있는 향수 정보를 상위 평점 기준 1000개 우선 제시
2. 향수 이름 또는 브랜드명 검색 기능

![image](https://user-images.githubusercontent.com/32251962/136781525-ef8c9608-e598-479e-9f21-29bfe6ee433a.png)

3. 계절별, 시간대별, 성별 향수 필터 기능  

![image](https://user-images.githubusercontent.com/32251962/136781538-b53b6228-dc22-497e-a354-8e0e0cd11870.png)

- 원하는 필터만을 선택적으로 체크하여 향수리스트를 조회할 수 있습니다. JPA 동적 쿼리를 사용하여 값의 유무에 따라 쿼리문을 다르게 작성하여 실행하도록 하였습니다.

### 1.2.4. 마이페이지 성향 정보 및 보유 향수/관심 목록

1. 성향 테스트 기반 선호 Accord 정보 확인
- 테스트 전과 후
    
    ![image](https://user-images.githubusercontent.com/32251962/136781549-e2c04c5b-75da-4be3-ba8a-23ad6b4ba88d.png)
    
    ![image](https://user-images.githubusercontent.com/32251962/136781569-35365bbf-35d4-4a8e-a68b-54c8634fa9c4.png)
    
2. 가지고 있는 목록(보유 향수) 등록 및 관리
- 검색 후 보유 향수 등록
    
    ![image](https://user-images.githubusercontent.com/32251962/136781582-f08ace78-d517-4f83-9a50-f887e9a60886.png)
    
- 목록에서 확인 및 삭제
    
    ![image](https://user-images.githubusercontent.com/32251962/136781595-7c8e6a8a-e7f5-4d8e-9c76-a67659c42c0b.png)
    
- 보유 향수에 한해서 평점과 리뷰 등록
    
    ![image](https://user-images.githubusercontent.com/32251962/136781599-ab020e16-8189-4a56-9395-c65eb6520d27.png)
    
- 등록한 리뷰는 마이페이지 메인에서 확인 및 삭제 가능
    
    ![image](https://user-images.githubusercontent.com/32251962/136781623-014191cc-5cb9-4023-8660-f19521f89ca6.png)
    
- 보유 향수 목록을 기반으로 평가한 평점, 리뷰에 따라 가중치를 적용하여 추천 목록 갱신
    
    ![image](https://user-images.githubusercontent.com/32251962/136781634-bed0bbf5-6d93-4d3f-a0ad-5b640e0544f1.png)
    
3. 관심 목록 등록 및 관리
- 향수 상세페이지에서 등록한 관심 향수 목록 확인
    
    ![image](https://user-images.githubusercontent.com/32251962/136781652-c0d15ce2-ad3e-4d09-89f0-40fa06914892.png)
    
- 목록에서 관심 등록 및 해제 관리
    
    ![image](https://user-images.githubusercontent.com/32251962/136781656-1715bbdf-105d-4845-bce7-460411fcde62.png)
    
- 구매한 향수는 보유 목록으로 이동
    
    ![image](https://user-images.githubusercontent.com/32251962/136781664-e3f74f32-d28a-400b-b442-0f813cf3d2ff.png)
    

## 2. 기술 스택

### **2.1. 데이터 수집 및 처리**

> Raw 데이터를 가공해서 의미있는 자료로 만들고, 정규화하여 DB에 저장합니다.

- Python 3.8.7
- Pandas
- Numpy

### **2.2. 백엔드**

- Python 3.8.7
- Django 3.2.7
    1. 라우팅, 직렬화, 테스트, 관리자 페이지 등 기능 지원이 다양하고 풍부하다.
    2. Python이다.(Python의 다양한 데이터 분석 라이브러리 사용 가능)
- DRF(Django Rest Framework)
    
    > DB의 데이터를 조회하고 유의미한 모음으로 직렬화하여, 클라이언트와 통신하는 API서버를 작성합니다.
    
- Swagger
- Postman
- Spring 2.5.4
- MariaDB

### **2.3. 프론트엔드**

- Vue.js
    1. 최고 점유율 라이브러리
    2. Vue 3 버전의 최신라이브러리 적용

### **2.4. 배포**

- AWS EC2
- Nginx

### **2.4. 프로젝트 관리**

- GitLab
- Notion
- Jira
- Google Sheet

## 3. 데이터 수집 및 추천 알고리즘

### **3.1. 데이터 수집**

- Kaggle 에서 5만개의 데이터셋과 4만개의 데이터셋 2가지를 수집한 후, 값이 존재하지 않는 row를 삭제한 후, JOIN하여 향수 이름, 이미지, 브랜드, 조화(향), 탑노트, 미들노트, 베이스노트, 계절감, 시간대, 연령, 성별, 평점 컬럼으로 구성하고 값을 수정하여 31,987개의 data를 추출했습니다.

### **3.2. 추천알고리즘**

- **코사인 유사도**

![image](https://user-images.githubusercontent.com/32251962/136782355-e5b5c0b7-1e94-4eb0-8dcb-c2a216c6a002.png)

코사인 유사도(cosine similarity)는 내적공간의 두 벡터간 각도의 코사인값을 이용하여 측정된 벡터간의 유사한 정도를 의미합니다. 31,987개의 향수데이터를 82가지의 조화로 코사인 유사도를 측정하여 상위 10개의 item을 추천하도록 구성했습니다.

![image](https://user-images.githubusercontent.com/32251962/136782367-86f00299-3e75-4e35-a7a0-a46280f6d914.png)

- **사용자 평점 가중치 및 성향 반영**

사용자가 평가한 향수의 평점과 빈도수를 반영하여 가중치 계산을 한 후, 상위 3개 accord를 추출하여 사용자가 선호하는 지속력과 잔향, 계절감을 반영하여 해당하는 향수 전체 목록 중 랜덤으로 10개씩 추천하도록 구성했습니다.

![image](https://user-images.githubusercontent.com/32251962/136782387-bee667df-e8f3-4792-abc6-38397b505578.png)

## 4. 아키텍처 상세

- 아키텍처

![image](https://user-images.githubusercontent.com/32251962/136782460-c312580a-bf77-4ab0-96a1-3d06845a50d1.png)

- ERD

![image](https://user-images.githubusercontent.com/32251962/136782470-0f6692aa-ca1a-4831-95b8-3c761e339554.png)

## 5. 레이아웃 및 디자인

- 와이어 프레임 (Figma)

![image](https://user-images.githubusercontent.com/32251962/136782625-408443e9-21eb-4e62-8feb-534e96d80e73.png)

