# 240711 - 문자열 출력/함수

# 1. 문자열 출력

## 1. 문자열 메소드

- 메소드를 활용해 불필요한 반복문을 줄일 수 있다.
- 파라미터 = argument(인자)
    - `str1.split(sep = '/', maxsplit = 2)`
        - sep ; 파라미터
        - ‘/’ ; 인자
    - 파라미터를 명시하면 순서대로 안써도 됨
    - but 명시하지 않으면, 순서대로 써야함. 그리고 파라미터를 생략 가능함

1. `split([sep ,maxsplit])`
    - sep의 default argument는 ‘ ‘(공백)
2. `str.replace(old, new[, count])`
    - count ; 바꾸는 횟수
3. `str.strip([chars])` : 앞뒤만 제거됨!!! 문자열 안에는 x
    - chars의 default argument는 공백과 escape 문자
    - `str.rstrip([chars])` ; 오른쪽 공백 제거
    - `str.lstrip([chars])` ; 왼쪽 공백 제거
4. `str.join(iterable)` : 여러 개의 문자열을 하나의 문자열로 합쳐 새로운 문자열을 return ; 리스트를 str으로 바꿀 수 있음!
    - str ; 문자 사이에 어떤 문자를 넣을 지 입력
        
        ```python
        a = ['짱구', '짱아', '장구엄마', '짱구아빠']
        '*'.join(a)
        ```
        
5. `str.casefold()` / `str.capitalize()`  / `str.upper()`   / `str.lower()`
    - `str.casefold()` : 유니코드 기준으로 lower보다 더 많은 문자열을 소문자화 할 수 있음
    - `str.capitalize()` : 문장 첫번째 단어를 대문자로
6. `str.find('찾을 문자'[, 시작인덱스[, 끝인덱스]])`
    - 문자열에 포함된 첫번째 요소의 index 값 반환
    - 찾고자 하는 특정 문자열이 여러 개인 경우에는 최초 발견한 원소의 시작위치만 알려줌(circuit evaluation)
    - -1 ; 없는 값을 찾는 경우 return 값

- method chaining 방식 : 한 객체의 메소드를 연속으로 호출하여, 결과를 이어서 사용하는 프로그래밍 방식
    
    ```python
    string = string.upper()
    string = string.strip()
    length = len(string)
    
    #위의 세 줄으리 코드를 체이닝을 통해 다음과 같이 표현 가능
    length = len(string.upper().strip())
    ```
    
- `sorted(`이터러블객체, *, key, reverse)
    - (**__iterable: Iterable[SupportsRichComparisonT@sorted]**, *, key: None = ..., reverse: bool = ...)
        - default : reverse = False ; 오름차순
        - 정렬 기준이 되는 함수를 넣음. lambda 이용 가능 !! - 여러 개의 요소를 가진 경우
        - 비교할 아이템의 요소가 복수 개일 경우, **튜플로 그 순서를 내보내주면 된다.** 즉, 첫 번째 인자를 기준으로 먼저, 두 번째 인자를 다음 기준으로 정렬함
            - ex. `sorted(e, key = lambda x : (x[0], -x[1]))`
                
                ```python
                e = [(1, 3), (0, 3), (1, 4), (1, 5), (0, 1), (2, 4)]
                f = sorted(e, key = lambda x : (x[0], -x[1]))
                # f = [(0, 3), (0, 1), (1, 5), (1, 4), (1, 3), (2, 4)]
                ```
                
            - - 를 붙이면, 현재 정렬차순과 반대로 하게 된다.
- collections - Counter
    - **most_common**([*n*]) ; *n* 개의 가장 흔한 요소와 그 개수를 가장 흔한 것부터 가장 적은 것 순으로 나열한 리스트를 반환

## 2. 정규식(Regular Expression)

