# linux_performance_analysis_in_60000_milliseconds
서버 점검을 하라고 시키지만, 막상 뭘 해야할지 멘붕이 올 때가 많다.  
물론 어떻게 점검하라고 가이드는 내려오지만, 여러가지 Official하게 밝힐 수 없는 이유로 부족한 점이 많다.  
이렇게 수박 겉핥기 식으로 서버를 봐도 되는가 싶어 검색해봤다.  
그러다 [Netflix팀의 글 - Linux Performance Analysis in 60,000 Milliseconds](https://medium.com/netflix-techblog/linux-performance-analysis-in-60-000-milliseconds-accc10403c55)을 발견했다.  
읽어보니 내가 원하는 내용인것 같아 번역하고 정리해보려고 한다.

## Netflix의 시스템  
Netflix는 현재 Amazon EC2 Linux Cloud로 대규모 시스템을 구성중이며, 이러한 시스템의 상태를 파악하기 위해 수많은 툴들을 사용하고 있다.  

### Amazon EC2
> **Amazon Elastic Compute Cloud(EC2)** 는 안전하고 크기 조정이 가능한 컴퓨팅 파워를 클라우드에서 제공하는 웹 서비스입니다. 개발자가 더 쉽게 웹 규모의 클라우드 컴퓨팅 작업을 할 수 있도록 설계되었습니다.  

원래는 "AWS == Amazon EC2" 이런 개념으로 알고 있었지만 AWS에서 제공하는 서비스는 엄청 많았던것이다. ~~AWS알못~~  
AWS Lambda(FaaS), AWS S3(Cloud Storage), AWS Glacier(자주 불러올 필요가 없는 데이터 위주 저장) 등 다양한 서비스가 존재한다.  

### Atlas
[Introducing Atlas: Netflix’s Primary Telemetry Platform](https://medium.com/netflix-techblog/introducing-atlas-netflixs-primary-telemetry-platform-bd31f4d8ed9a)

### Vector
[Introducing Vector: Netflix’s On-Host Performance Monitoring Tool](https://medium.com/netflix-techblog/introducing-vector-netflixs-on-host-performance-monitoring-tool-c0d3058c3f6f)
