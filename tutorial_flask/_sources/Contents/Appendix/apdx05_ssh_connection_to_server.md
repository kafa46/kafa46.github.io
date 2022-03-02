# 아마존 클라우드 서버에 접속하기

가장 널리 사용되는 클라우드 서버 중 하나는 아마존 클라우드 입니다. 
아마존에서 제공하는 클라우드 서버의 이름을 `Amazon EC2` 입니다.

그런데 어떻게 서버에 접속할까요?

현재 우리는 서버에 접속하려고 합니다.
서버는 우리 눈앞에 있는 것이 아닙니다. 
보이지 않는 서버를 찾아 가려면 주소가 필요합니다. 

네트워크에서 사용하는 인터넷 주소 `IP 주소`에 접속하는 것입니다.
`IP`는 컴퓨터를 찾아가는데 사용하는 주소입니다. 

`CJU 빌딩`이라는 건물이 있다고 가정해 봅니다.
만약 `CJU 빌딩`이라는 곳을 찾아가려면 주소가 필요하죠? 

컴퓨터도 마찬가지 입니다. 
특정 컴퓨터를 찾아가려고 사용하는 것이 `IP 주소` 입니다.

만약 `CJU 빌딩` 앞에 도착해서 모든 일이 해결될 수도 있습니다.
하지만 대부분의 경우는 `CJU 빌싱` 안에 있는 특정 장소를 찾아가야 할 일이 더 많겠죠?

예를 들면 5층 16번째 사무실(516호실)에 방문하거나, 지하 1층 3번째 매장에(B103호실) 방문한다거나 입니다.

컴퓨터도 마찬가지 입니다. 컴퓨터를 찾았는데 그 중에 내가 원하는 서비스에 접근하기 위한 방법이 필요하겠죠? 특정 컴퓨터 내부에서 서로 다른 서비스에 접근하기 위해 사용하는 것을 `포트(Port)` 번호라고 부릅니다.

````{admonition} 포트 번호? 가끔 헷갈리는 용어
인터넷 통신(네트워크 프로토콜)에서 사용하는 포트와 일반적으로 컴퓨터 하드웨어에서 사용하는 포트는 개념이 다릅니다. 

컴퓨터에 케이블이나 플러그를 연결하는 외부 단자를 `하드웨어 포트`라고 부릅니다. 포트가 여러 개라면 번호를 붙여줄 수 있습니다. 그 번호를 `포트 번호`라고 부릅니다. 그림 {numref}`appendix_32_hardware_ports`와 같은 것들이 대표적입니다.
```{figure}  ../../imgs/Appendix/appendix_32_hardware_ports.png
---
class: bg-primary mb-1
width: 300px
align: left
name: appendix_32_hardware_ports
---
컴퓨터 하드웨어에서 사용하는 `포트`의 예
```
반면에 통신에서 사용하는 포트 번호는 특정 네트워크 프로그램 또는 운영체제 위에서 돌아가고 있는 특정 프로세스(작동중인 프로그램)를 구별하는 논리 번호 입니다. 
네트워크에서 `포트 번호`는 눈에 보이지 않습니다. 예를 들면 다음과 같은 경우입니다.
- 포트 번호 25: 이메일 전송에 사용하는 프로토콜이 사용할 번호
- 포트 번호 80: 웹 페이지 전송에 사용할 프로토콜이 사용할 번호
````

IP 주소만 안다고 아무나 서버에 접속하면 안 되겠죠? 
그래서 서버 접속은 네트워크(인터넷)을 이용하기 때문에 보안이 필요합니다.
서버 접속 보안을 위해 주로 사용하는 방법은 아이디와 패스워드를 사용합니다.

