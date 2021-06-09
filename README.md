# 내가 쓰려고 만든 개인용 django 기반의 침투 웹 플랫폼 (docker 파일도 만들었는데 못 올림)
# This is django-based penetrance web platform I created for use

## 사용법(How to use?)

0. 세팅


    혹시 쓸 사람이 있을까? 해서 docker image도 만들었는데 사이즈 제한 때문에 못 올림. 그래서 씁니다.
    간단합니다. 먼저 칼리 리눅스에 이거 그대로 git clone하고 apache2를 설치합니다. 
    그리고 /etc/apache2/sites-available/000-default.conf를 다음과 같이 변경합니다.

    Who's gonna use this web platform? I don't sure. But maybe someone want to use it. So, I maked docker image which installed it
    But... I can't upload image because of the size limitation. So, I wrote this simple instrction. 
    Very simple. First, Clone it to kali linux to use git clone. and Install apache2 if your kali isn't installed.
    And change /etc/apache2/sites-available/000-default.conf like next section.

/etc/apache2/sites-available/000-default.conf

    <VirtualHost *:8000>
    ServerName put server name anything.
    <Directory <BASE_DIR>/penetrance_platform/penetrance_platform/config>
        <Files wsgi.py>
            Require all granted
        </Files>
    </Directory>
    <Directory <BASE_DIR>/penetrance_platform/penetrance_platform>
        Require all granted
    </Directory>
        #ServerName www.example.com
        
        WSGIDaemonProcess server name python-path=/usr/lib/python3/dist-packages 
        (If your python path is different paths, change this value)
        WSGIProcessGroup server name
        WSGIScriptAlias / <BASE_DIR>/penetrance_platform/penetrance_platform/config/wsgi.py process-group=server name
        Alias /static <BASE_DIR>/penetrance_platform/penetrance_platform/static

        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined
    </VirtualHost>

 <BASE_DIR>는 이거 clone한 디렉토리로 하면 됩니다. server name은 아무거나 해주세요!
 
 <BASE_DIR> is directory which is cloned project. server name is whatever you want !
 
 그리고 apache2 서비스를 실행하고 loopback 주소의 8000번 포트로 접속하시면 됩니다. 참 쉽죠?
 
 And run the apache2 service and access port 8000 of the loopback address. Isn't it easy?
 
 1. 기능

  1.1 포트 스캔(Port Scan)
  python-nmap 기반으로 스캐닝 합니다. 여러 스캔 방법을 지원합니다.
  
  Scanning based python-nmap. Supports various scanning methods.
  
  1.2 정보 누출(Information Disclosure)
  거창하게 정보 누출이라고 했지만 사실 Header에 서버 정보나 X-Powered-By를 확인하는 것 뿐입니다.
  
  It's Information Disclosure. But actually just checking Server and X-Powered-By in header.
  
  1.3 SQL Injection
  Blind SQL Injection 기반으로 체크합니다.
  
  Check vulnerability by blind SQL Injection code.
  
  1.4 XSS
  XSS 취약점이 존재하는 지 체크합니다.
  
  Check whether have XSS vulnerability.
  
  1.5 XXE
  XXE 취약점이 존재하는 지 체크합니다.
  
  Check whether have XXE vulnerability.
  
  1.6 Base64 Encoder/Decoder
  
  1.7 Hash generator
  MD5, SHA1, SHA256, SHA512
  
  1.8 File upload web shells
  파일 업로드 취약점에 이용할 수 있는 웹 쉘 코드나 웹 쉘의 GitHub 주소를 보여줍니다.
  
  Show GitHub address of a web shell or web shell that can be exploited for a file upload vulnerability.
  


2. 아직 개선해야 할 점

   1. 프론트엔드 전반적인 부분
   2. 포트 스캔 속도
   3. SQL, XSS,XXE 정확도 향상(확인 코드 추가)
   4. 봇 넷 개발 또는 그냥 안 하기!

   1. Front end overall part
   2. Port Scanning Rate
   3. Improve SQL, XSS, and XXE accuracy (add more verification code)
   4. Develop a botnet or just don't do it!

좀 거창하게 썼지만 사실 그냥 제가 편하게 모의해킹 프로젝트 시 쓸려고(+Django 연습할려고) 그냥 제 입맛에 맞게 편하게 만든 것 뿐 입니다.
더 좋은 웹 취약점 툴들이 많으니 그걸 쓰는 것을 추천합니다. 솔직히 제가 만들었지만 별로 좋지 않은 것 같거든요. (특히 프론트)
하지만 그래도 혹시 코드에 도움을 주실 분들은 언제나 환영합니다. 아니면 그냥 가져다 쓰셔도 됩니다!

I just made it comfortable to use it for a mock hacking or check vulnerability project (+Django practice) to suit my taste.
There are many better web vulnerability tools, so I recommend using them. Honestly, I made it, but I don't think it's good. (SPECIALLY FRONT)
But if you want to improve this, always welcome.
