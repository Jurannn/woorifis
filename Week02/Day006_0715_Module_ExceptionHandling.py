# -*- coding: utf-8 -*-

#  filter
- 이터러블의 각 요소에 대해 function이 참인 것만 반환하는 요소의 이터레이터

```
filter(function, iterable)
```

li = [1,2,3,4,5,6,7,8,9]
list(filter(lambda i : i%2 == 0, li))

[*filter(lambda i : i%2 == 0, li)]

[*{'a':2, 'b':4, 'c':10}]

def fun(a, b, c):
    print(a, b, c)

def summ(a,b,c):
  print(a+b+c)
# A call with unpacking of dictionary
d = {'a':2, 'b':4, 'c':10}
summ(**d)

"""# Enumerate & Zip
- Enumerate(열거하다)
    - 리스트의 요소를 추출할 때 번호를 붙여서 추출
```
enumerate(변수명)
```

- Zip (잠그다)
    - 두개의 리스트를 병렬적으로 추출함
```
zip(list, list)
```
"""

li = [i for i in range(31)]

enumerate(li) #(인덱스 번호, 리스트 원소)

list1 = ['사과', '바나나', '딸기', '포도', '키위']
[*enumerate(list1)]

for idx, element in enumerate(list1):
  print(idx, element)

"""- Zip (잠그다)
    - 두개 이상의 리스트를 병렬적으로 추출함
```
zip(list, list)
```
"""

alist = ['사과', '바나나', '딸기', '오렌지']
blist = ['Apple', 'Banana', 'Strawberry']
clist = [100, 200, 300, 400, 500]

[*zip(alist, blist, clist)]

for i, j in enumerate(zip(alist, blist)):
  print(i,j)

alist = ['사과', '바나나', '딸기', '오렌지']
blist = ['Apple', 'Banana', 'Strawberry']
clist = [100, 200, 300, 400, 500]

for i, j in enumerate(zip(alist, blist)):
  print(i,j[0], j[1])


"""# Reduce

- reduce는 반복 가능한 객체의 각 요소를 지정된 함수로 처리한 뒤 이전 결과와 **누적해서 반환**
- functools 모듈에서 reduce 함수를 가져와야 함
```
reduce(function, iterable, initializer=None)
```
"""

from functools import reduce

array2dim = [[x]*x for x in range(5)] # [x]
array2dim

reduce(lambda x, y : x+y, array2dim) #평탄화

# [[], [1], [2, 2], [3, 3, 3], [4, 4, 4, 4]]
# []   [1]
# x    y
# x  +  y
        # [1]   [2, 2]
        # x    +  y
        # [1, 2, 2]  + [3, 3, 3]
            #   x    +     y
                #  x            +      y
            #   [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]


test2 = [{'name' : 'a', 'age' : 1}, {'name' : 'b', 'age' : 2}, {'name' : 'c', 'age' : 3}]

xx = {'name' : 'a', 'age' : 1}
yy = {'name' : 'b', 'age' : 2}

{'name' : 'a', 'age' : 1}['age']

reduce(lambda x, y : x+y['age'] , test2, 0) / len(test2) # 첫번째 x를 초기값 0 으로 설정
# 0 + test2[0]['age'] 1
#        1                 +   test2[1]['age']    2
#                           3                           +  test2[2]]['age'] 3



# 모듈
- 이미 만들어진 파이썬 소스파일(라이브러리)
    - 파이썬은 모듈을 만들기 위한 추가 과정은 필요하지 않습니다.
    - 파이썬 소스파일은 모듈로 사용할 수 있습니다.
    - 재사용성을 위해서 그렇게 쓰고요


from math1 import 덧셈
from google.colab import drive

drive.mount('/content/drive')

# Commented out IPython magic to ensure Python compatibility.
# %%writefile test.py
# 
# def final(yay):
#   print('와 여깄구나! 하하하')
# 
# PI = 3.1423904029385902380598304923904

final(haha)

import test #파일 명 == 모둘 명

test.PI

test.final(1)

!pip install selenium #python index package

# Commented out IPython magic to ensure Python compatibility.
# %%writefile test_library/test1.py
# 
# def final_from_test1(yay):
#   print('test1.py에 있는 함수입니다.')
# 
# PI = 3.14

# Commented out IPython magic to ensure Python compatibility.
# %%writefile test_library/test2.py
# 
# def final_from_test2(yay):
#   print('test2.py에 있는 함수입니다.')
# 
# PI = 3.1423904029385902380598304923904

# .으로 파일 혹은 폴더를 구분

