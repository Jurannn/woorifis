# 객체 지향

- 객체지향 프로그래밍의 특징 - 추상화, 상속, 다형성, 캡슐화
    1. 추상화 : 본질적이고 공통적인 부분만 추출해 표현
        
        ![Untitled](240716%20-%20%E1%84%8F%E1%85%B3%E1%86%AF%E1%84%85%E1%85%A2%E1%84%89%E1%85%B3%20244fefcee43043558df0d715a43977a2/Untitled.png)
        
    2. 상속
        
        ![Untitled](240716%20-%20%E1%84%8F%E1%85%B3%E1%86%AF%E1%84%85%E1%85%A2%E1%84%89%E1%85%B3%20244fefcee43043558df0d715a43977a2/Untitled%201.png)
        
        - 오버라이딩
        - 오버로딩
    3. 다형성 : 객체의 속성이나 기능이 그 맥랑에 따라 다른 역할을 수행할 수 있음(다양한 형태가 되는 성질)
    4. 캡슐화 : 서로 연관있는 속성과 기능들을 하나의 캡슐로 만들어 내부를 외부로부터 보호, 외부로부터 숨길 수 있음
        
        ![Untitled](240716%20-%20%E1%84%8F%E1%85%B3%E1%86%AF%E1%84%85%E1%85%A2%E1%84%89%E1%85%B3%20244fefcee43043558df0d715a43977a2/Untitled%202.png)
        
    

# 클래스

## 클래스

- 클래스는 함수와 동일한 개념
- 호출하면 객체를 생성함
- 속성과 기능으로 정의됨
    - 클래스의 속성 : 클래스 내부에 정의되는 변수
        - 클래스 변수
        - 객체 변수
    - 클래스의 기능 : 클래스 내부에 정의되는 함수

## 객체와 인스턴스

- 인스턴스 : 클래스로 만든 객체
    - 변수와 인스턴스는 같은 원리로 만들어짐
    - 객체 지향 프로그래밍에서는 변수를 하나의 객체로 취급함
- 인스턴스와 클래스는 다른 메모리 주소를 가진다

## 클래스/인스턴스의 변수와 함수

- 메소드 - 특정 클래스에서만 사용할 수 있는 함수

### 변수

1. 클래스 변수 : `변수명 = 값` 으로 정의 가능
    - 공통 속성을 확인하는 함수
    - 객체와는 무관한 변수로 객체 없이도 참조 가능
    - 공유 변수 ; 모든 객체가 하나의 동일한 클래스 변수를 참조
    - 클래스 자체를 통해서도 접근할 수 있음
    - 클래스 변수는 모든 인스턴스가 공유하는 속성에 사용함
    - 클래스 변수는 인스턴스를 통해서도 접근이 가능 - 파이썬은 객체를 통해서 클래스 변수에 대한 참조가 가능
        
        ```python
        class Car:
          final_num = 0
        
          def __init__(self):
            self.num = Car.final_num #클래스의 변수를 인스턴스의 변수로 상속
            Car.final_num += 1
        ```
        
        ![Untitled](240716%20-%20%E1%84%8F%E1%85%B3%E1%86%AF%E1%84%85%E1%85%A2%E1%84%89%E1%85%B3%20244fefcee43043558df0d715a43977a2/Untitled%203.png)
        
2. 인스턴스(객체) 변수 : `__init __(self)`과 `self`를 이용해서 정의
    - 객체가 없으면 객체 속성 또한 없음. 객체가 생성된 후에 넣을 수 있음
    - 같은 타입이라고 해도 객체들 간에 객체 변수를 서로 공유하지 않음
    - 객체 고유의 변수로 객체 고유 메모리에 생성됨
    - `__init __(self)` ; 생성자(constructor) 함수, 클래스를 통해 인스턴스를 생성하는 순간 내부적으로 한 번만 실행되는 함수

### 함수

1. 클래스 함수 : `self` 없이 정의 ; 클래스에서만 동작하며, 인스턴스에서는 동작하지 않음

```python
class Person2:
	#클래스 변수
	name = '이름'
	age = 0
	
	#클래스 함수
	def introduce1():
		print(f'{Person2.name}, 안녕하세용')
		
		
	#인스턴스 함수
	def introduce2(self):
		print(f'{self.name}, 안녕하세용구링.')
		#인스턴스 변수를 정의하지 않았으므로, 클래스 변수를 가져옴
		#인스턴스 생성 후, 값을 할당할 수 있음(하단 캡쳐 참고)
```

![Untitled](240716%20-%20%E1%84%8F%E1%85%B3%E1%86%AF%E1%84%85%E1%85%A2%E1%84%89%E1%85%B3%20244fefcee43043558df0d715a43977a2/Untitled%204.png)

1. 인스턴스(객체) 함수 : `self`를 이용하여 정의
    - 인스턴스 생성 시 반드시 파라미터를 받아야 하는 경우
        
        ```python
        class Car:
          def __init__(self, name, cc, is_ko, colors):
            self.name = name
            self.cc = cc
            self.is_ko = is_ko
            self.colors = colors
        ```
        
    - 인스턴스 생성 시 파라미터를 입력받지 않는 경우
        
        ```python
        class Car2:
          def __init__(self):
            self.name = '차종'
            self.cc = 1
            self.is_ko = True
            self.colors = [1,2,3]
        ```
        

