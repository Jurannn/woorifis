# 240712 - 함수/모듈/패키지/예외처리

# 함수

- *args ; 순서대로 인자를 받음 ⇒ 한 묶음(튜플)로 받음
**kwargs ; key-value 형식으로 값을 전달 (파라미터-아규먼트 순서) ⇒ 한 묶음(딕셔너리)로 받음

    ![Untitled](https://github.com/user-attachments/assets/cfdedf53-a5b5-40c4-abf1-e30fd474f8f4)
    

- return은 하나의 결과를 반환 + return 뒤의 코드는 실행되지 않음

    ![Untitled 1](https://github.com/user-attachments/assets/472e3e19-3066-4d3a-a0f9-c594888c7b69)


- argument 순서
    1. positional arguments (non-default → default)
        1. positional argument ; 정의된 순서대로 값을 전달
    2. *args(variable length positional arguments)
    3. keyword-only argumets
        1. keyword argument ; 순서 대신 parameter 이름으로 맞추어서 값을 전달 → parameter 순서가 바뀌어도 됨
    4. **kwargs(variable length keyword arguments)
    

    ![Untitled 2](https://github.com/user-attachments/assets/be7e8fb2-0e18-4abd-8efd-472ab6fbd178)

    
- isinstance(data, type)
    - type(data)가 type과 일치하는지 True/False로 반환
- 조기return
    

    ![Untitled 3](https://github.com/user-attachments/assets/5df6b5c8-d91e-46f3-8401-3b6c9e8de736)

    
- unpacking
    
    ```python
    list(filter(lambda i : i%2 == 0, li))
    
    [*filter(lambda i : i%2 == 0, li)] #unpacking
    ```
    

    ![Untitled 4](https://github.com/user-attachments/assets/d8085bb2-c5b6-446e-80e8-027bab0bdab5)

    
- 파이썬의 데이터 구조
    - 주소(id)의 값이 큼/작음
    - Stack : 함수 호출하면 생성되고 실행이 완료되면 소멸, 후입선출
    - Heap : 동적 할당으로 생성
    

    ![Untitled 5](https://github.com/user-attachments/assets/a1dcfd3d-fd91-4631-ba76-af2d751350ff)

    
- 함수 내에 지역 변수 넣는 방법
    - 함수 안에서는 원래 지역변수가 전역변수에 우선
    - but, `global 변수명` 으로 선언하면 전역변수를 변경할 수 있음
        
        ```python
        # 전역변수(Global Variable): 파이썬 인터프리터가 종료되기 전까지는 어느 곳에서나 쓸 수 있는 변수
        a = '사과나무'
        b = '포도나무'
        
        def value1(a_):
            # 함수 안에서 선언한 변수는 함수가 종료되며 사라집니다.
            # 지역변수(Local Variable)
            # 함수 안에서는 지역변수가 전역변수에 우선합니다.
            a = a_
            print('함수 안에서', a, b)
            return a # a라는 변수에게 메모리가 사라지기 전에 나갈 수 있게 문을 열어줌
        
        value1('안녕')
        print('함수 밖에서', a, b)
        ```
        
- `globals()` ; 현재 정의된 모든 전역변수를 확인 가능
    - `a in globals()`

## 재귀함수

## 익명함수(lambda)

```
방법 1.
-   (lambda 매개변수들 : 식)(인수들)
방법 2.
-   객체명 = lambda 매개변수들 : 식
-   객체명(인수들)
```

```python
(lambda a, b : a+b)(1,2)
```

### 함수형 프로그래밍/함수형 문법

- 리스트 컴프리핸션
    - `[(변수에 적용할 수식) for (변수) in (for문이 돌아가는 범위)]`
    - `[(row, col) for row in rows for col in cols]` ; 이중 for문
    - 그냥 for문보다 훨씬 빠름
    - 집합, 튜플, 딕셔너리 컴프리핸션도 존재
        - 튜플의 경우 tuple()로 생성해야함
        - ()로 하면 generator로 만들어짐
    
    ```python
    [0 for _ in range(10)] #초기화된 리스트 만들 때 주로 사용
    ```
    

- Map
    - `map(function_name, list_data)`
    - 시퀀스 자료형 각 요소에 동일한 함수를 적용할 때
    - map 함수가 반환한 객체는 반복 가능한(iterable) 객체
    - 실행시점에 값을 생성하기 때문에 메모리 효율적
    
    ```python
    li1 = [1,2,3,4,5]
    li2 = [10,20, 30, 40, 50,60]
    list(map(lambda i,j : j/i, li2, li1))
    ```
    
    - callback 함수
        - 함수 안에서 함수를 실행
        - 부르는 함수 : Caller, 불리우는 함수 : Callee
            
            ```python
            list(map(plus_3, li))
            
            #map -> plus_3 -> list
            ```
            

# 함수

1. `filter(function, iterabler)` : 이터러블의 각 요소에 대해 function이 참인 것만 반환하는 요소의 이터레이터
2. `enumerate(변수명)` ; (인덱스 번호, 리스트 원소)로 출력
3. `zip(list, list)` ; 두 개 이상의 리스트를 병렬적으로 추출
4. `reduce(function, iterable, initializer = None)` ; 반복 가능한 객체의 각 요소를 지정된 함수로 처리한 뒤 이전 결과와 누적해서 반환
    
    ```python
    from functools import reduce 
    reduce(lambda x, y : x+y, list(range(11)))
    ```
