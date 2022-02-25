# 아마존 EC2 서버 만들기
`Amazon EC2 Console`에 회원가입을 마무리 하셨겠죠?
혹시 아직 회원가입이 안 되어 있다면 [Appendix List](../Appendix/apdx00_appendix_list.md)에 정리된 [](../Appendix/apdx03_aws_sing_up.md)를 참고하여 회원가입을 완료하기 바랍니다.

이제 본격적으로 클라우드 서버를 만들어 보겠습니다.

`Amazon EC2 Console`에 로그인 하고 서비스 콘솔 홈에서 `서비스` $\to$ `컴퓨팅`  $\to$ `EC2`를 차례로 클릭합니다. 그림 {numref}`appendix_20_ec2_select_menu`를 참고하세요.

```{figure}  ../../imgs/Appendix/appendix_20_ec2_select_menu.png
---
class: bg-primary mb-1
width: 700px
align: left
name: appendix_20_ec2_select_menu
---
클라우드 서버 생성을 위한 메뉴 선택
```

그림 {numref}`appendix_20_ec2_select_menu`에서 `EC2` 링크를 클릭하면 나오는 화면에서 다음 순서와 같이 그림 {numref}`appendix_20_ec2_select_menu`와 를 참고해서 우리가 원하는 서버를 선택합니다.

```{figure}  ../../imgs/Appendix/appendix_21_ec2_select_instance.png
---
class: bg-primary mb-1
width: 700px
align: left
name: appendix_21_ec2_select_instance
---
클라우드 서버 생성을 위한 메뉴 선택
```

```{admonition} 클라우드 서버(컴퓨터) 선택 순서
1. `인스턴스 시작` 메뉴 클릭합니다.
2. `프리 티어 사용 가능` 메뉴 $\to$ `선택` 클릭 - 저는 맨 첫번째 서버를 선택했습니다.
3. 인스턴스 유형에서 `프리티어 사용 가능` 서버 선택합니다.
4. `검토 및 시작` 클릭합니다.
```

`검토 및 시작`을 클릭하면 다음 화면으로 이동합니다.
`인스턴스`(우리가 생성하는 `클라우드 서버`를 인스턴스라고 부릅니다.) 검토 화면이 나옵니다. 특별히 할 일은 없습니다. 궁금한 사람들은 메뉴들을 클릭해 봅니다. 우리는 바로 `클릭하기`를 눌러서 다음 단계로 넘어갑니다. 그림 {numref}`appendix_22_ec2_config_review`를 참고하기 바랍니다.

```{figure}  ../../imgs/Appendix/appendix_22_ec2_config_review.png
---
class: bg-primary mb-1
width: 700px
align: left
name: appendix_22_ec2_config_review
---
`인스턴스`(클라우드 서버) 검토 화면
```

`인스턴스 시작` 아이콘을 클릭하면 `키 페어` 생성 화면이 뜹니다.
기존 아마존 클라우드 서버 사용자라면 이전 `키 페어` 이름이 뜹니다.
처음 아마존 서버를 만드는 경우라면 그림 {numref}`appendix_23_ec2_key_pair_generation`와 같은 화면이 뜹니다.
저는 `hello_cju`라고 이름을 입력해 봤습니다. 여러분은 여러분이 좋아하는 이름을 지어주면 됩니다.

```{figure}  ../../imgs/Appendix/appendix_23_ec2_key_pair_generation.png
---
class: bg-primary mb-1
width: 700px
align: left
name: appendix_23_ec2_key_pair_generation
---
`키페어(Key pair)` 생성 화면
```

`키 페어 다운로드` 아이콘을 클릭하면 여러분이 입력한 이름에 확장자 `.pem`이 붙은 파일을 다운로드 하는 창이 뜹니다. 여러분이 원하는 위치에 저장해 주세요. 저는 `hello_cju.pem` 파일을 `다운로드` 폴더에 저장했습니다. 여러분은 여러분이 좋아하는 위치에 저장하면 됩니다.

```{admonition} 키 페어는 언제 쓰나요?
`키 페어`는 아마존 서버에 원격으로 접속할때 필요합니다.
각종 SSH, FTP 접속에 필요합니다. 우리는 국산 SSH 접속 프로그램 중 하나인 `Xshell`을 이용해서 실습해 볼 예정입니다.
VS code `remote-SSH` 익스텐션(확장 프로그램)을 설치하면 SSH를 편리하게 사용할 수 있습니다. 이것도 실습할 예정입니다.
```

