# AWS 회원가입 및 MFA 설정

아마존 AWS에서 제공하는 클라우드 서버를 이용하기 위해서는 먼저 회원가입을 해야 합니다.
회원가입 주소는 AWS EC2 페이지 ([click](https://aws.amazon.com/ko/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Categories=categories%23compute&trk=ps_a134p000006gGh2AAE&trkCampaign=acq_paid_search_brand&sc_channel=PS&sc_campaign=acquisition_KR&sc_publisher=Google&sc_category=Cloud%20Computing&sc_country=KR&sc_geo=APAC&sc_outcome=acq&sc_detail=amazon%20ec2&sc_content=EC2_e&sc_matchtype=e&sc_segment=477203497843&sc_medium=ACQ-P|PS-GO|Brand|Desktop|SU|Cloud%20Computing|EC2|KR|EN|Text&s_kwcid=AL!4422!3!477203497843!e!!g!!amazon%20ec2&ef_id=EAIaIQobChMIhu2Chu6P9gIVa9dMAh3evQ6FEAAYASAAEgId0PD_BwE:G:s&s_kwcid=AL!4422!3!477203497843!e!!g!!amazon%20ec2&awsf.Free%20Tier%20Types=*all))에서 무료 계정 생성을 클릭해서 들어가면 됩니다.

(my-label)=
```{admonition} Amazon EC2
---
name: amazon_ec2_short_explanation
---
Amazon 클라우드에서 제공하는 컴퓨팅 인스턴스 서비스의 이름입니다. EC는 `Elastic Computing`의 약자로 CPU, HDD, 메모리와 같은 컴퓨팅 자원을 조정 가능한 클라우드 서버를 의미합니다.
```

곧바로 회원가입 페이지로 가고 싶다면 여기를 [click](https://portal.aws.amazon.com/billing/signup?refid=ps_a134p000006ggh2aae&trkcampaign=acq_paid_search_brand&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation&language=ko_kr#/start)하기 바랍니다.

```{figure} ../../imgs/Appendix/appendix_01_aws_sign_up_page1.png
---
class: bg-primary mb-1
width: 400px
align: left
name: appendix_01_aws_sign_up_page1
---
AWS EC2 회원가입 화면 1
```

그림 {numref}`appendix_01_aws_sign_up_page1`에 필요한 정보를 입력하고 `계속`을 클릭합니다.

```{figure} ../../imgs/Appendix/appendix_01_aws_sign_up_page2.png
---
class: bg-primary mb-1
width: 400px
align: left
name: appendix_01_aws_sign_up_page2
---
AWS EC2 회원가입 화면 2
```

회원가입에 필요한 정보를 입력하면 요금을 결재할 신용카드 정보를 입력하는 화면으로 이동합니다.

```{figure} ../../imgs/Appendix/appendix_01_aws_sign_up_page3_credit_card.png
---
class: bg-primary mb-1
width: 400px
align: left
name: appendix_01_aws_sign_up_page3_credit_card
---
AWS EC2 회원가입 화면 3 - 결재정보 입력
```

그림 {numref}`appendix_01_aws_sign_up_page3_credit_card`과 같이결재 정보를 입력하면 회원가입이 끝나면 아마존 클라우드에서 사용할 서버를 선택하는 창이 나옵니다.

```{figure} ../../imgs/Appendix/appendix_01_aws_sign_up_page4_payment_plan.png
---
class: bg-primary mb-1
width: 700px
align: left
name: appendix_01_aws_sign_up_page4_payment_plan
---
AWS EC2 클라우스 서버 선택
```

월 750시간을 무료로 사용할 수 있는 `프리티어 Amazon EC2 750시간` 플랜을 선택합니다.
한달을 31일로 가정하고 매일 서버를 작동시켜도 `31일 $\times$ 24 시간 = 744 시간` 이므로 750시간이면 공짜로 사용할 수 있는 옵션입니다. 

```{note}
 `프리티어 Amazon EC2 750시간` 플랜은 무료이지만 아마존에서 기본으로 제공하는 CPU, HDD 등의 자원을 초과해서 사용하면 요금이 부과됩니다. 또한, 무료 기간은 1년입니다. 1년이 지나면 자동으로 월정액이 여러분이 등록한 신용카드로 청구됩니다.
```

여기까지 하면 일단 회원가입이 완료됩니다.

하지만, 클라우드 서버는 해킹 당할 경우 수천만원 이상의 요금이 부과될 수 있습니다. 클라우드 서버는 비트코인 채굴 등과 같이 많은 컴퓨팅이 필요한 해커들의 먹잇감이 될 수 있습니다. 

네트워크 트래픽이 증가하거나 정해진 컴퓨팅 자원 이상을 사용하면 자동으로 서버 성능이 증가되기 때문에 엄청난 요금이 부과될 수 있습니다. 관리자 권한을 탈취당하면 고사양 클라우드 서버로 변경 후 돌리는 경우도 발생할 수 있습니다.

Amazon EC2는 이런 경우를 대비하기 위해 여러가지 보안 강화 기능을 추가로 제공하고 있습니다. 아이디/패스워드만으로 클라우드 서버 관리자 권한에 접속하는 것은 너무나도 위험합니다. 반드시 `추가 보안 옵션`을 사용하기 바랍니다.

우리는 MFA(Multi Factor Authentication) 방식을 사용하도록 하겠습니다.

아래에 별도의 절을 편성하여 설명하겠습니다.

## MFA 활용

클라우드 서버는 기본적으로 원격 접속을 통해 모든 일이 처리됩니다.
인터넷을 통해 다양한 서버의 설정, 작동에 대한 명령이 전달됩니다.
자연스럽게 보안에 취약합니다. 아이디/비밀번호, 캡차(CAPTCHA) 만으로는 안전하지 않습니다.

아마존은 보안을 강화하기 위해 `MFA` (Multi-factor Authentication)을 지원합니다. 우리나라 말로는 `다중 인증`이라고 번역하지만, 대부분은 영어 그대로 `멀티팩터 인증`이라고 부릅니다.

MFA는 다양한 방식으로 구현할 수 있습니다. 문자를 보내기도 하고, 여러분이 사전에 등록해 놓은 사전 지식을 묻기도 합니다. 우리가 사용할 MFA 방식은 은행에서 흔히 사용하는 OTP(One Time Password)와 동일한 방식입니다. 

```{figure} ../../imgs/Appendix/appendix_02_OTP_devices.png
---
class: bg-primary mb-1
width: 700px
align: left
name: appendix_02_OTP_devices
---
다양한 OTP 디바이스
```

그림 {numref}`appendix_02_OTP_devices`에는 다양한 OTP 장치들의 예를 보여줍니다.
플라스틱 카드처럼 생긴 것도 있고, 작은 디지털 장비처럼 보이는 것도 있습니다.

우리는 카드나 장치와 같이 물리적으로 존재하는 것이 아니라 앱(App)을 사용해서 MFA를 적용해 볼 것입니다.

여러분이 설정한 아이디와 패스워드로 아마존 클라우드에 `Amazon EC2 Console` 접속합니다. 바로가려면 여기를 [click](https://aws.amazon.com/ko/console/) 합니다.

### MFA 메뉴 찾아가기

우선 MFA 설정 메뉴를 찾아가 보겠습니다.

그림 {numref}`appendix_04_IMA_menu`같이 Amazon EC2 Console 화면 우측 상단에서 본인 아이디를 클릭하여 메뉴를 펼친 다음 `보안 자격 증명` 메뉴를 선택합니다.

```{figure} ../../imgs/Appendix/appendix_04_IMA_menu.png
---
class: bg-primary mb-1
width: 700px
align: left
name: appendix_04_IMA_menu
---
`보안 자격 증명` 메뉴 선택
```

`보안 자격 증명` 메뉴를 선택하면 그림 {numref}`appendix_05_MFA_Activation`과 같이 `멀티 팩터 인증(MFA)` $\to$ `MFA 활성화` 하는 메뉴를 클릭합니다.


```{figure} ../../imgs/Appendix/appendix_05_MFA_Activation.png
---
class: bg-primary mb-1
width: 700px
align: left
name: appendix_05_MFA_Activation
---
`MFA 활성화` 메뉴 선택
```

`MFA 활성화` 하는 메뉴를 클릭하면 그림 {numref}`appendix_06_virtual_MFA_device_option`와 같은 화면이 나타납니다. `가상 MFA 디바이스`를 선택하고 `계속`을 클릭합니다.

```{figure} ../../imgs/Appendix/appendix_06_virtual_MFA_device_option.png
---
class: bg-primary mb-1
width: 700px
align: left
name: appendix_06_virtual_MFA_device_option
---
`가상 MFA 디바이스` 메뉴 선택
```

`가상 MFA 디바이스`를 선택하고 `계속`을 클릭하면 그림 {numref}`appendix_07_virtual_MFA_device_available_apps`와 같은 화면이 나타납니다. 

```{figure} ../../imgs/Appendix/appendix_07_virtual_MFA_device_available_apps.png
---
class: bg-primary mb-1
width: 700px
align: left
name: appendix_07_virtual_MFA_device_available_apps
---
`가상 MFA 디바이스 설정` 화면
```

소프트웨어(앱)을 이용해 일회용 비밀전호(OTP, One Time Passward)를 생성하는 방법은 다양합니다. 그 중에서 아무거나 한가지를 선택해서 사용하면 됩니다.

가능한 앱 목록을 확인하기 위해 그림 {numref}`appendix_07_virtual_MFA_device_available_apps`에 표시된 `호환 애플리케이션 목록`을 클릭해 봅니다. 해당 링크를 클릭하면 다양한 정보를 제공하는 웹페이지 ([click](https://aws.amazon.com/ko/iam/features/mfa/))를 확인할 수 있습니다. 

[웹 페이지](https://aws.amazon.com/ko/iam/features/mfa/) 중간 스크롤 다운 하다보면 그림 {numref}`appendix_08_virtual_MFA_device_available_apps_list`와 같은 목록을 확인할 수 있습니다.

```{figure} ../../imgs/Appendix/appendix_08_virtual_MFA_device_available_apps_list.png
---
class: bg-primary mb-1
width: 700px
align: left
name: appendix_08_virtual_MFA_device_available_apps_list
---
`가상 MFA 디바이스` 앱 목록
```

`Android`와 `iPhone`에 따라 각각 사용 가능한 앱 목록이 보입니다.
본인의 컴퓨팅 디바이스에 따라 마음에 드는 것을 선택하여 사용하면 됩니다.
우리는 가장 먼저 소개된 [Authy](https://play.google.com/store/apps/details?id=com.authy.authy)를 사용하여 우리의 아마존 클라우드 서버에 MFA를 적용하겠습니다.

### OPT 프로그램 `Authy` 설치

`Authy`는 모든 스마트폰에 설치할 수 있고, PC 환경에도 설치할 수 있어 매우 편리합니다. 다운로드 페이지는 다음 링크를 클릭해서 확인하세요.
- Android 앱 설치: Google Play $\to$ [click](https://play.google.com/store/apps/details?id=com.authy.authy)
- iPhone 앱 설치: App Store $\to$ [click](https://apps.apple.com/us/app/authy/id494168017)
- 데스크톱 설치(애플 계열 포함): Authy 다운로드 페이지$\to$ [click](https://authy.com/download/)

저는 데스크탑 설치를 기준으로 진행해 보겠습니다. 스마트폰 앱 설치는 여러분들이 저보다 훨씬 더 잘 알테니 생략하겠습니다.

Authy 다운로드 페이지 ([click](https://authy.com/download/))로 들어가면 화면 아래쪽에 그림 {numref}`appendix_03_Authy_download`와 같은 선택 메뉴가 있습니다. 본인의 Desktop(PC) 운영체제를 선택해서 다운로드 다운로드 하고 설치합니다..

```{figure} ../../imgs/Appendix/appendix_03_Authy_download.png
---
class: bg-primary mb-1
width: 700px
align: left
name: appendix_03_Authy_download
---
`가상 MFA 디바이스` 앱 목록
```

Authy 설치가 끝나면 실행시키고 계정설정(이메일)을 하고 휴대폰 인증을 받습니다.

Authy의 모든 설정이 끝났습니다. 이제 Authy를 이용해서 아마존 MFA를 최종 설정하도록 하겠습니다.

### Authy를 이용해서 MFA 설정 마무리

그림 {numref}`appendix_07_virtual_MFA_device_available_apps`에서 호환 앱 목록을 확인하고 설치를 마쳤습니다.

이제 우리가 설치한 앱 `Authy`를 이용해서 MFA 설정을 마무리하면 되겠죠?

설정 순서는 그림 {numref}`appendix_11_virtual_MFA_overall_procedure`를 참고하여 차근차근 진행하면 쉽게 할 수 있습니다.
어렵지 않아요. 먼저 그림을 휙~ 둘러보고 아래에 제시된 설치 순서대로 설정합니다.

```{figure}  ../../imgs/Appendix/appendix_11_virtual_MFA_overall_procedure.png
---
class: bg-primary mb-1
width: 700px
align: left
name: appendix_11_virtual_MFA_overall_procedure
---
Authy를 이용해서 MFA 설정하는 순서
```

````{admonition} MFA 설정 순서
1. 설치한 Authy를 실행합니다.
2. 오른쪽 위에 있는 더하기 `+` 아이콘을 클릭합니다. 그림 {numref}`appendix_12_authy_enter_code_by_website`와 같은 화면이 뜹니다. `Enter Code given by the website`라는 입력창에 아마존 MFA에서 생성한 코드를 입력해야 합니다.
    ```{figure}  ../../imgs/Appendix/appendix_12_authy_enter_code_by_website.png
    ---
    class: bg-primary mb-1
    width: 200px
    align: left
    name: appendix_12_authy_enter_code_by_website
    ---
    일회용 비밀번호(OTP)를 사용할 웹사이트(아마존 서버)에서 발행한 코드를 입력하기 위한 Authy 입력창
    ```
3. 가상 MFA 디바이스 환경에서 `QR 코드 표시` 바로 아래에 `비밀키 표시`라는 링크가 있습니다. 링크를 클릭합니다. 그러면 그림 {numref}`appendix_13_MFA_secret_key`와 같이 비밀키를 볼 수 있습니다. 이 `비밀키`는 `절대 공개되면 안됩니다`. 해킹이나 유츌 되었다면 처음부터 MFA를 다시 설정하기 바랍니다. 비밀키를 복사해서(`CTL+C`) 그림 {numref}`appendix_12_authy_enter_code_by_website`에 있는 비밀키 입력창에 붙여넣기(`CTL+V`) 합니다.
    ```{figure}  ../../imgs/Appendix/appendix_13_MFA_secret_key.png
    ---
    class: bg-primary mb-1
    width: 700px
    align: left
    name: appendix_13_MFA_secret_key
    ---
    아마존 클라우드 서버에서 발행한 비밀키 확인
    ```
4. 그림 {numref}`appendix_12_authy_enter_code_by_website`에 비밀키를 붙여넣고 `Add Account`(계정 추가)를 클릭하면 그림 {numref}`appendix_14_authy_accountName_Logo`와 같은 화면이 나옵니다.
    ```{figure}  ../../imgs/Appendix/appendix_14_authy_accountName_Logo.png
    ---
    class: bg-primary mb-1
    width: 200px
    align: left
    name: appendix_14_authy_accountName_Logo
    ---
    아마존 MFA에서 사용할 OTP 이름 설정 및 로고 선택
    ```
5. 아마존 클라우드 서버에서 사용할 OTP 이름을 입력합니다. Authy는 아마존 이외의 다른 사이트에서도 사용할 수 있으므로 구분하기 위한 별명을 지어주는 것입니다. 아무 이름이나 써도 됩니다. 저는 `Amazon EC2`라고 지어 주었습니다. 로고는 마음에 드는 색깔이 있는 아이콘 아무거나 선택합니다. 저는 노란색(Orange)`을 선택하였습니다. 저장하기 아이콘을 누릅니다.
6. `5`번 과정을 마치면 그림 {numref}`appendix_15_authy_account_click`와 같은 화면이 나옵니다. 여러분이 지정한 아이디 이름과 색상이 반영된 목록이 나옵니다. OTP 생성을 위해 여러개를 만든다면 다수의 목록이 나타날 수 있습니다. 우리는 하나만 만들었으니 하나만 나타납니다. 저는 노란(Orange)색 `Amazon EC2`라고 나왔습니다. 아이콘을 클릭합니다.
    ```{figure}  ../../imgs/Appendix/appendix_15_authy_account_click.png
    ---
    class: bg-primary mb-1
    width: 200px
    align: left
    name: appendix_15_authy_account_click
    ---
    OTP 이름/로고 확인 $\to$ 클릭
    ```
7.  그림 {numref}`appendix_07_virtual_MFA_device_available_apps`에서 MFA 코드를 2개 입력하는 창이 있었죠? 여기에 Authy에서 생성하는 OTP를 입력하면 됩니다. Authy는 30초에 한번씩 OTP가 갱신됩니다. 먼저 하나를 복사하여 붙여넣고 기다리면 다른 번호가 생성됩니다. 다음 OTP 번호를 두 번째 MFA 입력창에 붙여넣습니다.
그림 {numref}`appendix_16_enter_OTP_code`을 참고하세요.
    ```{figure}  ../../imgs/Appendix/appendix_16_enter_OTP_code.png
    ---
    class: bg-primary mb-1
    width: 700px
    align: left
    name: appendix_16_enter_OTP_code
    ---
    Authy에서 생성한 OTP 코드를 MFA 활성화를 위해 입력
    ```
8. Authy에서 생성된 2개의 OTP를 차례로 입력했다면 `MFA 할당` 아이콘을 클릭합니다.
````

MFA 할당을 마치면 그림 {numref}`appendix_17_virtual_MFA_allocation_success`와 같은 메시지가 나타나면 성공한 것입니다. 

```{figure}  ../../imgs/Appendix/appendix_17_virtual_MFA_allocation_success.png
---
class: bg-primary mb-1
width: 600px
align: left
name: appendix_17_virtual_MFA_allocation_success
---
MFA 할당 성공 메시지
```

그림 {numref}`appendix_17_virtual_MFA_allocation_success`에서 `닫기` 아이콘을 클릭합니다. 그러면 그림 {numref}`appendix_18_MFA_setting_completion`와 같은 화면이 나옵니다. 이 화면이 나오면 모든 MFA 설정이 완성된 것입니다.

```{figure}  ../../imgs/Appendix/appendix_18_MFA_setting_completion.png
---
class: bg-primary mb-1
width: 600px
align: left
name: appendix_18_MFA_setting_completion
---
MFA 설정이 모두 마무리된 상태
```

### MFA를 이용해 아마존 클라우드 서버에 접속하기

MFA 설정이 완료되었습니다.

아마존 서버에서 로그아웃합니다.

이후 아마존 클라우드 서버 접속 과정은 그림 {numref}`appendix_19_log_in_using_MFA`와 같습니다. 비밀번호 입력 $\to$ 보안검사(캡차) $\to$ MFA 코드 (Authy OTP 번호 입력) 순서입니다.

```{figure}  ../../imgs/Appendix/appendix_19_log_in_using_MFA.png
---
class: bg-primary mb-1
width: 700px
align: left
name: appendix_19_log_in_using_MFA
---
MFA 단계가 적용된 아마존 클라우드 서버 접속 순서
```

처음 해보면 좀 복잡해 보이죠? 하지만 몇번 하다보면 그리 복잡하지 않습니다. 일반적인 웹사이트 로그인할때 아이디/비번 입력하는 것에 OTP 번호 한번 더 입력하는 과정이 추가된 것입니다.

앞서도 언급했지만 클라우드 서비스에서는 보안이 `매우`, `굉장히`, `아주 많이`, `겁나게` 중요합니다. 

약간 복잡한 설정이지만 여러분들은 반드시 다단계 `MFA` 인증 과정을 추가하여 클라우드 서버를 운영하시기 바랍니다.