#방법1
import test_library.test2 #직접 불러오고

test_library.test2.final_from_test2('안녕') #모듈을 길게 작성하는 방법

#방법2
import test_library.test1 as tlt1 #imort 라이브러리명 as 별칭
#import numpy as np

tlt1.final_from_test1('안녕')



#방법3
from test_library.test1 import * #*은 0개 이상의 모든 것
#test_libarary의 test1에서 모든 것을 가져올거야

final_from_test1('hi~~') #라이블더리 명을 쓰지 않고 함수와 변수를 사용 가능
PI

# Commented out IPython magic to ensure Python compatibility.
# #이미 모듈 불러와놓고 원본을 재수정 => 메모리에 이미 올라가있기 때문에
# #코드를 실행해도 이전 라이브러리가 실행됨
# #파일은 덮어써지지만 불러올때는 덮어쓴 파일을 불러오지 못함
# #===> 해결법 ; 런타임 다시 시작
# 
# %%writefile test_library/test2.py
# 
# def final_from_test2(yay):
#   print('test2.py에 있는 함수입니다.')
# 
# PI = '3.14어쩌궁'

#방법4
from test_library.test2 import final_from_test2 #라이브러리에서 필요한 함수만 가져옴

final_from_test2('hi~~')

PI

"""# 모듈은 어디서 가져오는지??
    - 파이썬 소스파일에서 가져옵니다
    - 근데 어디있다고 알려는 줘야 합니다.
    - 그래서 모듈은 위치를 미리 지정해놓습니다.
    - 모듈은 항상 그 위치에서 가져오도록 만들어 놓습니다.
"""

import copy # 경로가 없는데 불러와짐 -> 어디서 가져오는걸까?
#파이썬 설치된 환경 변수 안에 있는 폴더를 순서대로 돌면서 모듈을 읽어옴

import sys #시스템과 관련된 모듈

sys.path

# Commented out IPython magic to ensure Python compatibility.
# %%writefile copy.py
# 
# def hello():
#   print('how are you?')

import copy

copy.hello() #module 'copy' has no attribute 'hello'

# Commented out IPython magic to ensure Python compatibility.
# %%writefile functools.py
# 
# def hello():
#   print('how are you?')

import functools

functools.hello()

#우리가 만든 모듈 명은 기존에 있는 많이 사용하는 패키지 및 모듈 명과 이름이 겹치지 않도록 작성하기
#왜냐하면 sys.path(환경변수)에 등록된 0번 방부터 해당 파일을 찾는데
#list형식으로 관리되기 때문에 앞에서 True이면 (앞 폴더 안에서 해당 파일을 찾고 나면)
#뒤 경로를 확인하지 않음 -> 자주 쓰는 라이브러리를 사용할 수 없게 됨

#모듈을 불러올때는 모듈별칭명.변수 / 모듈별칭명.함수() 정도로 사용

!pwd # print working directory #코랩(리눅스)에서

from google.colab import drive
drive.mount('/content/drive')

#cd #윈도우에서

# Commented out IPython magic to ensure Python compatibility.
# %%writefile /content/drive/MyDrive/package/hello_bye.py
# 
# def hello():
# 	print('how are you?')

# Commented out IPython magic to ensure Python compatibility.
# %%writefile /content/drive/MyDrive/ITStudy/math1.py
# 
# def add(x, y):
#     return x+y
# 
# def minus(x, y):
#     return x-y
# 
# PI = 3.14
# 
# # package 폴더 안에 math1.py를 만드시고 add(x, y), minus(x, y), PI=3.14
#

# 모듈명 as 별명
#  별명.함수()

 # from 라이브러리명 import 모듈명
# 모듈명.함수

# from 라이브러명.모듈명 import 쓰려는함수명만
# 쓰려는함수명만

# from 라이브러명.모듈명 import *
# 함수

!pwd

#전체 경로로 불러오기
#모듈 부를 때 py 확장자 사용하지 않음
import drive.MyDrive.ITStudy.math1
drive.MyDrive.ITStudy.math1.PI

# from 라이브러리명 import 모듈명
import drive.MyDrive.ITStudy.math1 as math2
math2.PI

# from 라이브러명.모듈명 import 쓰려는함수명만
from drive.MyDrive.ITStudy.math1 import add
add(1,3)

# from 라이브러명.모듈명 import *
from drive.MyDrive.ITStudy.math1 import *
minus(4, 2)

"""새로운 경로를 path 에 추가
- colab에서 사용할 수 있는 모듈, 패키지를 가져오는 방법
- 가져오고 싶은 모듈이 들어있는 폴더 경로를 추가해주면 됩니다
    - 파일 경로가 아닙니다
    - 파일이 들어있는 폴더의 경로입니다
"""

