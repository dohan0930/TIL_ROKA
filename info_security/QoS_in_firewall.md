# Quality of Service in Firewall
하는 일 특성상 다양한 방화벽을 만지게 된다. ~~그리고 Official하게 얘기할 수 없는 여러가지 점에 대해 놀라게 된다...~~  
방화벽 정책을 넣을 때는 다양한 옵션을 만지게 되는데(SIP, DIP, PORT 등) 그 중에 QoS라는 옵션을 봤다.  

## QoS가 뭐지?
당연하게도 이게 뭐지라는 생각이 들었다. 궁금하면 찾아 봐야지.  
  
QoS는 
> **Quality of service (QoS)** is the description or measurement of the overall performance of a service, such as a telephony or computer network or a cloud computing service, particularly the performance seen by the users of the network.  
> To quantitatively measure quality of service, several related aspects of the network service are often considered, such as packet loss, bit rate, throughput, transmission delay, availability, jitter, etc.    

라고 [위키백과 QoS 페이지](https://en.wikipedia.org/wiki/Quality_of_service)가 설명해 준다....  
트래픽의 종류에 따른 우선순위 개념이라는것인데... ~~몽총해서~~ 이게 왜 방화벽이랑 관련이 있는지 감도 잘 안잡혔다ㅠㅠ  
처음에는 'QoS에 따라 Firewall 적용 우선순위가 바뀌나?'라는 생각까지 했지만 물론 아니다. ~~개몽총~~  
  
일단 QoS에 대해서 좀 더 깊게 파보자.  
네트워크 자원은 언제나 한정적이고, 언제나 대역폭을 늘려서 문제를 해결할 수 는 없는 법이다.  
서비스의 형태는 점점 늘어나면서 병목현상은 계속 일어나고 있다. 이러한 문제를 해결하기 위해 QoS라는 개념이 등장한 것이다.  





## QoS랑 Firewall은 어떤 관계가 있나???
모든 트래픽은 방화벽을 거쳐서 나간다는 것을 집중해보자.  
찾다보니 이런 자료를 발견했다.  


네트워크하는 사람 너모 무섭다....  

