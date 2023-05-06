# release-plan-doc-bot

<details>
<summary>요구사항 상세 보기</summary>
<div markdown="1">

## 🚀 기능 요구사항
- 이 프로그램은 배포계획서 관련 업무를 자동으로 진행하는 프로그램이다.
- 배포계획서 관련 업무는 다음과 같다
  - 배포일마다 배포계획서 내 **제목, 내용, 작업**을 취합해서 메일로 발송
  - 배포계획서 내용을 Serviceflow 내용을 기반으로 검증 및 수정
  - 검증 후 **배포계획서 및 Serviceflow 내용**을 취합해서 메일로 발송

## ✍🏻 입출력 요구사항
### ⌨️ 입력
- Word 문서(.docx)로 된 배포계획서
- 배포계획서를 입력받은 이후, 검증/일별 취합/주별 취합/종료를 구분하는 1/2/3/0 중 하나의 수
- 배포계획서 내 오류가 있는 경우, 내용 수정을 위한 문자열

### 🖥 출력
- 일별/주별 취합 시 취합 양식에 맞는 Word 문서 생성 후 문서 경로를 출력
```
{문서 경로}/{문서 이름}을/를 생성했습니다.
```
- 입력받은 배포계획서가 없는 경우, 오류 메시지 출력 후 종료
```
선택된 배포계획서가 없습니다. 프로그램을 종료합니다.
```
- 검증 중 수정 사항이 있는 경우, 수정이 필요한 내용을 출력 후 입력 대기
```
{문서 이름} 검증 중 다음 오류가 확인되었습니다. 
ERROR : SOR ID EMPTY
변경할 데이터를 입력해주세요.
SOR ID(CHXXXXXX-XXXXXX) : 
```

## 🎱 프로그래밍 요구사항
- Python 코드 컨벤션을 지키면서 프로그래밍한다.
  - 기본적으로 [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)을 원칙으로 한다.
- indent(인덴트, 들여쓰기) depth를 3이 넘지 않도록 구현한다. 2까지만 허용한다.
  - 예를 들어 while문 안에 if문이 있으면 들여쓰기는 2이다.
  - 힌트: indent(인덴트, 들여쓰기) depth를 줄이는 좋은 방법은 함수(또는 메소드)를 분리하면 된다.
- 3항 연산자를 쓰지 않는다.
- 함수(또는 메소드)가 한 가지 일만 하도록 최대한 작게 만든다.
- 자주 변동되는 정보(ex. 개발자 이름 및 직책)는 별도 파일로 관리한다.
- TDD 방식을 기반으로 Red > Green > Refactor 순으로 개발을 진행한다. (테스트가 불가한 경우, ISSUE에 작성)

## 📈 진행 요구사항
- 기능을 구현하기 전에 release-plan-doc-bot/README.md 파일 및 ISSUE에 구현할 기능 목록을 정리해 추가한다.
- git의 commit 단위는 앞 단계에서 README.md 파일에 정리한 기능 목록 단위로 추가한다.

</div>
</details>

## 기능 목록
- [v] load release plan from docx file
- [v] create daily report from a list of release plans