import sys # system 관련된 여러 설정들을 제어해주는 파이썬의 모듈

sys.path

#경로 추가
sys.path.append('/content/drive/MyDrive/ITStudy')

sys.path
#시스템 변수 안에 있는 경로들은 경로를 입력하지 않아도 바로 특정 파일을 접근할 수 있음

"""# 패키지

    - 모듈(여러개 파일)을 하나로 묶어서 관리하는 것
    - 파이썬 패키지는 폴더로 관리
    - 같은 폴더에 있으면 패키지가 됩니다
    - 패키지의 이름은 폴더의 이름이 됩니다.

- 버전에 따라서 폴더를 패키지로 인식할 수도 있고 인식하지 않을 수도 있습니다. (3 이하 버전)
    - 혹시 몰라서 호환용으로
    - __init__.py 가 들어있으면 패키지로 파이썬이 인식을 합니다.
    - 파일의 내용은 없어도 됩니다.
"""

# Commented out IPython magic to ensure Python compatibility.
# %%writefile 파일명
# 
# 
# def multiply(x, y):
#     return x*y
# 
# def divide(x, y):
#     return x/y
# 
# PI = 3.14
#

"""# 파이썬 소스파일의 실행

- 파이썬 인터프리터는 모듈도 따로 뭔가 할필요 없이 py이기만 하면 되고, 일반 실행파일도 py이기만 하면 됩니다.
- 그럼 이 둘을 구분할 필요가 있지 않을까요??

- 그래서 파이썬소스파일을 직접 실행하면
- 참조해서 실행할 때랑 자신을 직접 실행할 때랑 구분하는 방법이 있습니다.

    1. 자신이 직접 실행할때
        __name__ == "__main__"

    2. 모듈로 쓰여서 실행할때
        __name__ == 모듈명

출력됩니다

"""

import numpy as np

npli = np.array([1,2,3,4,5]) #numpy.py의 array()라는 함수를 통해 만들어진 객체

li = [1,2,3,4,5]

type(npli)

# if __name__ == "__main__":
    # 조건문

dir(npli)

type(li)

"""## 실습. modules 패키지 안에 만들어 주시고   my_area2라는 모듈을 새로 만들어주세요.

그 안에는

 triangle_area() (삼각형 넓이)
 squre_area2() (직사각형 넓이)

 를 구하는 함수를 넣어주세요.
"""

# my_area2
# ma2 라는 모듈명으로 불러와주세요
# triangle_area()

from modules.my_area2 import *   # 해당 모듈 안에 있는 함수를 다 가져옵니다

# Commented out IPython magic to ensure Python compatibility.
# %%writefile /content/drive/MyDrive/package/modules/copy.py
# 
# def triangle_area():
#     a = int(input('가로: '))
#     b = int(input('세로: '))
#     return a * b * 1/2
# 
# def square_area():
#     a = int(input('가로: '))
#     b = int(input('세로: '))
#     return a * b

# 예외처리

예외(exception)란?
- 일반적으로 오류 혹은 에러 라고 불리웁니다.
- 프로그램 실행 중에 예외가 발생하면 '비정상종료'가 되는데요
- 비정상 종료를 막기 위해서 에러(예외)가 발생된 이후의 문장은 정상적으로 수행하도록 처리하는 방법을 우리는 예외처리 라고 부릅니다.


```
try:
    예외가 발생할 가능성이 있는 코드
except:
    예외가 발생할 때 실행할 코드
except:
    예외가 발생할 때 실행할 코드
except:
    예외가 발생할 때 실행할 코드
else:
    잘 실행되면 실행할 코드
finally:
    되든 안되든 반드시 실행할 코드
```


import traceback # 에러메시지를 출력해주는 모듈입니다
#실제로 보는 에러메시지 - 몇번째 줄에서 에러가 발생헀는지 .. 등등

def convert(a):
    if a.isdigit():
        return int(a[::-1])

try:
    print(convert(54321))
    print(convert('abcd'))
except:
    traceback.print_exc()

def convert(string):
  try:
    return int(string[::-1])

  except ValueError:
    print('문자가 아닌 숫자를 입력하세요.')

try:
  print(convert(가))

except NameError:
    print('존재하지 않는 변수입니다.')

except KeyboardInterrupt:
  print('값을 입력하지 않았습니다.')

if True :  #인터프리터 실행 전