키 페어 파일은 여러분이 만든 클라우드 서버에 접속할때 사용하는 비밀키입니다. **절대 해킹 당하거나 유출뒤면 안됩니다.**
`반드시 안전한 장소에 보관하시기 바랍니다.`

```{figure}  ../../imgs/Appendix/appendix_24_save_key_pair_file.png
---
class: bg-primary mb-1
width: 700px
align: left
name: appendix_24_save_key_pair_file
---
`키페어(Key pair)` 생성 화면
```

키 페어를 저장하는 그림 {numref}`appendix_24_save_key_pair_file`은 여러분에게 매우 익숙한 화면일 것입니다. 원하는 위치에 `.pem` 파일을 저장합니다. 키페어 저장이 끝났으면 그림 {numref}`appendix_25_save_key_pair_and_continue`와 같이 `인스턴스 시작`을 클릭합니다.

```{figure}  ../../imgs/Appendix/appendix_25_save_key_pair_and_continue.png
---
class: bg-primary mb-1
width: 700px
align: left
name: appendix_25_save_key_pair_and_continue
---
인스턴스 생성 및 시작 화면
```

`인스턴스 시작`을 클릭하면 그림 {numref}`appendix_26_click_instance_view`와 같은 화면이 뜹니다.
`지금 인스턴스를 시작 중입니다.`라는 메시지가 보이면 모든게 정상적으로 진행되고 있다는 의미입니다.
인스턴스(클라우드 서버)가 잘 생성되었는지 `인스턴스 보기`를 클릭해 봅니다.

```{figure}  ../../imgs/Appendix/appendix_26_click_instance_view.png
---
class: bg-primary mb-1
width: 700px
align: left
name: appendix_26_click_instance_view
---
인스턴스(클라우드 서버) 생성 화면
```

인스턴스(클라우드 서버)의 상태 화면을 확인합니다.
이전에 사용하던 인스턴스가 있다면 목록이 같이 나타납니다.
만약 여러분이 처음 인스턴스를 생성했다면 1개의 서버 목록만 나타납니다.

조금 전에 생성한 인스턴스에 이름을 붙여줄 수 있습니다.
`Name`이라는 부분을 클릭하여 인스턴스(클라우드 서버)에 이름을 붙여줍니다. 이름이 없어도 상관없습니다. 

나중에 클라우드 서버를 여러개 생성하면 헷갈릴 수 있기 때문에 이름을 지어주는 것도 좋습니다. 저는 `hello_cju`라고 이름을 붙여 줬습니다.
그림 {numref}`appendix_27_naming_instance`를 참고하세요.


```{figure}  ../../imgs/Appendix/appendix_27_naming_instance.png
---
class: bg-primary mb-1
width: 700px
align: left
name: appendix_27_naming_instance
---
인스턴스(클라우드 서버)에 이름 지어주기
```

여러분이 생성한 인스턴스를 선택하면 아래쪽에 여러분이 지금 만든 클라우드 서버의 자세한 정보를 확인할 수 있습니다. 그림 {numref}`appendix_28_instance_detail`를 확인하세요.

```{figure}  ../../imgs/Appendix/appendix_28_instance_detail.png
---
class: bg-primary mb-1
width: 700px
align: left
name: appendix_28_instance_detail
---
인스턴스(클라우드 서버) 세부 정보 확인하기
```

가장 중요한 정보는 `퍼블릭 IPv4 주소`라는 정보입니다. 여러분이 인터넷이 연결된 어디에서든지 이 주소를 활용해 클라우드 서버에 접속해서 다양한 작업을 하게 됩니다. 퍼블릭 IP 주소는 개인마다 다릅니다. 제 화면하고 동일한 숫자가 나오지 않는 것이 정상입니다.

참고로 `프라이빗 IPv4 주소`라는 정보도 있습니다. 이것은 아마존이 내부 서버를 구성하기 위해 설정한 주소입니다. 우리는 잘 사용하지 않을 것입니다.

이제 여러분들은 아마존에서 제공하는 클라우드 서버를 만들었습니다.
조금 복잡해 보일지 모르지만... 여러분이 직접 서버 본체를 사고, IP 주소 확보하고, 각종 네트워크 설정하고, 리눅스 운영체제 설치하고, 보안 설정하는 것보다는 훨씬 편리합니다.

사실 클라우드는 처음 웹 시스템을 공부하는 사람들에게는 큰 축복입니다.

클라우드 서버 만들기에 성공한 여러분들께 축하의 말씀을 전합니다. ^^.


