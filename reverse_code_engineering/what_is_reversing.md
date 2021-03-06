# What is Reverse Engineering
> **Reverse engineering** is the process by which a man-made object is deconstructed to reveal its designs, 
architecture, or to extract knowledge from the object; similar to scientific research,
the only difference being that scientific research is about a natural phenomenon.

## 분석 방법 종류
### 정적/동적 분석
#### 정적 분석  
실제 실행 없이 바이너리의 프로그램 코드를 읽어 파일을 분석하는 방법  
 
* 파일의 종류(File Signature - [binwalk](https://github.com/ReFirmLabs/binwalk) / [FILE SIGNATURES TABLE](https://www.garykessler.net/library/file_sigs.html)로 분석 가능)
* 파일의 크기
* 헤더([PE](https://docs.microsoft.com/en-us/windows/desktop/debug/pe-format)) 정보
* IMPORT/EXPORT API
* 내부 문자열
* 실행 압축 여부, 등록 정보, 디버깅 정보 등

#### 동적 분석  
real processor 혹은 virtual processor상에서 파일을 직접 실행시켜 파일, 레지스트리, 네트워크, 프로세스 등을 관찰하면서  
코드 흐름과 메모리 상태 등을 자세히 살펴보는 방법  

##### 프로세스 추적  
* [Autoruns for Windows](https://docs.microsoft.com/en-us/sysinternals/downloads/autoruns) : 윈도우 시스템 상의 시작프로그램 관리 Tool  
* [System Explorer for Windows](http://systemexplorer.net/) : 스냅샷 기능이 포함된 작업, 프로세스, 드라이버 등 관리 Tool  
* [Process Explorer for Windows](https://docs.microsoft.com/en-us/sysinternals/downloads/process-explorer) : 현재 동작중이거나 새로 실행, 종료 되는 process에 대해 실시간 표시  
(svchost.exe - *윈도우즈 서비스를 백그라운드로 구동하는 프로세스* - 가 어떤 서비스 그룹을 돌리고 있는지 알 수 있다.)  
* [Process Monitor for Windows](https://docs.microsoft.com/en-us/sysinternals/downloads/procmon) : File의 추가나 삭제 등 File의 변화, Registry의 변화를 실시간으로 모니터링  

##### 네트워크 추적
* [TCPView for Windows](https://docs.microsoft.com/en-us/sysinternals/downloads/tcpview) : 현재 네트워크 동작중인 프로세스를 전부 보여줌.  
* [WireShark](https://www.wireshark.org/download.html) : 로그 형태의 결과가 나오는 패킷 분석 프로그램  

##### 디버거
* [GNU Project debugger (GDB)](https://www.gnu.org/software/gdb/) : 다양한 유닉스 기반 시스템에서 동작하는 디버거  
* [OllyDbg](http://www.ollydbg.de/) : 32-bit assembler level analysing debugger for Microsoft Windows (Shareware)  

##### 역어셈블러
* [IDA](https://www.hex-rays.com/products/ida/) : 다양한 플러그인(Hex-Ray 등)이 존재하는 매우 강하고 비싼 디버거 ~~IDA PRO 살만큼만 돈벌고 싶다~~
* [objdump](http://korea.gnu.org/manual/release/binutils/binutils_5.html) : CUI 기반의 역어셈블러. GNU 바이너리 유틸리티로써 리눅스 계열에서 사용하는 역어셈블러이다.  

## 분석 대상
바이너리 파일(일반적으로 리버싱에서는 실행 가능한 형식의 파일을 지칭.), 어셈블리 코드, 소스 코드  