try: # 에러가 나는지 감시
    num = input('0 이상의 정수 입력:')

    num = int(num)

    if ininstance(num, int) >= 0:
        print('참')
    else:
        print('다시 입력하세요')

except:
    print('뭔지 모를 에러 발생')

a = input()  #TypeError가 아니라 ValueError 발생
int(a)

try: # 에러가 나는지 감시
    num = input('0 이상의 정수 입력:')
    if int(num) >= 0:
        print('참')
    else:
        print('다시 입력하세요')

except TypeError:
  print('타입 에러 발생')
except Exception:
  print('Exception 예외')
except BaseException:
  print('BaseException 에러')

else: #except가 실행되지 않았을 때 동작됨
  print('try문이 성공적으로 에러없이 완료되었습니다.')

finally:
  print('try구문의 성공/실패와 관계 없이 동작')

#예외를 여러 가지로 나누어서 처리할 경우, 하위 예외 -> 상위 예외 순으로 작성함
#상위 예외를 먼저 작성하면 하위 예외는 동작하지 않기 때문
except BaseException as e: #상위 개념이면 먼저 실행 - e는 대신 하위 개념이 뜸
  print('BaseException 에러', e)
except TypeError as e:
  print('타입 에러 발생', e)
except Exception as e:
  print('Exception 예외', e)
except ValueError as e:
  print('value 에러', e)


else: #except가 실행되지 않았을 때 동작됨
  print('try문이 성공적으로 에러없이 완료되었습니다.')

finally:
  print('try구문의 성공/실패와 관계 없이 동작')


### 연산자
#### 1. 산술연산자 ; +, -, *, /, //, %
#### 2. 대입연산자 ; =, += ,
#### 3. 비교연산자 ; ==, >=, =<, !=
- 비교연산자는 양 변의 값을 비교하는 연산자이며 결과는 true와 false로 나오게 됩니다. 값을 비교하는 연산자 이므로 문자열은 비교할 수 없습니다.

- == ; 동일성 비교 -> 값, 자료형 확인 (숫자는 같은 자료형으로 봄)
- 숫자 자료형 ; 정수, 실수, boolean

#### 4. 논리연산자 ; and or not
#### 5. 비트연산자; & | ~ ^ << >>

#### 6. 연산자 우선순위
산술연산자 -> 비트연산자 -> 비교연산자 -> 논리연산자


0 == False

'' == False

None == False


"""# 예외를 응용하는 경우

- EOF 예외처리를 합니다.
    - EOL : End of Line (\n)
    - EOF : End Of File
        - 파일의 가장 마지막에 들어가는 문자
        - 입력이 끝을 표현하는 경우

    - 파이썬은 EOF을 처리하지 못합니다.
        - 언어의 끝을 예외로 처리합니다.

    - 종료를 의미하는 단축키
        - 윈 : ctrl + z
        - 리눅스, 맥 : ctrl + d

"""

#파일이 강제로 끝나도록 에러 발생
while True:
  try:
    read = input('c:\>')
    print(read)

  except EOFError:
    print('실행이 강제 종료되었습니다.')
    break

type(None)

type(False)

''==False

#keyboard interrupt

while True:
  try :
    read = input('c:w>')
    print(read)
  except KeyboardInterrupt as e:
    print('실행이 강제 종료1', e)
    break
  except EOFError as e :
    print('실행이 강제 종료2', e)
    break


while True:
  read = input('c:\>')
  if read != 'x':
    print(read)
  else:
    raise EOFError #error아닌데 에러 강제 발생

#error 함수
dir(ZeroDivisionError)

ZeroDivisionError.mro() #최하위 클래스 ---- > 최상위 클래스 순으로 출력
#[ZeroDivisionError, ArithmeticError, Exception, BaseException, object]

"""실습1. 아래 코드에서 발생할 예외를 예측하고, try, except 구문으로 해당 예외를 처리해주세요.
```
alist = ["a", "1", "c"]
blist = ["b", "2", "d"]
for a, b in enumerate(zip(alist, blist)): print(b[a])
```
"""


# 표준 출력
- print() 는 파이썬의 표준 출력 함수입니다.
    - 표준 출력 장비(모니터)로 출력을 보내주는 함수를 의미합니다.

```
 print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
```

텍스트 데이터인 경우
- # w : 쓰기 모드, r: 읽기 모드, a: 추가 모드
w ; 새로 쓰기, 있으면 덮어쓰기


바이너리 데이터인 경우(인코딩/디코딩 과정 없음)
-  # wb : 쓰기 모드, rb: 읽기 모드, ab: 추가 모드


