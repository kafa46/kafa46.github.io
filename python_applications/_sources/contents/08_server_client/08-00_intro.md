
(08-00)=
# 인터넷과 파이썬

인터넷은 전 세계적으로 연결된 컴퓨터 네트워크의 집합체로, 수많은 정보와 서비스를 공유하고 접근할 수 있도록 하는 거대한 정보 통신망입니다.
인터넷의 역사는 1960년대 미국 국방부의 연구 프로젝트인 ARPANET에서 시작되었습니다.
이 프로젝트는 다양한 컴퓨터 시스템 간의 신뢰할 수 있는 통신 방법을 개발하는 것을 목표로 했습니다.
ARPANET의 성공을 바탕으로, 인터넷은 점차 확장되었고, 오늘날의 글로벌 네트워크로 성장하게 되었습니다.

인터넷은 겁나게 큰 컴퓨터 네트워크라고 생각하면 쉽습니다.

우리는 이번 장에서 `파이썬`을 활용해 인터넷(`HTTP 기반 웹서비스`)을 사용하는 방법에 대해 공부할 것입니다.

```{figure} ../imgs/chap_08/ch08_00_01_python_requests.webp
---
width: 70%
name: ch08_00_01_python_requests
---
파이썬을 이용해 다양한 인터넷 서비스를 구현할 수 있습니다.
```

본격적인 학습에 앞서 인터넷의 (1) 구성 요소 및 (2) 작동 원리에 대해 간단히 소개하겠습니다.

사실 인터넷에 대한 자세한 내용을 학습하려면 대학교 1학기 정도 수업을 들어야 하지만, 인터넷에 대한 깊은 이해는 이 책의 범위를 벋어나기 때문에 아주 간략하게 소개하겠습니다.

**인터넷의 주요 구성 요소**

인터넷은 하드웨어, 프로토콜, 서비스로 구성됩니다.

**하드웨어**

- 인터넷의 기본 구성 요소는 라우터, 스위치, 서버, 컴퓨터 및 기타 네트워크 장비입니다.
    - 대부분 가정에서는 인터넷 공유기와 공유기에 연결된 컴퓨터의 랜카드가 바로 네트워크 장비입니다.
- 장비들은 물리적으로 연결되어 데이터를 주고받습니다.
    - 가정집 어딘가 설치되어 있는 통신사(KT, SKT, LG U+ 등)의 인터넷 장비와 랜선으로 연결되어 있는 상황으로 이해하면 쉽습니다.
- 데이터는 광섬유 케이블, 위성, 무선 네트워크 등을 통해 전송됩니다.
    - 무언가를 연결하는 매체를 영어로 `미디엄(medium)`이라고 합니다. 여러 개(복수)를 뜻하는 경우 `미디어(media)`라고 부릅니다.
    - 인터넷의 구성 요소를 연결하는 미디어(media)는 랜 케이블, 무선, 광케이블 등이 사용됩니다.

**프로토콜**

어떤 일을 할 때 정해진 규칙을 `프로토콜(protocol)`이라고 합니다.

예를 들어 대통령이 외국 손님을 맞이하는 절차를 정해 놓은 것을 `의전 프로토콜` 이라고 합니다.

콘서트를 전문으로 진행해 주는 회사가 있다면, 그 회사는 `콘서트 진행 프로토콜`을 가지고 있을 것입니다.

인터넷도 프로토콜이 있습니다. 먼저 보내는 객체와 받는 객체 사이에 미리 규칙을 정해 놓아야 합니다. 그 약속에 따라 데이터를 주고 받아야 서로간에 해석이 되는건 너무나 당연하겠죠? 인터넷은 다양한 통신 프로토콜을 사용하여 데이터를 전송합니다.

가장 중요한 프로토콜은 TCP/IP(Transmission Control Protocol/Internet Protocol)입니다.
- `TCP/IP`는 데이터 패킷의 전송과 라우팅을 관리하는 표준 프로토콜입니다.
- `HTTP`(HyperText Transfer Protocol)는 웹 페이지를 요청하고 전달하는 데 사용되는 프로토콜입니다.

**서비스**

인터넷은 다양한 서비스를 제공합니다.
가장 대표적인 서비스는 웹 서비스로, 월드 와이드 웹(`WWW`)을 통해 웹사이트와 웹 애플리케이션을 사용할 수 있습니다.
이메일, 파일 전송, 온라인 채팅, 스트리밍 미디어, 소셜 네트워크 서비스 등도 인터넷을 통해 제공되는 주요 서비스입니다.

**인터넷의 작동 원리**

**데이터 전송**

인터넷에서 데이터는 작은 패킷으로 나누어 전송됩니다.
각 패킷은 목적지 주소를 포함하고 있으며, 여러 경로를 통해 목적지로 전달됩니다.
라우터는 데이터 패킷을 최적의 경로로 전달하는 역할을 합니다.
패킷은 목적지에 도착한 후 다시 원래의 데이터로 조립됩니다.

**도메인 네임 시스템(DNS)**

`DNS`는 사람이 읽을 수 있는 도메인 이름을 IP 주소로 변환하는 역할을 합니다.
예를 들어, 사용자가 웹 브라우저에 "`www.example.com`"을 입력하면,
`DNS`는 이를 해당 IP 주소로 변환하여 서버에 요청을 보냅니다.

**클라이언트-서버 모델**

인터넷 서비스는 대부분 클라이언트-서버 모델을 기반으로 작동합니다.
클라이언트는 서비스를 요청하는 사용자 장치이며, 서버는 요청을 처리하여 응답을 반환하는 컴퓨터 시스템입니다.
예를 들어, 사용자가 웹 페이지를 요청하면, 웹 서버는 요청된 페이지를 클라이언트에 전달합니다.

```{figure} ../imgs/chap_08/ch08_00_02_internet_intro.webp
---
width: 70%
name: ch08_00_02_internet_intro
---
인터넷 서비스는 대부분 서버-클라이언트 기반 구조에서 HTTP 프로토콜을 이용해 제공됩니다.
```

이제부터 파이썬을 이용해 인터넷을 사용하는 방법에 대한 학습을 시작하겠습니다.

[맨 위로 이동](08-00)