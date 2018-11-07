# Apache HTTP Server Access Log
CCE 본선 공방전에서는 초반에 웹 취약점 코드 패치 전  
Apache HTTP Server access log를 위주로 판단하는 전략을 세웠었지만 잘 먹히지 않았다.   
지금 다시 생각해보면 access log만 좀 더 잘 봤더라도 초반에 그렇게 빠르게 실점을 하지는 않았을것 같다. ~~제주 맛집~~  
Access Log는 어떻게 생성되고, 어떤 내용이 담겨 있는지 정리해 보자.  
  
## Apache HTTP Server에는 어떤 로그들이 생성되는가?
[Apache HTTP Server 공식 문서](https://httpd.apache.org/docs/2.4/en/logs.html) 를 보자.  


