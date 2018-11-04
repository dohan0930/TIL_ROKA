# SNORT
10월 중순즈음에 간부와 IPS 시그니처에 대한 얘기를 하다가 어쩌다 보니 **Snort rule**이라는 얘기가 나왔다.  
Smart rule로 알아듣고 그게 뭐지 하고 있다가 나중에 궁금해서 찾아보니 아예 다른 개념이라는것을 알게 되었다.

## SNORT란?
[SNORT](https://www.snort.org/)는  
> It is an open source intrusion prevention system capable of real-time traffic analysis and packet logging.

라고 공식 홈페이지에서 소개하고 있다.  
해석하면 리얼타임으로 패킷/트래픽을 조사하는 오픈소스 IDPS(Intrusion Detection and Prevention Systems)이다.  
  
SNORT는 rule 기반으로 패킷을 판단하고 처분을 결정하게 되는데, 이 Rule들은 SNORT rule format 형태로 작성되게 된다.  
SNORT rule 포맷은 네트워크 보안업계에서 보편적으로 사용되고 있다.  
(커뮤니티의 빠른 기능 개선, 오류 수정 등으로 다른 IPS가 따라오기 힘든 수준이며, 사실상의 IPS 기술 표준)  
(OISF에서 개발한 Suricata도 SNORT rule이 호환됨.)  
  
**따라서 IPS를 사용할 때 SNORT rule에 대한 기본적인 이해가 되어 있어야 하는것이다.**
  
## SNORT Rule
SNORT Rule은 크게 Header와 Option으로 나뉘게 된다.  
