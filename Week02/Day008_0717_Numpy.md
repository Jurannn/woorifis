
# 1. ndarray

## 1) 특징

- numpy의 데이터 타입 중 하나로, 리스트와 비슷한 형식의 구조적 데이터
- 선형대수 연산 가능
- 전체 원소의 type이 같아야 함 → 만약 다른 원소이지만 자신이 포함할 수 있다면, 자료형을 바꿈(자동 형변환)
    
    ```python
    aa = np.array(['15', 25, True]) #모두 str으로 바뀜
    aa
    #array(['15', '25', 'True'], dtype='<U21')
    ```
    
    ```python
    ndarray2 = np.array([1, '가', True, {'가' : '가위'}])
    ndarray2 #dtype=object
    #array([1, '가', True, {'가': '가위'}], dtype=object)
    ```
    
    ```python
    ndarray3 = np.array([1, '가', True, {'가' : '가위'}, [1,2]])
    ndarray3
    #dept가 포함되는 경우 error
    ```
    

## 2) 생성 방법

1. `np.array()` 
    - `np.array(object, dtype=None, *, copy=True, order='K', subok=False, ndmin=0, like=None)`
        - object : array_like (_ _ array _ _ 가 있는 객체)
        - dtype : `float` , `int8` (8bit 이므로 -127 ~ 127만 표현 가능. 첫번째 비트(부호 비트,sign bit)이며, 나머지 비트들 : 절대값 크기(magnitude))
        - 
2. `np.arange(시작점, 끝+1, 스텝)`
    - range와의 차이점 : range는 정수 배열만 생성 가능

## 3) ndarray vs list

![Untitled](240717%20-%20numpy%20beea389f51ee41d7be7d84a5374ef291/Untitled%202.png)

- 파이선 리스트
    - 포인터의 배열로 각각 객체의 메모리가 흩어져 있음
    - 따라서 캐시 활용이 어려움
- np ndarray
    - 타입을 명시하여 원소의 배열로 데이터를 유지하며, 다차원 데이터도 “연속된” 배열로 데이터를 유지

## 4) np.nan, np.inf

### 1. 결측치

1. np.nan의 필요성
    - `None` 의 타입은 NoneType으로 숫자형이 아니다.
    - 따라서, array에 `None`이 있을 경우 dtype = object가 된다. → 자료형이 다르기 때문에 브로드캐스팅 불가능
    
    ```python
    np.array([[1,2,3,4], [5,6,7, None]])
    #array([[1, 2, 3, 4],
    #       [5, 6, 7, None]], dtype=object)
    ```
    
    - ndarray의 요소를 모두 동일하게 맞춰주기 위해, 넘파이에서 숫자형 결측치를 나타내는 `np.nan`을 사용 → 브로드캐스팅 가능!
2. 관련 메소드
    1. `np.nan_to_num(arr, nan = value)` ; arr의 nan값을 value로 채워줌

### 2. np.inf

- infinite을 의미, float

# 2. 주요 메소드

1. `arr.itemsize` : 요소 한 개의 메모리 상의 크기
    1. np.array([1,2,3,128], dtype = 'int8').itemsize == 1
2. `arr.ndim` : 차원
3. `arr.shape` : 구조 - (i, j, k) / (행, 열)
4. `arr.size` : 요소의 개수
5. `arr.strides` : 각 dimensions를 건너가는데 몇 bytes나 뛰어넘어야 하는지에 대한 정보 (다음 요소로 가기 위해 몇 bytes씩 건너 뛰어야 하는 지)
예를들어 [[1,2,3],[4,5,6]] 이라는 2차원의 array가 있다면 strides를 사용하면 (dimensions 간의 간격, 앨리먼트간의 간격) 으로 결과가 출력된다. 각 dimensions 간의 간격은 [1,2,3] 의 용량과 같으므로 4바이트인 int32형 3개 = 12 bytes인 것.
6. `arr.T`  :  전치
7. `arr.cumsum()` :  누적합
8. `arr.var()` : 분산
9. `arr.std()` : 표준편차
10. `arr.argmax(axis=None, …)` : 가장 큰 값이 들어있는 방 번호 (3차원에서는 어케되는거지??)
11. `arr.argmin(axis=None, …)` : 가장 큰 값이 들어있는 방 번호
12. `np.append(arr, values, axis=None)`
    1. 기존 arr의 shape이 깨지고 벡터로 출력됨
    2. 데이터 관련 패키지에서는 원본 보존을 위해 일반 파이썬의 append와 달리 원본을 파괴하지 않음
    3. `axis = 0` (가로축, 행) - 원본과 열 size가 동일해야 함
    `axis = 0` (가로축, 행) - 원본과 행 size가 동일해야 함
        
        ```python
        ndarray2 = np.array([[ 1,  2,  3,  4],[ 5,  6,  7,  8]])
        np.append(ndarray2, [9,10,11,12], axis = 0)
        #ValueError: all the input arrays must have same number of dimensions
        
        np.append(ndarray2, [[9,10,11,12]], axis = 0)
        ```
        
13. `np.sum(arr, axis=None, ..)`
    1. 파이썬 기본 내장 sum과의 차이점
        1. 파이썬 내장 sum :  행 기준으로만 연산 가능
        2. numpy 내장 sum : axis 아규먼트를 통해 열 기준도 연산 가능
14. `np.mean(arr)` : 평균

# 다차원 배열

넘파이가 제공하는 숫자형 자료형은 정수(int), 부호없는 정수(uint), 실수(float), 복소수(complex), 논리(bool)로 총 5가지

# 3. np.random

# 4. 인덱싱/슬라이싱

# 5. 연산

## 1) boolean 연산

## 2) 브로드캐스팅

- universal function → ndarray 원소 전체에 선형대수 연산을 적용(element-wise)
