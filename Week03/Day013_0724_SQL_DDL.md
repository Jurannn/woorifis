# 240724 MySQL

```html
<html>
<head> </head>
<body>
	<h1> 제목 </h1>
</body>
</html>
```

비정형 데이터 - 바이너리

dbms - 서버에 db를 항상 올려놔야함

![Untitled](240724%20MySQL%20d2b51ef0ef8a408385140e554b28b698/Untitled.png)

스키마 : 데이터베이스의 메타데이터

테이블 : 행과 열로 구성된 테이블

데이터베이스 객체 : 테이블 간의 관계를 미리 맺어두는 프로시저 같은거.. ***데이터베이스 객체***란 ***데이터베이스*** 내에 존재하는 논리적인 저장 구조

컬럼 = 열 = 속성 = 어트리뷰트

로우 = 행 = 데이터 튜플 = 레코드

데이터마트 : 현업자(분석가, 기획자..)가 데이터를 활용할 수 있는 수준으로 데이터를 정제해서 적재한 곳

데이터웨어하우스 : 레이크에서 수집된 데이터를 주제별로 저장하는 물리적/논리적 공간, 통합 저장

데이터레이크 : 여러 원천에서 발생한 데이터를 raw 데이터 자체로 저장

### DBMS의 유형

1. 계층적 DBMS
    1. 데이터가 부모와 자식 관계가 있는 트리와 같은 구조로 구성됨
    2. 처음 구성 후 변경 어렵, 유연성 떨어짐
    3. 현재는 거의 사용 x
    4. plasma를 cd에 넣기 위해 다시 테이블을 생성하든지.. 아니면 타고 올라가서 가져오든지 해야되서 별룽
2. 네트워크 DBMS(망형 DBMS)
    1. 프로젝트/부서 단위로 관리 - 주제 단위 x → 설계나 관리가 복잡해짐
    2. 다대다 관리
3. 관계형 DBMS(RDBMS) → MySQL
    1. 중심이 되는 key를 기준으로 테이블 join
    2. 원본에는 중복되는 정보를 최소화
4. NoSQL DBMS → 엘라스틱서치
    1. 비관계형 DBMS 클래스
    2. key-value DB, graph DB, column Family, Document

### RDBMS

스키마를 나누어서 관리하는 이유

정렬방식

인코딩양식

컬럼 생성 주의사항

- 기준이 되는 컬럼(PK) ; NOT NULL 명시하기
- 기왕이면 띄어쓰기는 하지 않는 것이 좋습니다. 띄어쓰기를 사용하면 컬럼(열) 이름을 큰따옴표로 묶어줘야 해서 불편하므로 대부분 띄어쓰기 위치에 언더바(_)를 사용합니다.
- CHECK
    - 해당 열의 값은 지정된 조건을 만족해야 합니다.
    - 예시: CREATE TABLE students (name VARCHAR(20), age INT CHECK(age > 0));

테이블명 주의사항

- 예약어 사용 불가

대소문자를 가리지 않음 → 대문자로 입력해도 ok 근데 소문자로 입력됨

# sql-2

- 별칭적을 때 as 생략 가능
- LIKE : _ ; 한글자, % ; 여러글자 → 일부 일치
- IN : 완전 일치 탐색

```sql
SELECT movie_name FROM box_office WHERE movie_name LIKE '천년'; #완전히 일치
SELECT movie_name FROM box_office WHERE movie_name LIKE '천년%'; #천년으로 시작
SELECT movie_name FROM box_office WHERE movie_name LIKE '%천년%'; #첫년이 들어가는
```

 # format(sale_amt, 0) ; 숫자 000,000,000 이렇게 만들어줌

```sql
SELECT gender, COUNT(math), AVG(math), MIN(math), MAX(math), SUM(math)
FROM students
GROUP BY gender -- 원본을 그대로 두고 원본에 없는 값을 연산하는 것임
HAVING AVG(math) > 60 -- 집계함수의 WHERE절로 볼 수 있음~~~~!!! (WHERE은 행연산에서의 조건, HAVING은 원본에 없는 값으로 조건)
ORDER BY AVG(math) DESC;
```