- 참고 사이트
    - [https://velog.io/@bbkyoo/Logstash-grok-필터-와-정규식-정리](https://velog.io/@bbkyoo/Logstash-grok-%ED%95%84%ED%84%B0-%EC%99%80-%EC%A0%95%EA%B7%9C%EC%8B%9D-%EC%A0%95%EB%A6%AC)
    - [https://regex101.com/](https://regex101.com/)

- 실행 방법
    - 함수로 실행
        
        ```python
        import re
        m = re.match(r'([a-zA-Z]+)@([a-zA-Z]+)\.com', 'abcd@naver.com')
        print(m)
        ```
        
    - 정규표현 패턴 오브젝트의 메소드로 실행
        
        ```python
        p = re.compile(r'([a-zA-Z]+)@([a-zA-Z]+)\.com')
        m = p.match('abcd@naver.com')
        print(m)
        ```
        

- 메타 문자
    - [] : 문자 클래스(charater class)
        - .(dot) 자체를 찾으려면 [.]라고 패턴을 만들면 됨!
    - ^[] : ~로 시작하는
    - [^] :not
    - $ : ~로 끝나는
    - +:1글자 이상(1~)
    - *:해당 문자가 있거나 공백(0개)인 모든 것(0~)
    - ?:0개(공백)~1개 == {0,1}
    - {m, n} : m번 이상 n번 이하
    - . :  \n을 제외한 모든 문자를 매칭(wild card)
        - `a.b` vs `a[.]b`
- Flags
    - re.IGNORECASE / re.I
        - Perform case-insensitive matching; expressions like `[A-Z]` will also match lowercase letters
        - Igmorecase는 default로 off되어있음
    - re.MULTILINE / re.M
        - \n를 한 줄로 간주해서 패턴 검색
        - When specified, the pattern character `'^'` matches at the beginning of the string and at the beginning of each line
    - 동시에 사용하려면 ; |(리눅스에서 파이프라인)
        
        ```python
        test_string2 = '''happy happy dappy happyis HAPPY HaPpy Happy
        Happy Happy'''
        
        re.findall('^happy\s', test_string2, flags = re.IGNORECASE | re.MULTILINE)
        ```
        

- re.sub(pattern, repl, string)
    - (**pattern: str | Pattern[str]**, repl: str | ((Match[str]) -> str), string: str, count: int = ..., flags: _FlagsType = ...)

- raw string ; \(escaping 문자)와 그 다음에 오는 문자를 그대로 string 자체로 받아들인다
    
    ```python
    a = 'abc\nabc'
    print(a)
    
    b = r'abc\nabc'
    print(b)
    
    c = 'abc\\nabc'
    print(c)
    ```
    

- 그루핑 패턴 - 1부터 시작!!!!, 별명을 지어서 부를 수 있음
    
    ```python
    re.compile(r'(?P<이름>문자열)')
    ```
    

## 3. 문자열 포맷팅

- 참고 사이트
    - [https://pyformat.info/](https://pyformat.info/)

1. f-string
    
    ```python
    PI = 3.14159265465465465465
    r = 3
    print(f'파이: {round(PI, 2)}')
    print(f'반지름이 {r}인 원의 넓이: {r*r*PI:.3f}')
    ```
    
2. format  `str.format(*args, **kwargs)`
    
    ```python
    print('파이 : {}'.format(round(PI,2)))
    print('반지름이 {}인 원의 넓이 : {: .3f}'.format(r, r*r*PI))
    ```
    
    ```python
    a = 3
    b = 2
    
    'the sum of {1} + {2} = {0}'.format(a, b, a+b)
    ```
    
3. % = 호환은 되지만 데이터 손실이 있다 - decimal, float은 호환 가능 근데 지수부를 버림)
    
    ```python
    a = '하하하'
    b = 2
    c = 1.3445322
    
    'The sum of %s + %d = %f' % (a, b, c)
    ```
    

## 4. 표준 출력

# 2. 함수

- def 함수를 정의할 때는 함수 자체를 실행하지 않아서 에러를 발견할 수 없음
- parameter(인자), argument(인수)
- 기본적으로는 argument의 자료형을 강제할 수 없다
- `def 함수명(parameter)`; 함수의 시그니처, 헤더
- 디폴트 파라미터
    
    ```python
    def hi(name = 'juran', hi = 'hi'):
      return f'{name}! {hi}~'
      
    hi('minsu', 'hello')
    ```
    
    ```python
    def hi2(hi, name = 'juran'):
    #SyntaxError: non-default argument follows default argument 순서 주의!
      return f'{name}! {hi}~'
    
    hi2()
    
    hi2('hello')
    
    hi2('hello', 'minsu')
    ```
    

- return은 1개만 가능
- 함수 부가 설명 - docstring ; document를 적기 위한 string 이라는 의미
    
    ```python
    def func():
    	'''
    	함수에용
    	'''
    ```
    

- 가변 인자 : 입력 값의 개수가 정해져 있지 않은 경우
    - 파이썬에서 가변인자는 튜플로 묶어서(패킹) 전달이 됨
    - 실행문에 *가 있으면 순서 없음. 패킹되지 않음
    
    ```python
    def 함수명(*args):
        print(args)
    ```


    ```python
    def 함수명(**kwargs):
    #가변인자/파라미터 순서로 받을거야. 몇개인지는 몰랑
    	실행문
    ```