## 던더메소드(Dunder Method) == 매직 메소드

- Dunder == Double Underscore
- 함수도 매직 메소드 중 하나다!
- 던더 메소드를 사용하면 파이썬에서 기본적으로 제공하는 연산자(예: +, -, *, / )를 오버로딩하여 클래스가 사용자 정의 동작을 수행하도록 만들 수 있
    
    ```python
    class MyClass:
        def __init__(self, x):
            self.x = x
    
        def __str__(self): #인스턴스를 문자열로 표현
            return f"MyClass object with x={self.x}"
    
        def __add__(self, other): # 덧셈 연산자 '+' 오버로딩
          return self.x + other.x
    
    a = MyClass(1)
    print(a)
    str(a)
    
    a_description= a.__str__()
    print(a_description)
    
    b = MyClass(2)
    print(a + b)
    ```
    
- 예시
    - ex. **init** ; 객체가 생성될 때 인터프리터에 의해서 자동적으로 불러짐
- 풍부한 비교(rich comparison)
    
    [3. 데이터 모델](https://docs.python.org/ko/3.11/reference/datamodel.html#object.__eq__)
    
    ```python
    object.__lt__(self, other)
    object.__le__(self, other)
    object.__eq__(self, other)
    object.__ne__(self, other)
    object.__gt__(self, other)
    object.__ge__(self, other)
    ```
    

## 오버라이딩

- 오버라이딩(overriding)은 무시하다, 우선하다라는 뜻을 가지고 있는데 말 그대로 기반 클래스의 메서드를 무시하고 새로운 메서드를 만든다는 뜻입니다.
- 중복되는 기능은 파생 클래스에서 다시 만들지 않고, 기반 클래스의 기능을 사용하면 됩니다. -  메서드 오버라이딩은 원래 기능을 유지하면서 새로운 기능을 덧붙일 때 사용

```python
def greeting(self):
        super().greeting()    # 기반 클래스의 메서드 호출하여 중복을 줄임
```

- 원래 class의 type과 at 메모리 주소를 출력하는 던더메소드를 오버라이딩

## 데코레이터

- @classmethod
    - 클래스 함수 정의 방법 2가지 - 데코레이터 / 클래스 변수 사용(class.변수명)
    
    ```python
    class Car:
      total_cnt = 0
      korean_yn_cnt = 0
      
      def __init__(self):
        self.num = Car.total_cnt #class 변수 상속받음!!!! 입력 필요 없음
        Car.total_cnt += 1
         
         
    	@classmethod #현재 클래스의 변수를 참조
    	#@classmethod라고 적고 , cls를 아규먼트로 넣어서 클래스 함수임을 알려주깅!!!!!
      def car_cnt(cls):
        print(f'등록된 차종은 {cls.total_cnt}대 입니다.')
    
    ```
    
- @staticmethod ; 객체로는 호출하지 못하고 클래스로만 호출 가능함
    
    ```python
    class Car():
    
        final_num = 0
    
        def __init__(self):
            Car.final_num += 1
    
        @classmethod # 현재 클래스의 변수를 참조합니다.
        def check_num(cls):
            return f'누적 판매량: {cls.final_num}개'
    
        @staticmethod #,이 메소드가 만들어진 클래스의 변수를 참조
        def check_num1(cls):
            return f'누적 판매량 : {cls.final_num}개'
    
    a = Car()
    
    a.check_num() #정상 출력
    
    a.check_num() #error
    #TypeError: Car.check_num1() missing 1 required positional argument: 'cls'
    
    ```
    
- @property
    - 함수를 변수처럼 부를 수 있음
    - 함수를 getter로 만들어줌!!!!!!!
    
    ```python
    class BankAccount:
      def __init__(self, _account_num, _name, _balance, _password):
        self._account_num = _account_num
        self._name = _name
        self._balance = _balance
        self._password = _password
    
      @property
      def get_pw(self):
        print(self._password)
    
      def set_pw(self, new_password):
        self._password = new_password
    
      def outer_balacne(self):
        print(self._balance)
        
        
        
    a = BankAccount(1234,'강주란', 30000, '1234')
     
    a.get_pw() #TypeError: 'NoneType' object is not callable
    #함수이지만 변수처럼 호출하므로!!!
    a.get_pw #정상 출력
    
    a.get_pw = '12233' #AttributeError: can't set attribute 'get_pw'
    #getter임. setter가 아니므로 값 변경 불가능
    ```
    
- @(getter함수명).setter
    - 함수를 setter로 만들어 줌!!!!
    
    ```python
    class BankAccount:
      def __init__(self, _account_num, _name, _balance, _password):
        self._account_num = _account_num
        self._name = _name
        self._balance = _balance
        self._password = _password
    
      @property
      def get_pw(self):
        print(self._password)
    
      @get_pw.setter #값을 변경하는 변수처럼 부르는 함수,
      def get_pw(self, new_password):
          self._password = new_password
    
      @property
      def outer_balacne(self):
        print(self._balance)
    ```
    

```
# 은닉성을 약속한 속성에 어떻게 접근을 해야하는가?

```

### etc.

- 객체의 생명주기
    - [https://blog.naver.com/sajkl2/221763145606](https://blog.naver.com/sajkl2/221763145606)
