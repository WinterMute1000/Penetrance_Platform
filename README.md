# 내가 쓰려고 만든 개인용 django 기반의 침투 웹 플랫폼 (docker 파일도 만들었는데 못 올림)
# This is django-based penetrance web platform I created for use

## 사용법(How to use?)

0. 세팅
혹시 쓸 사람이 있을까? 해서 docker image도 만들었는데 사이즈 제한 때문에 못 올림. 그래서 씁니다.
간단합니다. 먼저 칼리 리눅스에 이거 그대로 git clone하고 apache2를 설치합니다. 
그리고 /etc/apache2/sites-available/000-default.conf를 다음과 같이 변경합니다.

0. Setting
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

        # The ServerName directive sets the request scheme, hostname and port that
        # the server uses to identify itself. This is used when creating
        # redirection URLs. In the context of virtual hosts, the ServerName
        # specifies what hostname must appear in the request's Host: header to
        # match this virtual host. For the default virtual host (this file) this
        # value is not decisive as it is used as a last resort host regardless.
        # However, you must set it for any further virtual host explicitly.
        #ServerName www.example.com
        
        WSGIDaemonProcess server name python-path=/usr/lib/python3/dist-packages (If your python path is different paths, change this value)
        WSGIProcessGroup server name
        WSGIScriptAlias / <BASE_DIR>/penetrance_platform/penetrance_platform/config/wsgi.py process-group=server name
        Alias /static <BASE_DIR>/penetrance_platform/penetrance_platform/static

        # Available loglevels: trace8, ..., trace1, debug, info, notice, warn,
        # error, crit, alert, emerg.
        # It is also possible to configure the loglevel for particular
        # modules, e.g.
        #LogLevel info ssl:warn

        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined

        # For most configuration files from conf-available/, which are
        # enabled or disabled at a global level, it is possible to
        # include a line for only one particular virtual host. For example the
        # following line enables the CGI configuration for this host only
        # after it has been globally disabled with "a2disconf".
        #Include conf-available/serve-cgi-bin.conf
    </VirtualHost>

 <BASE_DIR>는 이거 clone한 디렉토리로 하면 됩니다. server name은 아무거나 해주세요!
 <BASE_DIR> is directory which is cloned project. server name is whatever you want !
 
 그리고 apache2 서비스를 실행하고 loopback 주소의 8000번 포트로 접속하시면 됩니다. 참 쉽죠?
 And run the apache2 service and access port 8000 of the loopback address. Isn't it easy?
 
 

