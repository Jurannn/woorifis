## 1. 사실(Facts)
- 파이썬 변수와 연산자, 데이터 타입

## 2. 발견(Discovery)
1. 코드가 연결되는 경우 백슬래쉬(\\)로 연결 가능.
   1. if 연결x, 세미콜론(;)으로 두 줄의 코드를 한 줄에 작성 가능함

3. Naming Conventions
    a. 변수명 앞 _(밑줄) : 내부에서만 사용되는 변수
    b. PascalCase : 클래스명
    c. snake_case : 함수명

4. 코랩 커맨드
    a. 셸 커맨드(Shell Command) : !기호를 앞에 붙여서 셸에서 명령어를 실행함 -> 리눅스 기반의 명령어 사용 가능
    b. 매직 커맨드(Magic Command) : %(%)를 이용해 코랩 환경 내에서 특정 기능을 실행하도록 설계된 명령어

5. PERL(Read, Evaluation, Print, Loop)
    a. Read : 명령어를 읽고, 인터프리터가 문자로 된 명령어를 숫자(기계어/binary)로 변환
    b. Evaluaiton : 명령어 실행
    c. Print : 명령어 실행 결과를 return
    d. Loop : 과정 반복

6. 비교 연산자
    a. 동일성(identity) - is : 동일성 비교, 타 언어의 ===과 같은 역할, 값/자료형/같은 메모리 주소에서 나오는지 확인
    b. 동등성(equality) - == : 동등성 비교, 숫자 자료형(inf/float/bool)끼리는 비교 연산자가 호환됨

7. 논리 연산자
    a. 우선순위 : not > and > or
    b. circuit evaluation : 부울(논리)연산을 할 때, 앞 연산자의 결과에 따라 뒤 연산자의 실행 여부가 결정되는 계산 방식

8. float
    a. 부동소수점 : 부정확
    b. decimal 모듈을 import 해서 정확한 소수계산 가능

9. Casting
    a. str -> float -> int
    b. int(float('2331.51'))

10. 컨테이너 자료형
    a. 시퀀스 자료형 : 순서로 값을 관리
        -리스트, 튜플, range
    b. 매핑형 : 키-값으로 자료를 관리
        - 딕셔너리 {'key':'value'}
        - 딕셔너리의 기본 메소드들은 보통 key를 중심으로 동작함
        - key가 없는 경우, dict1['key']의 경우 error 발생 -> dict1.get('key')로 에러 방지 가능!!
        - key 중복 불가 -> 중복으로 생성하면 기준 value 값이 변경됨
    c. 집합형 : 키만으로 자료를 관리

11. 복사
    a. 얕은 복사 : "같은 주소(자리)"에 다른 변수명을 지정 -> 원본 훼손 가능성
    b. 깊은 복사 : import copy 후 copy.deepcopy(원본)


12. 하드 코딩 vs 소프트 코딩
    a. 하드 코딩 : 자료가 변해도 계속 같은 결과를 나타내도록 고정
    b. 소프트 코딩 : 자료가 변하면 결과가 달라지도록 하는 종류의 코딩


## 3. 배운점(Lesson Learned)
막연하게 알고 있었던 개념들을 정리할 수 있어서 1~11 항목 모두 배울 수 있었다.



## 4.  선언(Daclaration)
수업때 쉬운 내용인것 처럼 보여도 열심히 들어서 지식을 쌓아야겠다
