## 1. 사실(Facts)
- 파이썬 제어문, 반복문

## 2. 발견(Discovery)
1. match-case 문
```python
match 변수(값):
  case 값 :
    실행문
  case 값 :
    실행문
  case _ :
    실행문
```

2. 기호의 의미
    1. _ : 와일드카드, 앞 조건을 제외한 모든 것을 포함
    2. \* : 앞의 값을 제외하고 나머지 요소들을 모두 저장
    3. | : OR을 의미

3. 삼항 연산자
    1. 결과 = '조건이 참일 때 값' if '조건식' else '조건이 거짓일 때 값'
  

4. 연산자 우선순위
    1. 사칙연산 > 비트 연산자 > 비교 연산자 > 논리 연산자 > 삼항 연산자(조건식) > 대입 연산자
    2. 연산자 우선 순위에 따라서, if ans == '피자' or '햄버거' 는 (ans) == ('피자' or '햄버거')와 동일하다
        

5. 비트 연산자 vs 논리 연산자
     1. 파이썬에서 논리 연산자 사용하기.
     2. 비트 연산자 : 연산 대상을 비트(bit)로 변환한 후 연산 수행
          - 1|2|3의 비트 연산 : (1|2)|3 == 0001|0010|3 => 0011|3 =>  0011|0011 => 0011 => 3 return
          - 1 or 2 or 3의 논리 연산 : 1 return (by circuit evaluation)
       
            
6. short-circuit evalution(단락 평가)
       1. 1 or 2 or 3 #True or ... 이므로 1을 return
       2. 0 or 2 or 3 #False or True .. 이므로 2를 return

7. flag 변수
     1. 깃발을 올리고 내리듯이 참과 거짓으로 무엇인가를 판단할 때 사용할 수 있는 변수
```python
flag = True
while flag :
  print('True')
else :
  print('false)
```

8. 딕셔너리 - iterable ==> for문에 사용 가능~~~!! (key 중심)
```python
#딕셔너리도 iterable!! __iter__
for fruit in fruits:
  print(fruit) #key를 출력!!
  
  
#value만 출력
for fruit in fruits:
  print(fruits[fruit])

#key-value
for key, value in fruits.items():
  print(key + ' - ' + value)
#
 ```

9. while문의 continue
```python
#아래 코드는 무한반복과 동일

n = 1
while n <= 10:
  if n % 2 == 0:
    print(n)
  else :
    continue #만나면 한 번만 넘어감
  i += 1
```

```python
n = 1
while n <= 10:
  i += 1
  if n % 2 == 0:
    continue
  print(i)
```

10. 바다코끼리 연산자
```python
cnt, output = 0, 0
while (cnt := cnt + 1) < 20:
  #:=는 바다 코끼리 연산자, 값을 할당 하면서 동시에 사용하는 연산자
  output += cnt if cnt % 3 == 0 else 0
print(output)
```

## 3. 배운점(Lesson Learned)
1. 라인 순서에 따라 값이 크게 달라지는 것을 보며 파이썬은 인터프리터 언어임을 다시 한 번 되새길 수 있었다.
2. 연산자 우선순위가 단순히 이론적인 지식에만 중요하다고 생각했는데, 실제 코드를 작성할 때 생각보다 많이 쓰이는 것을 보고 연산자 우선순위를 잘 지켜야 겠다고 생각했다.



## 4.  선언(Daclaration)
1. 파이썬이 인터프리터 언어임을 명확하게 인지하겠다.
2. 연산자 우선순위 또한 명확하게 인지하겠다.
3. 조건문 작성 시 조건에 빠짐이 없는지 확인해야겠다.
4. 반복문 작성 시 반복 횟수 조절하는 변수를 잘 할당해야겠다.
