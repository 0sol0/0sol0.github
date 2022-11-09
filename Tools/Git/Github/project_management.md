# ProjectManagement

## Commit
- feat : 기능(새로운 기능)
- fix : 버그(버그 수정)
- refactor : 리팩토링
- style : (코드 형식, 세미콜론 추가: 비즈니스 로직에 변경 없음)
- test : 테스트(테스트 코드 추가, 수정, 삭제: 비즈니스 로직에 변경 없음)
- docs : 문서(문서 추가, 수정, 삭제)
- chore : 기타 변경 사항(빌드 스크립트 수정 등)

ex) Feat : 검색 기능 #5 => 검색 기능 #5 Issue 열림
ex) Feat : 검색 기능 close #5 => 검색 기능 #5 Issue 닫

## Issue
 : 작업단계별 task 및 sub-task를 관리함
- Assignees : Issue에 Assignees를 선택하여 작업 담당자를 설정함
- Milestones(작업 단위 목표) : Issues를 그룹핑하여 그룹을 관리하고 그룹의 진행현황을 추적함(기능, 주)

### Label
 : Issue에 Label을 추가하여 Issue를 카테고리별로 관리함

    - enhancemeant(향상) : New feature or reuest(새로운 기능 또는 요청 [commit feat])
    - bug(버그) : Something isn't working(뭔가 작동하지 않습니다. [commit fix])
    - documentation(문서) : Improvements or additions to documentation(문서 개선 또는 추가 [commit docs])

    - duplicate(복제) : This issue or pull request already exists(이미 있는 Issue, Pull Request입니다.)
    - help wanted(도움 필요) : Extra attention is needed(각별한 주의가 필요합니다.)
    - invalid(유효하지 않음) : This doesn't seem right(이것은 옳지 않은 것 같습니다.)
    - question(질문) : Further information is requested(추가 정보가 요청됩니다.)
    - wontfix(꼼수) : This will not be worked on(이것은 작동하지 않습니다.)
    - good first issue(좋은 첫번째 issue) : Good for newcomers(신규가입자에게 좋음)

## Project
 : Issue를 진행상태에 따라 구분하여 work flow를 관리함(기능, 주)

### Project 생성
- None : 아무 것도 없이 프로젝트만 생성하는 것이다.
- Basic Kanban : To Do, In Progress, Done 이 생성된다.
- Automated kanban : To Do, In Progress, Done이 생성되고 자동화가 된다.
- Automated kanban with reviews : To Do, In Progress, Review In Progress, Reviewer Approved Done 이 생성된다.
- Bug triage : Needs triage, High priority, Low priority, Close가 생성이 된다.

## project 진행 상황
- To Do : 해야 할 작업
    - 새로 추가 되는 모든 이슈가 해당(해야할 것, 새로운 기능 추가, 기능 수정 등등)
    - 새로 추가 되는 모든 PR이 해당

- In Progress : 진행 중인 작업
    - 작업이 진행중 이라는 것을 의미
    - 새로 열린 모든 PR이 해당
    - 새로 열린 모든 이슈가 해당

- Done : 완료된 작업
    - 이슈가 Close되면 해당
    - Merge가 된 PR이 해당
