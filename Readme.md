# Pinterest 모티브로한 Blog 개발
> Version 1.0 : http://141.164.39.223/

## 목차

1. [개발 목적](#개발-목적)
2. [개발 목표](#개발-목표)
3. [사용 기술](#사용-기술)
4. [개발한 기능](#개발한-기능)
5. [배포](#배포)
6. [향후 개선 과제](#향후-개선-과제)

***

## 개발 목적


- 간단한 Blog 개발을 통해 Django CURD 학습
- 개발부터 배포까지 해보며 웹 프로그래밍의 전반적인 흐름 학습
<br>

***

## 개발 목표

- Pinterest 모티브로한 Blog 개발
- Docker, AWS를 활용해 배포
- 지속적인 개선을 통한 Upgrade

***

## 사용 기술

- OS : Window
- IDE : Pycharm Community
- 언어 : Python, HTML/CSS, Javascript
- Framework : Django
- Web Server : Nginx
- WSGI : Gunicorn


***

## 개발한 기능

- Login(LoginView), Logout(LogoutView), SignUp(CreateView)

<br>

- MyPage : 프로필 설정, 변경 및 계정 삭제 <br>
![image](https://user-images.githubusercontent.com/76996686/133378848-7b673f58-5214-4bfd-9e1f-87732ec00970.png)

<br>

- Article
  - 로그인 한 유저만 게시글 작성, 본인 글만 수정 및 삭제 
  - 댓글 작성, 카테고리 
  - magicgrid.js 활용해 카드형태 설정(https://github.com/e-oj/Magic-Grid )

![image](https://user-images.githubusercontent.com/76996686/133379495-c51846f8-1c7b-419f-8cfd-8c8408b3319c.png)

![image](https://user-images.githubusercontent.com/76996686/133379610-8b3a2ef4-2359-47d3-911c-3ca3a8c856bb.png)

![image](https://user-images.githubusercontent.com/76996686/133380365-5491e19d-46ba-4d5b-9d59-ee1da9cdecf0.png)

<br>

- Project
  - 주제 별로 article 모음
  - 구독 기능

![image](https://user-images.githubusercontent.com/76996686/133379820-d2c4353a-2a33-48a5-9775-e7292346cb3d.png)

![image](https://user-images.githubusercontent.com/76996686/133380071-24387e25-235a-4ea1-8b92-aa496165f0a0.png)

<br>

- Subscription
  - 구독한 카테고리 게시글 모아보기

<br>

***

## 배포

- Vultr를 통해 VPS 대여 
- docker portainer 활용해 GUI 환경 사용 및 Stack 활용해 container 생성
- Web Server : Nginx
- WSGI : Gunicorn

***

## 향후 개선 과제

- [ ] 메뉴 이름 변경(이름과 기능이 직관적이지 않음)
- [ ] 디자인 개선 (카드가 더 촘촘하게)
- [ ] 좋아요 기능 추가(인스타그램 처럼)
- [ ] 개선 후 AWS 활용해 배포


