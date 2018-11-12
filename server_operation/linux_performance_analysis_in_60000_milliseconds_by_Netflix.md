# linux_performance_analysis_in_60000_milliseconds
서버 점검을 하라고 시키지만, 막상 뭘 해야할지 멘붕이 올 때가 많다.  
물론 어떻게 점검하라고 가이드는 내려오지만, 여러가지 Official하게 밝힐 수 없는 이유로 부족한 점이 많다.  
이렇게 수박 겉핥기 식으로 서버를 봐도 되는가 싶어 검색해봤다.  
그러다 [Netflix팀의 글 - Linux Performance Analysis in 60,000 Milliseconds](https://medium.com/netflix-techblog/linux-performance-analysis-in-60-000-milliseconds-accc10403c55)을 발견했다.  
읽어보니 내가 원하는 내용인것 같아 번역하고 정리해보려고 한다.

## Netflix의 시스템  
Netflix는 현재 Amazon EC2 Cloud로 대규모 시스템을 구성중이며, 이러한 시스템의 상태를 파악하기 위해 수많은 툴들을 사용하고 있다.  

### Amazon EC2 Cloud
### Atlas
### Vector
