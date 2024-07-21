
# 1. 시리즈/데이터프레임

## 1) 시리즈

- 1차원 구조를 표현

## 2) 데이터프레임

### 1. 정의 및 특징

1. 엑셀과 같이, 인덱스(index), 변수(column), 값(value)로 이루어진 데이터 구조. 판다스의 특수한 자료형.
2. Series를 묶어 둔 집합
    
    ![Untitled](240718%20-%20pandas%2085b8e603035f4f55b7a92db03cb4acf5/Untitled.png)
    

### 2. 생성 방법(Create)

`pd.DataFrame(**data**=None, index: Axes | None=None, columns: Axes | None=None, dtype: Dtype | None=None, copy: bool | None=None)`

1. `index`  : 행 이름을 지정
2. `columns` : 어떤 컬럼을 가져올 지 명시 (열 이름 지정x)
    
    ![Untitled](240718%20-%20pandas%2085b8e603035f4f55b7a92db03cb4acf5/Untitled%201.png)
    

### 3. 읽기(Read)

1. `df[컬럼명][행이름]`  / `df.컬럼명[행이름]` 
    1. pandas : 열→ 행 순서로 접근 
    2. 같은 자료형끼리 묶어둔 series(1차원)를 여러 개 합쳐둠 (for broadcasting)
    3. 여러 개의 시리즈가 모여서 하나의 데이터프레임이 됩니다.
    4. 따라서 열 → 행 순서로 접근
    5. 기본적으로 열/행의 **“이름”**으로 호출 - 따라서 중복되는 것이 있으면 중복되는 모든 열/행이 출력됨
        1. `df.컬럼명[행이름]` #호출만 가능
        2. `df[컬럼명][행이름]` #호출, 변경 가능
        
        ![Untitled](240718%20-%20pandas%2085b8e603035f4f55b7a92db03cb4acf5/Untitled%202.png)
        
2. `df.loc[행, 열]` / `df.iloc[행, 열]`
    1. `df.loc[행, 열]` : 슬라이싱 시 (시작 : 끝)
        
        ![Untitled](240718%20-%20pandas%2085b8e603035f4f55b7a92db03cb4acf5/Untitled%203.png)
        
    2. `df.iloc[행, 열]` : 슬라이싱 시 (시작 : 끝+1)
        
        ![Untitled](240718%20-%20pandas%2085b8e603035f4f55b7a92db03cb4acf5/Untitled%204.png)
        

### 4. 변경(Update)

1. 컬럼/로우 명 변경
    1. 관련 메소드
        1. `df.index` : 행 이름 return → 활용해서 행 이름 변경 가능
            
            ```python
            #행 이름 변경
            df.index += 1
            df.index = ['하나', '둘', '셋']
            ```
            
        2. `df.columns` : 열 이름 return → 활용해서 열 이름 변경 가능
2. 새로운 column 추가
    1. 일괄로 값을 추가
        1. df[’새로운컬럼명’] = ‘값’
            
            ![Untitled](240718%20-%20pandas%2085b8e603035f4f55b7a92db03cb4acf5/Untitled%205.png)
            
        2. df1[’컬럼명1’] = df2[’컬럼명2’] (주의 ; 인덱스 명이 같은 곳에 붙음)
            
            ```python
            #df의 Name을 data에 붙이는 방법
            #컬럼 명은 달라도 ok
            #index 명이 동일한 곳에 값이 붙음
            data['Name'] = df['Name'] #index 명이 다르면 붙일 수 없음
            data
            
            df.index -= 1
            data['Name2'] = df['Name'] #index 명이 다르면 붙일 수 없음
            data
            ```
            
    2. 한 칼럼에 여러 값을 추가
        
        ```python
        # 1. lambda와 삼항 연산자 활용
        df['Result'] = list(map(lambda x : 'Pass' if x>= 80 else 'Fail', df.Score))
        
        # 2. 리스트 컴프리헨션 + df.apply() 활용
        df['Result'] = df['Score'].apply(lambda x: 'Pass' if x >= 80 else 'Fail')
        
        #2-1 for문 + df.apply() 활용
        def pass_or_fail(row):
            if row >= 80:
                return "Pass"
            else:
                return "Fail"
        df.Result = df.Result.apply(pass_or_fail) 
        
        #3. np.where() 이용
        df_jjang['Result'] = np.where(df_jjang['Score'] >= 80, 'Pass', 'Fail')
        
        #4. bolean indexing
        df.Result[df.Score >= 80] = 'Pass'
        df.Result[~(df.Score >= 80)] = 'Fail'
        ```
        

### 5. 삭제(Delete)

- `del` ; 열 삭제, 원본 변경 O
    
    ![Untitled](240718%20-%20pandas%2085b8e603035f4f55b7a92db03cb4acf5/Untitled%206.png)
    

- `df.drop('row/column명', axis = 0)` ; 원본 변경 X
    - axis = 0 ; 행 삭제
    - axis = 1 ; 열 삭제
    

### 7. 메소드/함수

1. `df.sort_values()`
2. `df.replace()`

### 6. 두 데이터프레임 병합

1. `pd.concat([df1,df2])` : 데이터 프레임을 행/열 기준으로 “단순” 병합
    1. default ; 열 방향 연산, 없는 값이 있으면 자동으로 Null
    2. `join` 
    3. `axis` : axis = 0 ; 행 연산, axis = 1
2. df1.join(df2)
3. pd.merge(df1, df2)

# 2. 형변환

## 1) datetime

## 2) apply

# 3. Grouping Analysis / 데이터 구조화

## 1) df.groupby()

![Untitled](240718%20-%20pandas%2085b8e603035f4f55b7a92db03cb4acf5/Untitled%207.png)

`df.groupby('Class').count()`

`df.groupby("묶음의 기준이 되는 컬럼명")["적용받는 컬럼"].적용받는 연산()`

## 2) pandas.melt()

**`pandas.melt(frame, id_vars=None, value_vars=None, var_name=None, value_name='value', col_level=None, ignore_index=True)`**

![Untitled](240718%20-%20pandas%2085b8e603035f4f55b7a92db03cb4acf5/Untitled%208.png)

## 3) Pivot Table

- 복습
    
    [https://www.kaggle.com/learn/pandas](https://www.kaggle.com/learn/pandas)
    
    [https://www.kaggle.com/code/kimck924/chassis-aistudy-pandas](https://www.kaggle.com/code/kimck924/chassis-aistudy-pandas)
    
    [https://www.kaggle.com/code/kimck924/chassis-aistudy-pandas](https://www.kaggle.com/code/kimck924/chassis-aistudy-pandas)
    

![Untitled](240718%20-%20pandas%2085b8e603035f4f55b7a92db03cb4acf5/Untitled%209.png)
