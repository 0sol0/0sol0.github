## Linux 명령어
### 생성한 ssh와 연결
`ssh -i keypair경로 ubuntu@퍼블릭 ipv4 주소`

### 폴더 경로
- 절대 경로 `cd /home/user/example` '/home/user' 안에 'example'폴더로 이동
- 상대 경로 
    - `cd ./example`: 현재 위치에서 'example'폴더로 이동
    - `cd ../`현재 위치에서 상위 폴더로 이동
- 현재 경로 `pwd`

### 폴더 생성
- 절대 경로 `mkdir /home/user/example` '/home/user' 안에 'example'폴더 생성
- 상대 경로 
    - `mkdir ./example2`: 현재 위치에서 'example2'폴더 생성
    - `mkdir ./example/example3`현재 위치에서 'example'폴더 안에 'example3'폴더 생성

### 파일 목록 보기
- `ls` 현재 위치에 파일 목록 보기
- `ls -l` 현재 위치에 파일 목록 자세히 보기
- `ls -a` 현재 위치에 숨겨진 파일 목록 포함해 보기
- `ls -al` 현재 위치에 숨겨진 파일 목록 포함해 자세히 보기
- `ls ./test` 현재 위치에 있는 'test'폴더 안에 있는 파일 목록 보기

### 파일 생성
- `touch test.txt`

### 파일 복사
- `cp test.txt test_copy.txt` 파일 복사
- `cp -r directory directory_copy` 폴더 복사

### 파일 이동
- `mv ./test/test.txt ./` 'test'폴더 안에 있는 'text.txt'파일을 현재 위치로 이동
- `mv test.txt test2.txt` 'test.txt'파일 이름을 'text2.txt'로 변경

### 파일 삭제
- `rm text.txt` 파일 삭제
- `rm -r diretory` 폴더 삭제

### 파일 내용 보기
- `cat test.txt` 전체 보기
- `head test.txt` 처음 10줄만 보기
- `tail test.txt` 마지막 10줄만 보기

### 패키지 설치
- `sudo apt update`
- `sudo apt install net-tools`
- `ifconfig`
- `apt install package`

### 파일 찾기
- greb : 문자열이 포함된 파일 찾기
    - `greb word ./*`  현재 경로의 모든 파일에서 'word'가 포함된 파일 찾기
    - `greb word ./* -r` 현재 경로의 모든 폴더 안에서 'word'가 포함된 찾기
- find : 조건이 포함된 파일 찾기
    - `find / -name "*.txt"` 최상위 경로에서 파일이 '.txt'인 파일 찾기
    - `find / -type d` 최상위 경로에서 모든 폴더 검색
    - `find / -type f -name "*.txt"` 최상위 경로에서 파일이 '.txt'인 파일 찾기

