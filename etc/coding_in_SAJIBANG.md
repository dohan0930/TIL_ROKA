# coding_in_SAJIBANG  
**#사이버지식정보방(a.k.a 사지방)에서 코딩 비스무리한거라도 해보기**  
**#군대에서 코딩하기 #군대에서 프로그래밍하기**  
여러분만큼은 저만큼 뻘짓하는 일이 없길 바라는 마음에서 1년동안의 경험을 공유합니다... 

## 주의사항
* 코딩이 너무 하고 싶더라도 **인트라넷에서는 어지간하면 하지 마십쇼.** 본인이 특정보직이 아니라면 매우 곤란해집니다.  
  물론 여러가지 인트라넷 속 대안(C# 장인이 된다거나)이 있긴 합니다만 노력에 비해 Output이 잘 안나옵니다ㅠㅠ  
* 사지방에서도 마찬가지입니다. '이 정도면 되지 않을까?' 하지말고 사지방 담당 간부/병사한테 물어보는걸 추천합니다.  

## 사지방 환경  
*쓰고 보니 어떻게 이 환경에서 코딩하는지 모르겠네요 걍 군대 안 올 수 있으면 안오시는 걸 추천드립니다....*
* **원격접속 / ftp,telnet 등 자료 통신 프로그램 사용 금지**  
  걸려서 징계당하기 싫으면 하지 마십시오.  
* **github 안됨 / gitlab, bitbucket은 가능**  
  특정 IP대역은 방화벽 상에서 막혀 있는데, 공인 IP 192, 172대역은 안됩니다.  
  (172는 라우터가 멍청해서라는 얘기도 있음.)  
  방화벽 쪽 때문에 CSS하고 AWS 관련 서비스도 다 막힌다고 들었습니다.
* **일정 용량 이상 업로드 제한**
* **마우스 우클릭 제한**  
  윈도우 시스템적으로 접근할 수 있는것은 모두 막혀있습니다. 해보시면 알게 됨....   
  다행히도 system32 폴더에 직접 들어가서 옵션 건드는건 안 막혀있음.
* **웹 브라우저 최신화 안되어있음**  
  군인공제회에 연락하면 스냅샷 시점을 올려주기는 하는데... 해본 사람말로는 좀 오래 걸린다고 합니다.  
* **로그인 이후 120분 지나면 강제 로그아웃** 
* **전원 꺼지면 스냅샷으로 싹 초기화 됨.**  
  (로그아웃은 남아있습니다. 시크릿 모드로 안 키면 비정상종료로 탭 전부 다시 복구됨!!)
* **접속 로그 남는 기준은 잘 모르겠습니다. 해당부대 사지방 담당한테 가서 물어보십시오.**
* **해 부대마다 규정이 조금씩 다른 점이 있습니다. 사지방 담당 간부님한테 가서 딜을 쳐봅시다.**  
  (github 열리는 부대도 있다고 들음)    
* **github에서 가져오는거라 gitbash 다운 안 됨.**  
  서버없으면 IDE에서 git 기능 제공하는것 많으니 그거 쓸 것.

## Useful
* **Server**  
[Shell in a box](https://github.com/shellinabox/shellinabox) : 괜찮습니다. 몇개 깨지는거 빼고 저는 잘 쓰고 있습니다.

* **Web Browser**  
[Opera](https://www.opera.com/ko) : 내장되어있는 [기능](https://help.opera.com/en/latest/security-and-privacy/#VPN)을 잘 활용합시다.  
[Whale](https://whale.naver.com/ko) : 사람들은 속으로는 웨일을 좋아하면서 왜 싫어하는 척 하는걸까? 저는 잘 쓰고 있습니다.  
[Chrome](https://www.google.com/intl/ko_ALL/chrome) : 192 대역 업데이트 서버 이슈가 있긴 한데, 걍 직접 가서 다운 받으면 됩니다.    

* **IDE**  
[구름 IDE](https://ide.goorm.io/) : ~~국방부에서 공인한~~ 국내 서비스. 어지간한건 이걸로 처리할 수 있습니다.  
국방부 SW캠프에서도 이거 쓰게 하니까 미리 연습해보시는것도 추천. 좀 느린게 문제긴 합니다.  
w3m 써서 이걸로 github 들어온다는 사람도 봄...  
[CodeAnywhere](https://codeanywhere.com) : 다른 중대 전우님이 쓰는거 봤는데 너무 괜찮던데요. 저도 한번 써보고 얘기해보겠습니다...  
[Ideone](https://ideone.com) : 예제 코드 돌려보기 좋습니다.

* **Network**  
[Outgoing port tester](http://portquiz.net) : 포트가 열려있는지 확인하고 싶을 때. 

* **Messenger**  
[slack](https://slack.com/) : 2018년 11월 기준으로 안 막혀있습니다. 킹갓 슬랙 최고다!!!  
[facebook messenger](https://www.facebook.com/messages) : 자대 가서 사지방 가면 처음 켜게 되는 그것  

## More  
다른 분들이 저보다 훨씬 잘 소개해주신 글들입니다.  
* https://lalafell.network/lalafell/coding-on-ssajibang
* https://neurowhai.tistory.com/192
* https://pgr21.com/pb/pb.php?id=freedom&no=76103&divpage=15&ss=on&sc=on&keyword=군대  