아마존 클라우드 서버에 접속하려고 합니다.
클라우드 서버는 컴퓨팅 자원(CPU, 메모리, HDD)이 부족하거나 네트워크 트래픽이 급증하면
자동으로 컴퓨팅 자원을 증가시키게 됩니다.
이런 기능을 `Auto Scaling` (참고: [click](https://docs.aws.amazon.com/ko_kr/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html))이라고 합니다.

클라우드 서버는 사용자가 클릭 몇 번으로 원하는 서버를 쉽게 만들 수 있습니다.
하지만, 만약 내가 서버를 직접 구축했다면 서버 마음대로 CPU나 메모리가 커지거나 적어지지는 않습니다. 컴퓨팅 자원을 늘이려면 직접 구매해서 장착해야 하니까요.

하지만 클라우드 서버는 자동으로 조절되게 할 수 있습니다.
그리고 클릭 몇 번만 해주면 서버 자원 능력을 쉽게 바꿀 수 있습니다.
그러나 여러분이 서버를 직접 운영한다면 CPU나 메모리를 직접 구매해서 서버에 달아주고 드라이버 설치하는 등 다양한 일들을 해야 할 것입니다. 
직접 운영하는 서버는 클릭 몇 번에 해결되는 경우는 없다는 뜻입니다.

이러한 클라우드 서버의 장점 점은 아주 강력한 장점이기도 하지만, 반면에 치명적인 단점이 되기도 합니다.

만약 해킹이 된다면 해커가 마음대로 고사양 서버를 생성해서 마음대로 사용한다면,
상상하기 어려울만큼 엄청남 요금 폭탄을 맞을 수 있습니다.
그래서 필요한 것이 추가적인 보안 접속 방법입니다.
참고로 아마존에서는 SSH로 원격 서버에 접속할 경우에는 비밀키를 이용한 접속 방법만을 허용하고 있습니다. 

이제 본격적으로 아마존 클라우드 서버(인스턴스)에 접속해 볼까요?

Amazone EC2 콘솔에서 그림 {numref}`appendix_29_moving_to_ec2_connect_menu_1` 또는 {numref}`appendix_30_moving_to_ec2_connect_menu_2`와 같이 메뉴를 이동하여 `연결` 아이콘을 클릭합니다. 클릭하면 서버에 접속할 수 있는 방법을 안내하는 페이지로 이동합니다.

```{figure}  ../../imgs/Appendix/appendix_29_moving_to_ec2_connect_menu_1.png
---
class: bg-primary mb-1
width: 600px
align: left
name: appendix_29_moving_to_ec2_connect_menu_1
---
인스턴스(클라우드 서버) 연결 메뉴 이동 1
```
```{figure}  ../../imgs/Appendix/appendix_30_moving_to_ec2_connect_menu_2.png
---
class: bg-primary mb-1
width: 700px
align: left
name: appendix_30_moving_to_ec2_connect_menu_2
---
인스턴스(클라우드 서버) 연결 메뉴 이동 2
```

Amazon EC2 서버를 기준으로 아마존 클라우드 서버에 접속하는 방법은 4가지 정도 가능합니다.

```{figure}  ../../imgs/Appendix/appendix_31_ec2_connect_option.png
---
class: bg-primary mb-1
width: 700px
align: left
name: appendix_31_ec2_connect_option
---
인스턴스(클라우드 서버) 접속 방법
```

그림 {numref}`appendix_31_ec2_connect_option`과 같이 클라우드 서버에 접속할 수 있는 방법이 안내됩니다. 4가지 방법이 가능하다고 안내하고 있습니다. 

- `EC2 인스턴스 연결`: 웹 브라우저에서(크롬, 엣지 등) 클릭 한번으로 클라우드 서버(인스턴스)에 접속하는 방법입니다. AWS EC2 콘솔에 로그인 되어 있다면, 가장 편리한 방법입니다.
- `Session Manager`: `아마존 세션 관리자`라고도 부릅니다. 아마존의 클라우드 서버 `EC2 `(Elastic Compute 2), `온프레미스`(On-premise) 서버, `가상머신`(Virtual Machine), `엣지 디바이스`(Edge Device)를 통합관리할 수 있는 기능입니다. 참고문서 [click](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html)
    ```{admonition} 온프레미스
    클라우드와 같은 원격 환경이 아닌 자체적으로 구축한 서버를 의미합니다. 회사 또는 대학교 전산실에서 자체적으로 운영하는 서버실을 일컬을때 사용하는 단어입니다.
    ```
- `SSH 클라이언트`: 클라이언트(여러분의 컴퓨터, 혹은 서버에 접속하려는 컴퓨터)에 설치된 SSH 프로그램을 이용하여 서버에 접속하는 방법입니다. 가장 많이 사용하는 방법입니다.
    ```{admonition} SSH
    SSH(Secure SHell)은 멀리 떨어져 있는 컴퓨터에 접속하기 위한 통신 방법(프로토콜)입니다.
    사용자들이 접속할 서버에는 `SSH 서버` 프로그램이, 클라이언트(서버에 접속하려는 컴퓨터)에는 `SSH 클라이언트` 프로그램이 설치되어 있어야 합니다. SSH 프로토콜은 기본적으로 TCP 22번 포트를 사용합니다.
    ```
- `EC2 직렬 콘솔`: 클라우드 서버의 직렬 포트 (Serial Port)에 직접 연결한 것과 동일한 기능을 제공하는 접속 방식입니다. 서버의 장애 해결, 네트워크 설정 등 서버에 문제가 발생한 경우에 사용합니다. 클라우드 서버를 부팅할때 생성되는 모든 메시지를 볼 수 있습니다. 우리가 사용한 클라우드 서버(인스턴스)에는 적용할 수 없는 기능입니다. 참고문서 [click](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-serial-console.html?icmpid=docs_ec2_console)



우리는 아래 4가지 방법 중에서 [](ec2_instance_connection) 방법과 [](ssh_client_connection) 방법을 활용할 예정입니다.

서버 접속 시 사용할 암호키 파일 `.pem` 이름을 안내해 줍니다. 
제가 사용할 클라우드 서버(인스턴스)에 적용할 암호키 파일은 `hello_cju.pem`이 됩니다. 
여러분에게는 각자 지정한 `.pem` 파일 이름을 친절하게 안내해 줄 것입니다.

아래쪽에 `사용자 이름`에 `ubuntu`라고 기본(default)설정 되어 있을 겁니다.
우분투 운영체제는 수많은 리눅스의 파생형 중 하나입니다. 
세계적으로 가장 많이 사용되기 때문에 우리가 선택한 운영체제입니다.
리눅스는 기본적으로 다수 사용자가 동시에 이용하는 개념으로 설계되어 있습니다.

다수의 사용자를 구분하려면 아이디(ID)가 필요하겠죠?
우리가 만든 클라우드 서버(인스턴스)에도 리눅스 운영체제가 깔려 있을테니 당연히 접속하기 위해서는 아이디가 필요합니다. 그때 사용할 아이디 이름이 `ubuntu`라고 알려주는 것입니다.
각자 희망하는 아이디가 있다면 입력해도 됩니다. 
우리는 일단 `ubuntu`라는 이름(아이디)을 그대로 사용하겠습니다.

(ec2_instance_connection)=
## EC2 인스턴스 연결 기능 활용하기
Amazon EC2 Console에서 지원하는 기능을 이용하여 편리하게 접속하는 기능입니다.
매우 편리하고 간편한 방법입니다.
먼저 이 방법을 이용해서 접속해 보겠습니다.

```{figure}  ../../imgs/Appendix/appendix_33_ec2_option_instance_connect.png
---
class: bg-primary mb-1
width: 700px
align: left
name: appendix_33_ec2_option_instance_connect
---
`EC2 인스턴스 연결` 이용하여 연결하기 메뉴
```

그림 {numref}`appendix_33_ec2_option_instance_connect`에서 `EC2 인스턴스 연결`  클릭하고 `연결` 아이콘을 클릭합니다. 이 때 본인의 `.pem` 파일 이름, 퍼블릭 IP 주소, 아이디 등 정보를 유의깊게 살펴보세요. 

`연결`을 클릭하면 그림 {numref}`appendix_34_ec2_option_instance_connect_success`과 같은 브라우저(크롬 등) 창이 생깁니다.

```{figure}  ../../imgs/Appendix/appendix_34_ec2_option_instance_connect_success.png
---
class: bg-primary mb-1
width: 700px
align: left
name: appendix_34_ec2_option_instance_connect_success
---
`EC2 인스턴스 연결`에 성공하여 새로 나타난 브라우저 창(Window)
```


하지만 이 방법은 불편한 점이 있습니다.
시간이 지나면 보안을 위해서 자동으로 연결이 중지 됩니다.
그러면 그 동안 작업했던 내용들이 같이 중단되기도 합니다.

빈번히 접속해야 하는 경우 AWS EC2 콘솔에 매번 접속해야 하는 번거로움도 있고, 즐겨찾기를 하거나 여러 대의 서버를 등록하여 사용하기도 불편합니다.

그래서 이 방법보다는 SSH 클라이언트를 이용하는 방법을 더 자주 사용합니다.

(ssh_client_connection)=
## SSH 클라이언트 이용하여 접속하기
원격에서 고객의 요청(`request`)에 답변(`response`)을 보내주는 컴퓨터를 서버라고 합니다.
서버에 요청을 보내는 컴퓨터를 클라이언트라고 합니다.

SSH는 원격 컴퓨터에 보안이 강화된 방법으로 접속하기 위한 통신 프로토콜입니다.
SSH 통신을 위해서 서버에는 `SSH server` 프로그램이 동작하고 있어야 하고, 
클라이언트 컴퓨터에는 `SSH client` 프로그램이 동작해야 합니다.

서버 컴퓨터에서 작동하는 `SSH server`를 `SSH 데몬`(`deamon`) 이라고 부르기도 합니다.
우리가 만든 클라우드 서버에는 우분투 리눅스가 깔려 있습니다. 
리눅스 운영체계는 `openssh-server`라는 데몬이 기본적으로 설치되고, 서버를 작동시키면 자동으로 동작합니다.

만약 설치되어 있지 않다면 터미널을 열고 다음 명령어를 실행시키면 우분투 패키지 관리자 `apt`가 자동으로 설치해 줍니다.
```
sudo apt install openssh-server
```

`openssh-server`가 실행되고 있는지 확인하려면 다음과 같은 명령어를 사용합니다.
```{code} bash
sudo systemctl status sshd
```

위 명령어를 실행하면 아래와 같은 결과가 나옵니다.
```
● ssh.service - OpenBSD Secure Shell server
     Loaded: loaded (/lib/systemd/system/ssh.service; enabled; vendor preset: enabled)
    Drop-In: /usr/lib/systemd/system/ssh.service.d
             └─ec2-instance-connect.conf
     Active: active (running) since Sat 2022-02-26 01:29:32 UTC; 36s ago
       Docs: man:sshd(8)
             man:sshd_config(5)
   Main PID: 18871 (sshd)
      Tasks: 1 (limit: 1147)
     Memory: 1.0M
     CGroup: /system.slice/ssh.service
             └─18871 sshd: /usr/sbin/sshd -D -o AuthorizedKeysCommand /usr/share/ec2-instance-connect/eic_run_aut>

Feb 26 01:29:32 ip-172-31-38-113 systemd[1]: Starting OpenBSD Secure Shell server...
Feb 26 01:29:32 ip-172-31-38-113 sshd[18871]: Server listening on 0.0.0.0 port 22.
Feb 26 01:29:32 ip-172-31-38-113 sshd[18871]: Server listening on :: port 22.
Feb 26 01:29:32 ip-172-31-38-113 systemd[1]: Started OpenBSD Secure Shell server.
```

위 코드의 중간 부분에 `Active: active (running) ~ ~`라는 라인에서 `active (running)`이라는 글자가 보이면 잘 작동하고 있는 것입니다. 
만약 `inactive (dead)`라는 글자가 보이면 SSH 데몬이 죽어있는 상태입니다.
이럴 경우에는 다음 명령어를 실행시켜 SSH 데몬을 실행시킵니다.

```
sudo systemctl start sshd
```

이후에 다시 SSH 데몬 상태를 확인해 보면 됩니다.
```
sudo systemctl status sshd
```

그렇다면 서버에 접속할 클라이언트 컴퓨터(여러분의 PC)에는 무엇이 있어야 할까요?
걱정할 필요가 없습니다. 
대부분의 운영체제에는 SSH client 프로그램이 기본으로 설치되어 있습니다. 

- 윈도우라면 파워쉘(`PowerShell`) 프로그램을 실행시키고 `ssh`라고 타이핑한 다음에 엔터를 칩니다. 그러면 그림 {numref}`appendix_35_ssh_powershell`와 같은 결과가 나오면 정상입니다.
    ```{figure}  ../../imgs/Appendix/appendix_35_ssh_powershell.png
    ---
    class: bg-primary mb-1
    width: 700px
    align: left
    name: appendix_35_ssh_powershell
    ---
    윈도우 `PowerShell`에서 SSH 서버 프로그램을 실행시킨 결과
    ```

- 리눅스(우분투)의 경우 `터미널(Terminal)`을 열고 `ssh`라고 타이핑한 다음에 엔터를 칩니다.
그림 {numref}`appendix_36_ssh_ubuntu`와 같은 결과가 나오면 정상입니다.
    ```{figure}  ../../imgs/Appendix/appendix_36_ssh_ubuntu.png
    ---
    class: bg-primary mb-1
    width: 700px
    align: left
    name: appendix_36_ssh_ubuntu
    ---
    리눅스 `터미널(Terminal)`에서 SSH 서버 프로그램을 실행시킨 결과
    ```
여러분의 컴퓨터(PC)에도 전부다 SSH client 프로그램이 설치되어 있을 것입니다.

클라이언트에서 서버로 접속하기 위한 명령어는 다음과 같습니다.

```
ssh [서버에서 사용하는 아이디]@[서버 IP 주소]

# [사용 예시]
# 만약 여러분 서버의 접속 정보가 다음과 같다면,
# 공인 IP 주소: 3.352.234.111
# 아이디: ubuntu
# 명령창에 다음과 같이 ssh 명령어를 실행시킵니다.

ssh ubuntu@3.352.234.111
```

일반적인 경우 위 명령어를 실행하면 비밀번호를 입력하라는 메시지가 나오고, 
비밀번호가 맞다면 서버에 바로 접속할 수 있습니다.

하지만 아마존 클라우드 서버는 보안 강화를 위해 비밀키 `.pem` 파일을 사용해야 한다고 했죠?
위와 같은 방법으로는 `접속 거부(Permission Denied)` 메시지가 뜨면서 접속할 수 없게 됩니다.

이런 경우에는 다음과 같은 명령어를 사용하면 접속이 가능합니다.
```
ssh -i /path/my-key-pair.pem my-instance-user-name@my-instance-public-dns-name
```

또는
```
ssh -i /path/my-key-pair.pem my-instance-user-name@my-instance-public-ip-address
```

위 명령어를 입력하더라도 `private key` 파일을 입력하라, 보안이 수준이 어떻다는 등등 메시지를 계속 마주하며 해결해 나가야 합니다.

이런 명령어를 일일히 키보드로 입력하고 메시지를 확인하는 것은 매우 번거롭습니다. 
서버 접속을 편리하게 도와주는 툴(소프트웨어)이 있습니다.

대표적으로 많이 사용하는 것이 `Putty`와 `Xshell`, `mobaXterm` 등이 있습니다.
대부분 SSH 클라이언트 소프트웨어는 거기서 거기입니다. 
아무것이나 선택해서 사용하면 됩니다.
우리는 `Xshell` 프로그램을 사용해 볼 것입니다.

각 프로그램의 안내/설명은 아래 링크를 참고하세요.
- `putty`: 무료, 가볍고 간단해서 세계적으로 많이 사용 $\to$ [click](https://www.putty.org/)
- `mobaXterm`: 가정용 무료, `putty`보다 다양한 기능 $\to$ [click](https://mobaxterm.mobatek.net/)
- `Xshell`: 가정 및 학교 무료, 한국 벤처회사에서 만든 소프트웨어, 다양한 기능 지원 $\to$ [click](https://www.netsarang.com/ko/xshell/)


### SSH 클라이언트 - Xshell 설치
`Xshell`은 대한민국에서 개발한 소프트웨어로 전세계적으로도 많이 사용되고 있는 SSH 클라이언트 프로그램입니다. 우리는 Xshell을 이용해서 아마존 클라우드 서버에 접속해 보겠습니다.

먼저 Xshell 다운로드 페이지 [click](https://www.netsarang.com/ko/xshell-download/)에서  가정 및 학교 내 사용자를 위한 `무료 라이선스 페이지`를 클릭합니다. 그림 {numref}`appendix_37_xshell_free_license`를 참고하세요.

```{figure}  ../../imgs/Appendix/appendix_37_xshell_free_license.png
---
class: bg-primary mb-1
width: 700px
align: left
name: appendix_37_xshell_free_license
---
Xshell 무료 라이선스 다운로드 링크
```

그림 {numref}`appendix_38_xshell_download_field`를 참고하여 이름, 이메일, 다운로드 받고 싶은 프로그램(Xshell, Xftp, 또는 둘다)을 선택하고 다운로드 아이콘을 클릭합니다.
우리는 일단 SSH 프로그램만 필요하기 때문에 Xshell 하나만 선택하겠습니다.
여기서 입력한 이메일 주소로 다운로드 링크를 보내줍니다. 
이메일은 정확히 입력해야 합니다.

```{figure}  ../../imgs/Appendix/appendix_38_xshell_download_field.png
---
class: bg-primary mb-1
width: 700px
align: left
name: appendix_38_xshell_download_field
---
Xshell 무료 라이선스 다운로드 링크
```

입력한 이메일로 다운로드 링크를 보내줍니다.
다운로드 받은 후에 본인의 컴퓨터에 프로그램을 설치합니다.
설치 방법은 생략하겠습니다.

### Xshell 접속 설정
Xshell을 실행시키고 `파일-새로만들기` 메뉴를 실행하거나 단축아이콘을 클릭하여 세션 만들기 창을 띄웁니다. 그림 {numref}`appendix_39_xshell_id_psswd`를 참고하여 서버 `이름(N)`을 입력해 줍니다. 서버 이름은 아무거나 적어도 됩니다.

`호스트(H)`에는 여러분이 접속하려는 서버의 공인 IP 주소나 DNS 주소를 적어줍니다.
아마존 클라우드 서버는 공인 IP 주소를 적어줍니다. 클라우드 서버의 공인 IP 주소 대신에 AWS EC2 콘솔에서 확인할 수 있는 `퍼블릭 IPv4 DNS`를 적어줘도 됩니다.

그리고 `확인` 아이콘을 클릭합니다.

```{figure}  ../../imgs/Appendix/appendix_39_xshell_id_psswd.png
---
class: bg-primary mb-1
width: 700px
align: left
name: appendix_39_xshell_id_psswd
---
Xshell 무료 라이선스 다운로드 링크
```

확인을 클릭하면 화면이 사라집니다.
그림 {numref}`appendix_40_xshell_footprint`을 참고하여 조금 전에 만든 서버를 세션관리 창에서 더블클릭 합니다. 맨 처음 접속하는 서버일 경우 손도장(footprint)가 뜹니다. 손도장은 서버에서 여러분의 컴퓨터를 인식하기 위해 랜덤하게 생성해서 보내는 고유한 문자열입니다. 

`한번 수락(O)`를 클릭하면 다음에 해당 서버에 접속하려 할때 또 손도장 화면이 뜹니다. 번거로움을 방지하기 위해 `수락 및 저장(S)`를 클릭하여 저장합니다. 그림 {numref}`appendix_40_xshell_footprint`을 참고하세요.

```{figure}  ../../imgs/Appendix/appendix_40_xshell_footprint.png
---
class: bg-primary mb-1
width: 700px
align: left
name: appendix_40_xshell_footprint
---
손도장 확인, 수락 및 저장
```

Xshell 세션관리창에서 여러분이 만든 서버 이름에 마우스 오른쪽 클릭하여 등록정보를 클릭합니다. `연결` - `사용자 인증 ` 메뉴를 선택해서 사용자 이름에는 `ubuntu`를 입력하고 `방법`은 `Public Key`를 선택하고 `확인` 아이콘을 클릭합니다(만약 AWS EC2 콘솔에서 사용자 이름을 `ubuntu` 이외에 다른 이름을 지정했다면 그 이름을 입력합니다).

```{figure}  ../../imgs/Appendix/appendix_41_xshell_userName_publicKey.png
---
class: bg-primary mb-1
width: 700px
align: left
name: appendix_41_xshell_userName_publicKey
---
사용자 이름 및 Public Key 선택
```

이제는 우리가 아마존에서 받은 비밀키 `.pem` 파일을 등록할 차례입니다.
그림 {numref}`appendix_42_xshell_register_pem_file_with_passwd`참고해서 비밀키 파일을 등록합니다.


```{figure}  ../../imgs/Appendix/appendix_42_xshell_register_pem_file_with_passwd.png
---
class: bg-primary mb-1
width: 800px
align: left
name: appendix_42_xshell_register_pem_file_with_passwd
---
비밀키 `.pem` 파일 등록
```

Xshell 세션관리창에서 여러분이 만든 서버 이름을 클릭하면 `사용자 키`를 찾기위한 `찾아보기` - `사용자 키` 메뉴를 선택하면 그 다음창에서 `가져오기` 메뉴를 선택합니다.

파일탐색기 창이 뜹니다. 여러분이 저장해 놓은 비밀키 `.pem` 파일을 엽니다.

사용자키 창에 여러분의 비밀키 파일이 나타납니다.

비밀키 `.pem` 파일에 비밀번호를 부여하기 위해 등록정보를 클릭합니다.

`암호변경` 아이콘을 클릭하면 `현재 암호`, `새 암호`, `암호 확인` 입력창이 뜹니다. 현재 암호는 없으므로 빈 칸으로 두고, 새 암호와 암호 확인을 입력하고 확인을 클릭합니다.

확인을 계속 누르면 사용자 인증 창으로 돌아옵니다.
사용자 키가 등록되어 있을 겁니다. 암호 입력창에 여러분이 설정한 암호를 입력하면 아마존 클라우드 서버에 접속할 수 있습니다.

처음에 암호 등록이 복잡하긴 하지만, 한번만 해주면 다음 접속부터는 안해도 됩니다.

### Xshell로 아마존 서버 접속하기
모든 작업을 마치고 서버에 접속하면 아래 그림 {numref}`appendix_43_xshell_ec2_sucess` 같은 화면이 뜹니다.

```{figure}  ../../imgs/Appendix/appendix_43_xshell_ec2_sucess.png
---
class: bg-primary mb-1
width: 800px
align: left
name: appendix_43_xshell_ec2_sucess
---
Amazon EC2 서버에 접속한 상태
```

서버는 단순히 클라이언트의 요청을 처리하고 그 결과를 클라이언트에게 알려주는 일을 하기 때문에 MS 윈도우나 맥OS와 같이 예쁜 모양(GUI)를 제공하는 경우는 거의 없습니다. 대부분 명령어를 `콘솔(터미널)`이라고 불리는 까만 명령창을 제공합니다.

그림 {numref}`appendix_43_xshell_ec2_sucess`을 통해 서버 화면을 잠깐 감상해 볼까요?

서버 접속 화면의 맨 위에 있는 메시지는 서버 접속 전에 여러분들의 컴퓨터 위치입니다.
```
Type `help' to learn how to use Xshell prompt.
[C:\~]$ 
```
위 코드는 제 화면에 나타난 내용입니다. 
저는 `C` 드라이브의 사용자(Users) 홈 디렉토리(`~`)에 있었다는 뜻입니다.

아래 코드는 여러분이 접속한 서버는 Ubuntu 20.04.3 LTS 버전을 사용하고 있다는 의미입니다.
```
    Welcome to Ubuntu 20.04.3 LTS (GNU/Linux 5.11.0-1022-aws x86_64)
```

다음 코드는 현재 접속한 서버의 전반적인 상황을 설명하고 있습니다.
```
    System information as of Sat Feb 26 03:23:41 UTC 2022

    System load:  0.0               Processes:             113
    Usage of /:   25.0% of 7.69GB   Users logged in:       1
    Memory usage: 23%               IPv4 address for eth0: 172.31.38.113
    Swap usage:   0%
```

다음 코드는 서버에 명령을 내릴 수 있는 준비가 되어있는 명령 프롬프트 입니다.
```
ubuntu@ip-172-31-38-113:~$ 
```

각각의 의미는 다음과 같습니다.
- `ubuntu`: 서버에 접속한 아이디 입니다.
- `ip-172-31-38-113`: 아마존에서 서버에 붙여준 이름입니다.
- `~`: 홈 디렉토리에 있다는 의미입니다. 절대경로는 `/home/ubuntu/`입니다.
- `$`: 현재 일반 유저(user) 권한으로 접속해 있다는 의미입니다. 관리자 권한 (super user)으로 변경되면 `#` 표시로 바뀝니다.

앞서 간략히 설명했던 `putty`, `mobaXterm`와 같은 프로그램도 `Xshell`과 사용법이 매우 비슷합니다. 관심있는 사람들은 공부삼아 한번씩 사용해 보는 것도 좋습니다.

이제 여러분은 SSH 클라이언트의 한 종류(툴, Tool)인 `Xshell` 프로그램을 이용해 서버에 원격 접속하였습니다. 이제 마음껏 서버를 이용해서 작품을 만들면 됩니다. 

축하합니다. 짝짝짝~

## VS code를 이용하여 접속하기
`VS code`는 거의 모든 프로그래밍 언어를 이용한 개발 환경을 지원하고 있습니다.
또한 다양한 확장 프로그램(익스텐션, extension)이 지원되고 있기 때문에 전 세계적으로 가장 많이 사용되는 통합개발환경(IDE: Integrated Development Environment)입니다.

VS code를 이용해서 서버에 접속하고, 코딩을 진행하고, 터미널에서 명령을 내릴 수 있습니다.
VS code로 서버에 접속해서 코딩 하다가 터미널에 명령어를 주어야 하는 경우에 Xshell 같은 별도 프로그램을 작동시키는 것도 바쁜 개발자에게는 번거로운 일입니다.

이번에는 VS code에서 SSH client를 이용해 서버에 접속하는 방법에 대해 알아보겠습니다.

### VS code에 SSH 확장 프로그램 설치
VS code에서 SSH 프로토콜을 사용하려면 당연히 SSH client 프로그램이 있어야겠죠?
VS code로 원격 컴퓨터에 접속하기 위해서는 `Remote-SSH`라는 확장(익스텐션) 프로그램을 설치해야 합니다. 

그림 {numref}`appendix_44_vscode_remote_ssh_extension`을 먼저 살펴보세요.

```{figure}  ../../imgs/Appendix/appendix_44_vscode_remote_ssh_extension.png
---
class: bg-primary mb-1
width: 800px
align: left
name: appendix_44_vscode_remote_ssh_extension
---
VS code에 SSH 호가장 프로그램 설치
```

VS code를 실행시키고 왼쪽에 아이콘들이 세로로 쭉 줄지어 있는 것 중에서 확장 프로그램 아이콘을 클릭합니다.
`EXTENSINO: MARKETPLACE`라는 글자 밑에 검색창이 나타납니다. 
`remote-ssh`라고 검색어를 입력하면 관련된 확장 프로그램 목록이 보입니다.
우리가 필요한 SSH 프로그램은 `remote-ssh`이므로 `install` 아이콘을 클릭하여 설치를 진행합니다.

그림 {numref}`appendix_45_vscode_remote_ssh_installed`은 `Remote-SSH` 설치가 완료된 상태입니다.

```{figure}  ../../imgs/Appendix/appendix_45_vscode_remote_ssh_installed.png
---
class: bg-primary mb-1
width: 800px
align: left
name: appendix_45_vscode_remote_ssh_installed
---
VS code에 SSH 확장 프로그램 설치
```

그림 {numref}`appendix_45_vscode_remote_ssh_installed` 상태에서 `Uninstall`을 클릭하면 설치된 프로그램이 제거됩니다. `Disable` 아이콘을 클릭하면 삭제되지는 않지만 기능이 중단됩니다. `Switch to Pre-Release Version`을 선택하면 이전 버전의 프로그램으로 버전이 변경됩니다.
우리는 별도로 손댈 일은 없습니다. 

아래쪽에 설치한 프로그램에 대한 소개와 튜토리얼이 제공됩니다.

### VS code에 SSH 접속 설정하기

VS code에 SSH 확장 프로그램 (익스텐션) `Remote-SSH` 설치 완료가 되었다면, 
우리가 접속할 서버의 정보를 입력해 주어야 합니다. 

먼저 그림 {numref}`appendix_46_vscode_remote_config_setting`를 살펴보세요.

```{figure}  ../../imgs/Appendix/appendix_46_vscode_remote_config_setting.png
---
class: bg-primary mb-1
width: 800px
align: left
name: appendix_46_vscode_remote_config_setting
---
VS code에 SSH 설정(config) 파일 작성
```

차근차근 설명해 보겠습니다.

그림 {numref}`appendix_46_vscode_remote_config_setting` 참고하면서 따라해 보세요.

먼저 `Remote-SSH` 설치 성공했다면, VS code 왼쪽에 아이콘이 세로로 모여있는 곳에서 원격접속 아이콘을 클릭합니다. 

`SSH TARGETS`라는 창이 생깁니다. 
이전에 등록해 놓은 원격 컴퓨터가 있다면 목록이 나타납니다.
처음으로 원격지 컴퓨터(서버)를 등록하는 경우라면 아무것도 없습니다.

톱니바퀴 모양 아이콘을 클릭합니다.
SSH 설정파일 작성이 가능한 목록이 보입니다.
대부분 MS 윈도우 운영체제일 경우 대부분 `C:\Users\본인아이디\.ssh\config`라는 목록이 있을 겁니다. 본인의 컴퓨터가 리눅스 또는 맥OS일 경우는 설정파일(`config`) 파일이 있는 위치가 자동으로 나타납니다. 우리는 `C:\Users\본인아이디\.ssh\config` 선택합니다.

설정파일을 편집할 수 있는 창이 생성됩니다.
서버 접속에 필요한 기본적인 것은 서버의 IP 주소, 사용자 아이디, 포트 번호 입니다.
다음과 같이 입력합니다. 
`IdentityFile`는 `.pem` 파일을 저장해 놓은 디렉토리 경로를 의미합니다.
아래 예시는 MS 윈도우 경로 기준으로 작성된 예시 입니다.

```
Host [원격 컴퓨터에 붙여줄 이름]
    HostName [원격 컴퓨터의 IP 주소]
    User [원격 컴퓨터에서 사용할 아이디]
    Port 22 [접속 포트]
    IdentityFile "[여러분의 .pem 파일이 있는 경로]\[.pem 파일명]"
```

감이 안 잡히면 그림 {numref}`appendix_46_vscode_remote_config_setting` 참고하세요.

위 내용을 입력하고 저장합니다.
그리고 새로 생성한 리모트 서버에 접속합니다.

하지만 아래와 같은 무시무시한 에러가 날 수 있습니다. ㅠㅠ
```
[16:51:51.096] Log Level: 2
[16:51:51.097] remote-ssh@0.74.0
[16:51:51.097] win32 x64
[16:51:51.101] SSH Resolver called for "ssh-remote+7b22686f73744e616d65223a224157535f68656c6c6f5f636a75227d", attempt 1
[16:51:51.102] "remote.SSH.useLocalServer": false
[16:51:51.102] "remote.SSH.showLoginTerminal": false
[16:51:51.102] "remote.SSH.remotePlatform": {"DeepLearning":"linux","ACIN_GPU_server":"linux","AIHC_GPU_server":"linux","AWS_hello_cju":"linux"}
[16:51:51.102] "remote.SSH.path": undefined
[16:51:51.102] "remote.SSH.configFile": undefined
[16:51:51.102] "remote.SSH.useFlock": true
[16:51:51.103] "remote.SSH.lockfilesInTmp": false
[16:51:51.103] "remote.SSH.localServerDownload": auto
[16:51:51.103] "remote.SSH.remoteServerListenOnSocket": false
[16:51:51.103] "remote.SSH.showLoginTerminal": false
[16:51:51.103] "remote.SSH.defaultExtensions": []
[16:51:51.103] "remote.SSH.loglevel": 2
[16:51:51.103] "remote.SSH.enableDynamicForwarding": true
[16:51:51.103] "remote.SSH.enableRemoteCommand": false
[16:51:51.104] "remote.SSH.serverPickPortsFromRange": {}
[16:51:51.104] "remote.SSH.serverInstallPath": {}
[16:51:51.120] SSH Resolver called for host: AWS_hello_cju
[16:51:51.120] Setting up SSH remote "AWS_hello_cju"
[16:51:51.142] Using commit id "f80445acd5a3dadef24aa209168452a3d97cc326" and quality "stable" for server
[16:51:51.148] Install and start server if needed
[16:51:51.151] Checking ssh with "ssh -V"
[16:51:51.190] > OpenSSH_for_Windows_8
[16:51:51.190] > .1p1, LibreSSL 3.0.2

[16:51:51.195] Running script with connection command: ssh -T -D 64713 "AWS_hello_cju" bash
[16:51:51.197] Terminal shell path: C:\Windows\System32\cmd.exe
[16:51:51.432] > ]0;C:\Windows\System32\cmd.exe
[16:51:51.432] Got some output, clearing connection timeout
[16:51:51.450] > C:\\Users\\cju/.ssh/config: line 32: Bad configuration option: `    
> C:\\Users\\cju/.ssh/config: terminating, 1 bad configuration options
> 프로세스에서 없는 파이프에 쓰려고 했습니다.
> 
[16:51:52.720] "install" terminal command done
[16:51:52.721] Install terminal quit with output: 프로세스에서 없는 파이프에 쓰려고 했습니다.
[16:51:52.721] Received install output: 프로세스에서 없는 파이프에 쓰려고 했습니다.
[16:51:52.722] Failed to parse remote port from server output
[16:51:52.723] Resolver error: Error: 
	at Function.Create (c:\Users\cju\.vscode\extensions\ms-vscode-remote.remote-ssh-0.74.0\out\extension.js:1:585917)
	at Object.t.handleInstallOutput (c:\Users\cju\.vscode\extensions\ms-vscode-remote.remote-ssh-0.74.0\out\extension.js:1:584569)
	at Object.t.tryInstall (c:\Users\cju\.vscode\extensions\ms-vscode-remote.remote-ssh-0.74.0\out\extension.js:1:680558)
	at processTicksAndRejections (internal/process/task_queues.js:93:5)
	at async c:\Users\cju\.vscode\extensions\ms-vscode-remote.remote-ssh-0.74.0\out\extension.js:1:643417
	at async Object.t.withShowDetailsEvent (c:\Users\cju\.vscode\extensions\ms-vscode-remote.remote-ssh-0.74.0\out\extension.js:1:646762)
	at async Object.t.resolve (c:\Users\cju\.vscode\extensions\ms-vscode-remote.remote-ssh-0.74.0\out\extension.js:1:644496)
	at async c:\Users\cju\.vscode\extensions\ms-vscode-remote.remote-ssh-0.74.0\out\extension.js:1:721503
[16:51:52.729] ------
```

위와 같은 문제(서버 접속 실)는 접속 에러 내용을 읽다 보면 `> C:\Users\cju/.ssh/config: terminating, 1 bad configuration options 프로세스에서 없는 파이프에 쓰려고 했습니다.` 라는 메시지가 원인이라는 것을 알 수 있습니다.

비밀키 `.pem` 파일은 다른 프로세스(실행중인 프로그램)이나 다른 사용자와 동시에 공유되어서는 안됩니다.

다른 프로그램에서 공유키 `.pem` 파일을 사용하고 있거나, 공유 폴더로 지정된 경우가 있는지 확인합니다. 공유키 `.pem` 파일의 공유를 중지하는 방법은 그림 {numref}`appendix_47_vscode_stop_share_folder` 참고하세요.

```{figure}  ../../imgs/Appendix/appendix_47_vscode_stop_share_folder.png
---
class: bg-primary mb-1
width: 800px
align: left
name: appendix_47_vscode_stop_share_folder
---
VS code에 SSH 설정(config) 파일 작성
```

서버에 정상적으로 접속하면 그림 {numref}`appendix_48_vscode_open_folder`와 같이 서버의 폴더(디렉토리)를 선택하여 열 수 있습니다. 

먼저 `폴더 열기` 또는 `Open Folder` 메뉴를 선택하면 중앙 상단에 접속한 서버의 기본(default) 위치가 나타납니다. 일반적으로 `/home/사용자아이디` 위치 입니다. 아마존 클라우드 리눅스 서버인 경우 기본 시작 위치는 `/home/ubuntu/` 입니다. 

마우스 클릭을 통해 본인이 원하는 폴더를 선택하고 `OK`를 클릭합니다. 이때 처음 접속하는 폴더일 경우 `Do you trust the authors of the files in this folder?`라고 묻는 창이 나타납니다. 폴더를 사용해야 하니 `Yes, I trust the authors`를 클릭합니다. 다음 접속부터 이 메시지를 생략하려면 체크 박스에 체크해 줍니다.

```{figure}  ../../imgs/Appendix/appendix_48_vscode_open_folder.png
---
class: bg-primary mb-1
width: 800px
align: left
name: appendix_48_vscode_open_folder
---
접속한 서버에서 원하는 작업 디렉토리 선택 및 이동
```

원하는 디렉토리를 선택해서 접속에 성공하면 그림 {numref}`appendix_49_vscode_open_folder_after` 같은 화면이 될 것입니다.
왼쪽에는 파일 탐색기 창이 보입니다. 우리가 윈도우에서 사용하는 파일 탐색기와 동일한 기능을 제공합니다.
오른쪽 상단은 파일을 열거나 새로 만들면 해당 파일 내용을 볼 수 있는 편집기 창 공간입니다.
오른쪽 하단의 그림은 접속한 서버의 터미널 입니다.
Xshell과 같은 SSH client 프로그램을 별도로 이용하지 않더라도 VS code에서 직접 명령어를 사용할 수 있습니다.

```{figure}  ../../imgs/Appendix/appendix_49_vscode_open_folder_after.png
---
class: bg-primary mb-1
width: 800px
align: left
name: appendix_49_vscode_open_folder_after
---
접속한 서버의 디렉토리에 최종적으로 들어간 상황
```

이제 VS code를 이용하여 SSH 접속하는 방법을 모두 마쳤습니다.
서버에 접속하여 편리한 환경에서 개발할 수 있게 되었습니다.

축하드립니다 .^^.