# 방법1.
# with open(파일명, 모드) as 파일을 가리키는 약어:
#    print(뭘 쓰려는지, file=약어)
# - with문이 끝나면 자동으로 파일이 닫힘


with open('textex.txt', 'w') as f:
  f.write('안녕하세용')
  f.write('두번째 줄 이에용')

with open('textex.txt', 'w') as f:
  f.write('안녕하세용\n')
  f.write('두번째 줄 이에용\n')

with open('textex.txt', 'a') as f:
  f.write('안녕하세용\n')
  f.write('두번째 줄 이에용\n')

# 방법 2
# 1. 파일을 만들어야 합니다
# 2. 파일을 열어야 합니다
# 3. 사용할 방법(모드)을 지정해야 합니다 (r, w, a)
# 4. 파일을 닫습니다.

f2 = open('textex2.txt', 'w')

f2.write('안녕하세용\n')
f2.write('두번째 줄 이에용\n') #파일을 닫지 않으면 저장되지 않음

f2.close()

f2 = open('textex2.txt', 'w')

f2.write('안녕하세용\n')
f2.write('두번째 줄 이에용\n') #파일을 닫지 않으면 저장되지 않음

f2 #<_io.TextIOWrapper name='textex2.txt' mode='w' encoding='UTF-8'>
#TextInputOutput

f2.close()

print()
'''
print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

Prints the values to a stream, or to sys.stdout by default.
Optional keyword arguments:
file:  a file-like object (stream); defaults to the current sys.stdout.
sep:   string inserted between values, default a space.
end:   string appended after the last value, default a newline.
flush: whether to forcibly flush the stream.
'''
#stdout ; standard out ; 표준출력

f3 = open('textex3.txt', 'w')
print('testex3.txt에 넣어주세용', file = f3) #안닫으면 안보임
f3.close()

f4 = open('textex4.txt', 'w')
print('testex4.txt에 넣어주세용', file = f4, flush = True) #안닫아도 보임

f4.close()

#코드는 메모리 안에 있음
#file은 하드디스크에서 저장

#'r'객체에서 쓸 수 있는 메서드/변수 확인
r = open('textex.txt', 'r')
dir(r)

'''
 'read',
 'readable',
 'readline',
 'readlines',
'''
with open('textex.txt', 'r') as f:
  print(f.read()) #한꺼번에 전체 string 객체를 return

with open('textex.txt', 'r') as f:
  print(f.readable()) #값이 있으면 True

with open('textex.txt', 'r') as f :
  print(f.readline()) #한줄씩 \n단위로 text 데이터를 꺼내옴

with open('textex.txt', 'r') as f :
  print(f.readline())
  print(f.readline())
  print(f.readline())
  print(f.readline())
  print(f.readline())

with open('textex.txt', 'r') as f :
  while f.readline():
    print(f.readline())

with open('textex.txt', 'r') as r:
    # r.readline() # 한줄씩 \n 단위로 텍스트 데이터를 꺼내옵니다.
    while True:
        t = r.readline()
        if not t:
            break
        print(t, end = '')

with open('textex.txt', 'r') as r:
    # r.readline() # 한줄씩 \n 단위로 텍스트 데이터를 꺼내옵니다.
    while True:
        t = r.readline()
        if not t:
            break
        print(t)

with open('textex.txt', 'r') as f:
  print(f.readlines())

with open('textex.txt', 'r') as r: # read 의 앞글자
    # r.readlines() # 전체 데이터를 \n 단위로 끊어서 리스트로 출력합니다.
    for r in r.readlines():
        print(r) # 전체 데이터를 \n 단위로 끊어서 리스트로 출력합니다.

#파일이 있으면 그 파일의 내용을 모두 출력
#파일이 없으면 새로운 파일을 작성해서 '새 파일

#파일을 다 쓰고 나서 close()로 닫아주기

try:
  #파일이 있으면 그 파일의 내용을 모두 출력
  f = open('새파일.txt', 'r')
  print(f.read())
  f.close()

except FileNotFoundError:
    w = open('새파일.txt', 'w')
    w.write('새파일이에용')
    w.close()

except:
    print('그 외의 문제가 발생했습니다.')

try:
  f = open('새파일.txt', 'r')

except FileNotFoundError:
  f = open('새파일.txt', 'w')
  f.write('새파일이에용')

except:
  print('그 외의 문제가 발생했습니다.')

else : #파일이 있으면 그 파일의 내용을 모두 출력
  print(f.read())
  #else절은 예외가 발생하지 않아 except 절을 실행하지 않았을 경우 실행되는 절

finally :
  f.close()
