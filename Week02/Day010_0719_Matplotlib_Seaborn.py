# 데이터 시각화

## 기본 환경 설정
"""

# 코랩에서 한글 폰트 깨지는 현상 해결을 위해 한국어 폰트들을 설치합니다
!sudo apt-get install -y fonts-nanum # 매직메소드
!sudo fc-cache -fv
!rm ~/.cache/matplotlib -rf
# 이후 런타임 재시작해주세요

"""# 1. Matplotlib

- 파이썬의 대표적인 과학 계산용 그래프 라이브러리
- 판다스에 연계된 시각화 도구
- 논문용으로 많이 쓰임
-  다양한 운영체제와 그래픽 백엔드에서 동작

[Matplotlib](http://matplotlib.org/)

[documentation](http://matplotlib.org/api/pyplot_api.html)

[examples](http://matplotlib.org/gallery.html#statistics)
"""

# %matplotlib inline  # 버전이 낮은 노트북에서 그래프가 바로 뜨지 않을 때 사용 % 쉘메소드

import matplotlib as mpl  # 기본 설정 만지는 용도
import matplotlib.pyplot as plt  # 그래프 그리는 용도
import matplotlib.font_manager as fm # 폰트 관련 용도

# 현재 설치된 폰트 확인해보기
sys_font=fm.findSystemFonts()
print(f"sys_font number: {len(sys_font)}")
print(sys_font)

nanum_font = [f for f in sys_font if 'Nanum' in f]
print(f"nanum_font number: {len(nanum_font)}")

nanum_font

# 시각화도 결국...
import numpy as np

# 한글 폰트 설정
plt.rc('font', family='NanumGothic')
# - 기호 깨짐 현상 방지를 위한 설정
plt.rc('axes', unicode_minus=False)

"""## 1. 도화지 그리기
- 플롯(plot)은 그림(figure)와 축(axes)으로 구성되어 있습니다.
    - plt.figure: 축과 그래픽, 텍스트, 레이블을 표시하는 모든 객체를 포함하는 컨테이너
    - plt.axes: 눈금과 레이블이 있는 테두리 박스로 시각화를 형성하는 플롯 요소 포함
"""

#1. 도화지 만들기
plt.figure() #<Figure size 640x480 with 0 Axes> 기본해상도

#2. 도화지 위에 x축과 y축 얹기
plt.axes()

x = [0, 2, 4, 6, 8]
y = [1, 2, 3, 4, 5]

plt.plot(x, y)

"""## 2. Marker, Linestyle, Color
- marker : https://matplotlib.org/stable/api/markers_api.html
"""

plt.plot(x, y, marker = 'x')

"""- linestyle
    - '-' : solid
    - '--' : dashed
    - '-.' : 'dashdot
    - ':' : dotted
"""

plt.plot(x, y, marker = 'x', linestyle = ':')

plt.plot(x, y, marker = 'x', linestyle = 'dashdot')

"""- Color : https://matplotlib.org/stable/gallery/color/named_colors.html

https://htmlcolorcodes.com/
"""

plt.plot(x, y, marker = 'x', linestyle = ':', color = 'g')

plt.plot(x, y, marker = 'x', linestyle = ':', color = 'green')

plt.plot(x, y, marker = 'x', linestyle = ':', color = '#FFDD31') #hmtl color code 앞에 #을 붙여야함

plt.plot(x, y, '-.xg') #하나의 파라미터 안에 여러 옵션을 넣을수 있음

plt.plot(x, y, 'xg-.') #순서바뀌어도됨

"""- 예시 - np.random.randn(30).cumsum()"""

#왜 색을 구분해서 표현하는지?
#-> plot을 하나의 도화지에 공유해서 그리기 때문에 구분하기 위해

plt.plot(np.random.randn(30).cumsum())
plt.plot(np.random.randn(30).cumsum(), 'gx-.')
plt.plot(np.random.randn(30).cumsum(), 'r--^')
plt.show() #여러개 출력할때
#위 내용까지만 하나의 도화지를 공유하겠당

plt.plot(np.random.randn(30).cumsum())
plt.plot(np.random.randn(30).cumsum(), 'gx-.')
plt.plot(np.random.randn(30).cumsum(), 'r--^')
plt.show()

"""## 3. 축과 레이블

- 축(axis)
"""

plt.plot(np.random.randn(30).cumsum(), 'g-.x')
#plt.axis([-5, 50, -5, 5]) #반시계방향으로 좌 -> 우 -> 하 -> 상

plt.xlim(5,50)
plt.ylim(-5,5)

plt.plot(np.random.randn(30).cumsum(), 'g-.x')
plt.axis('tight') #그래프를 가장 잘 보여줄 수 있게 범위 자동 설정

plt.plot(np.random.randn(30).cumsum(), 'g-.x')
plt.axis('equal') # 시각화된 그래프를 중앙에 그릴 때

"""- 레이블 Label

"""

plt.plot(np.random.randn(30).cumsum(), 'g-.x', label = '2023년')
plt.plot(np.random.randn(30).cumsum(), 'b^-', label = '2023년')
plt.title('연도별 분기별 매출 차이') #그래프 제목
plt.xlabel('분기') #x축 제목
plt.ylabel('매출') #y축 제목
plt.axis('equal')
plt.legend(loc = 'upper right', frameon = False) #범례 + 위치 지정(log = upper right.. left...) #frame on  위치는 고정인데 범례 뒤 음영 제거

"""## 5. 폰트
- 폰트 관리자(Font Manager)를 통해 외부에서 지정 후 사용
"""

set([f.name for f in mpl.font_manager.fontManager.ttflist])

#계속 쓰고 싶은 폰트 규격이 있을 때
font1 = {'family' : 'NanumSquareRound', 'size' : 20, 'color' : 'red'}
font2 = {'family' : 'NanumMyeongjo', 'size' : 14, 'color' : 'green'}

family = 'NanumMyeongjo', size = 14, color = 'green'

plt.plot(np.random.randn(30).cumsum(), 'g-.x', label = '2023년')
plt.plot(np.random.randn(30).cumsum(), 'b^-', label = '2023년')
plt.title('연도별 분기별 매출 차이', fontdict = font1) #그래프 제목
plt.xlabel('분기', family = 'NanumMyeongjo', size = 10, color = 'black', rotation = 60, weight = 'bold')
#x축 제목 #바로 쓸 경우에는 딕셔너리로 전달 x
#rotation ; 각도
# weight ; 강도

plt.ylabel('매출', fontdict = font2, rotation = 70) #y축 제목
plt.axis('equal')
plt.legend(loc = 'upper right', frameon = False)


## Matplotlib로 그린 다양한 그래프 확인

### Line Plots ; 연속형 데이터
"""

x  = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y1 = [1, 3, 5, 3, 1, 3, 5, 3, 1]
y2 = [2, 4, 6, 4, 2, 4, 6, 4, 2]

plt.figure()
plt.plot(x, y1, label = 'line L')
plt.plot(x, y2, label = 'line H')
plt.title('Line Graph Example')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend(loc = 'upper right')
plt.show(); #; 적으면 이미지 위에 설명(글) 안나옴

"""### Bar Plots ; 범주형 데이터"""

import matplotlib.pyplot as plt

# Look at index 4 and 6, which demonstrate overlapping cases.
x1 = [1, 3, 4, 5, 6, 7, 9] #(x1, y1) = (4,2) 의 경우 보이지 않음
y1 = [4, 7, 2, 4, 7, 8, 3]

x2 = [2, 4, 6, 8, 10]
y2 = [5, 6, 2, 6, 2]

# Colors: https://matplotlib.org/api/colors_api.html

plt.bar(x1, y1, label="Blue Bar", color='b')
plt.bar(x2, y2, label="Green Bar", color='g')
plt.plot()

plt.xlabel("bar number")
plt.ylabel("bar height")
plt.title("Bar Chart Example")
plt.legend()
plt.show()

"""### Histograms ; 연속형, 양적 변수
- 연속형 데이터를 특정 구간으로 나누어서 범위에 해당하는 데이터의 빈도수를 막대형태로 표현한 그래프
- 데이터 중심 경향 / 변동성 / 이상치 등을 쉽게 시각적으로 판단 가능
- bin : 구간, 간격
"""

import matplotlib.pyplot as plt
import numpy as np

# Use numpy to generate a bunch of random data in a bell curve around 5.
n = 5 + np.random.randn(1000)

m = [m for m in range(len(n))]
plt.bar(m, n)
plt.title("Raw Data")
plt.show()

plt.hist(n, bins=20) # bins 히스토그램의 구간의 개수
#bins; 20개의 구간으로 나눔
plt.title("Histogram")
plt.show()

plt.hist(n, cumulative=True, bins=20) # cumulative - 누적그래프
plt.title("Cumulative Histogram")
plt.show()

"""### Scatter Plots ; 양적변수 간 관계
- 산점도
- 연속형 변수 간의 관계성 파악 가능
"""

import matplotlib.pyplot as plt

x1 = [2, 3, 4]
y1 = [5, 5, 5]

x2 = [1, 2, 3, 4, 5]
y2 = [2, 3, 2, 3, 4]
y3 = [6, 8, 7, 8, 7]

# Markers: https://matplotlib.org/api/markers_api.html

plt.scatter(x1, y1)
plt.scatter(x2, y2, marker='v', color='r')
plt.scatter(x2, y3, marker='^', color='m')
plt.title('Scatter Plot Example')
plt.show()

"""### Stack Plots
- 누적 분포 그래프
- 연속형(양적) 변수를 여러 개의 시점에서 흐름을 파악할 때 사용
"""

import matplotlib.pyplot as plt

idxes = [ 1,  2,  3,  4,  5,  6,  7,  8,  9]
arr1  = [23, 40, 28, 43,  8, 44, 43, 18, 17]
arr2  = [17, 30, 22, 14, 17, 17, 29, 22, 30]
arr3  = [15, 31, 18, 22, 18, 19, 13, 32, 39]

# Adding legend for stack plots is tricky.
plt.plot([], [], color='r', label = 'D 1')
plt.plot([], [], color='g', label = 'D 2')
plt.plot([], [], color='b', label = 'D 3')

plt.stackplot(idxes, arr1, arr2, arr3, colors= ['r', 'g', 'b'])
plt.title('Stack Plot Example')
plt.legend()
plt.show()

"""### Pie Charts
- 질적 변수(비율이 중요한 변수)에서 비율을 나타내기 위해 사용
- 너무 많거나 비슷한 비율이 있으면 보기 힘듦
- 각 변수 간 기호/이름을 함께 표기해야 눈에 잘 들어옴
"""

import matplotlib.pyplot as plt

labels = 'S1', 'S2', 'S3'
sections = [56, 66, 24]
colors = ['c', 'g', 'y']

plt.pie(sections, labels=labels, colors=colors,
        startangle=120, #s1이 어느 각도에서 시작할지 (반시계방향)
        explode = (0, 0.1, 0), # 틈새
        autopct = '%1.2f%%' # autopercent - 소수점 둘째짜리까지 비율을 계산해 출력해다오
        )

plt.axis('equal') # Try commenting this out.
plt.title('Pie Chart Example')
plt.show()

"""### fill_between and alpha"""

import matplotlib.pyplot as plt
import numpy as np

ys = 200 + np.random.randn(100)
x = [x for x in range(len(ys))]

plt.plot(x, ys, '-')
plt.fill_between(x, ys, 195, where=(ys > 195),facecolor='g', alpha=0.6) # 195, where=(ys > 195) : xlim(195, ~ )와 같은 명령어
#alpha ; 투명도(?)

plt.title("Fills and Alpha Example")
plt.show()

"""### Subplotting using Subplot2grid

- 하나의 도화지를 등분해서 여러 그래프를 그림
"""

import matplotlib.pyplot as plt
import numpy as np

def random_plots():
  xs = []
  ys = []

  for i in range(20):
    x = i
    y = np.random.randint(10)

    xs.append(x)
    ys.append(y)

  return xs, ys

fig = plt.figure() #1. 도화지 그림
#. 도화지 축 1, 2, 3, 4를 그림
#grid ; 웹 서비스에서 하나의 화면을 나누는 박스의 단위ㅈ
#subplot2grid((5칸으로 나눔, 2칸으로 나눔), ())
ax1 = plt.subplot2grid((5, 2), (0, 0), rowspan=1, colspan=2)
ax2 = plt.subplot2grid((5, 2), (1, 0), rowspan=3, colspan=2)
ax3 = plt.subplot2grid((5, 2), (4, 0), rowspan=1, colspan=1)
ax4 = plt.subplot2grid((5, 2), (4, 1), rowspan=1, colspan=1)

x, y = random_plots()
ax1.plot(x, y) #축별로 그래프 그림

x, y = random_plots()
ax2.plot(x, y)

x, y = random_plots()
ax3.plot(x, y)

x, y = random_plots()
ax4.plot(x, y)

plt.tight_layout() #화면에 제일 잘 맞게 출력
plt.show()


"""# 2. Seaborn
- Matplotlib을 기반으로 다양한 색상 테마와 통계용 차트 등의 기능을 추가한 시각화 패키지
- 기본적인 시각화 기능은 Matplotlib 패키지에 의존하며 통계 기능은 Statsmodels 패키지에 의존한다.
- 함수가 쉬우며 직관적으로 결과를 확인할 수 있다.

[Seaborn](http://seaborn.pydata.org)

<img src="https://blog.kakaocdn.net/dn/qxvT2/btqHJixzvms/0WNuSBlA4TEotrDToRuFoK/img.png">

- 출처 : https://wikidocs.net/86290
"""



# Commented out IPython magic to ensure Python compatibility.
# % reset -f



"""## 0) 환경설정"""

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt  # 그래프 그리는 용도
import matplotlib.font_manager as fm  # 폰트 관련 용도
import seaborn as sns
# %matplotlib inline

# 현재 설치된 폰트 확인해보기
sys_font=fm.findSystemFonts()
print(f"sys_font number: {len(sys_font)}")
print(sys_font)

nanum_font = [f for f in sys_font if 'Nanum' in f]
print(f"nanum_font number: {len(nanum_font)}")

# 한글 폰트 설정
plt.rc('font', family='NanumGothic')
# - 기호 깨짐 현상 방지를 위한 설정
plt.rc('axes', unicode_minus=False)

"""## 1) EDA가 필요한 이유"""

df = sns.load_dataset('anscombe')
df

df.info()

df.describe(include='all')

df.dataset.unique()

df[df.dataset == 'I'].describe()

df[df.dataset == 'II'].describe()

df[df.dataset == 'III'].describe()

df[df.dataset == 'IV'].describe()

df[df.dataset == 'I'][['x', 'y']].corr()

df[df.dataset == 'II'][['x', 'y']].corr()

df[df.dataset == 'III'][['x', 'y']].corr()

df[df.dataset == 'IV'][['x', 'y']].corr()

df[['x', 'y']].corr()

# df['dataset'] 가  I ['I', 'II', 'III', 'IV'] df1, df2, df3, df4 에 각각 저장해주세요
# info, describe 등등 확인도 해주세요

"""### I. Seaborn 기본 함수
- 스타일 지정
#### 가. sns.set()
  - 환경변수 설정 함수 : set 함수는 스타일, 팔레트, 글꼴, 글꼴 크기 등 앞으로 그리게 되는 모든 플롯의 그림에 영향을 준다.
  - seaborn.set(context, style, palette, font, font_scale, color_code, rc)

  - Parameter
    - context: 배율조정
    - style: {None, 'darkgrid', 'whitegrid', 'dark', 'white', 'ticks'} 중 하나

  #### 나. set_style
    - 틱스타일만 변경


https://seaborn.pydata.org/tutorial/color_palettes.html

https://seaborn.pydata.org/tutorial/aesthetics.html?highlight=style

## 2) lmplot (Logistic Model Plot)
"""

sns.lmplot(data = df, x = 'x', y = 'y') #44개 데이터 전체를 그려줌

sns.lmplot(data = df, x = 'x', y = 'y', hue = 'dataset') #'컬럼명'기준으로 데이터 색깔 구분해줌
#고유값을 구분해서 색을 입히고 범례도 만들어줌

sns.lmplot(data = df
           ,x = 'x'
           , y = 'y'
           , hue = 'dataset'
           , col = 'dataset')

sns.lmplot(data = df
           ,x = 'x'
           , y = 'y'
           , hue = 'dataset'
           , col = 'dataset'
           , col_wrap = 3) # col_wrap : 한 줄에 몇개의 그래프를 그릴지

sns.lmplot(data = df
           ,x = 'x'
           , y = 'y'
           , hue = 'dataset'
           , col = 'dataset'
           , col_wrap = 3
           , palette = 'dark') #씨본에서 정한 팔래트를 가져옴

sns.lmplot(data = df
           ,x = 'x'
           , y = 'y'
           , hue = 'dataset'
           , col = 'dataset'
           , col_wrap = 3
           , palette = 'dark'
           , ci = None) #신뢰구간

sns.set_theme(style="ticks")
plt.figure(figsize=(20, 20))   # 그래프 크기
sns.lmplot(x="x", #lmplot ; 로지스틱 모델
           y="y",
           col="dataset", # col ; 구분자를 바탕으로 그래프를 여러개 만들어줌
           hue="dataset", # hue : 컬럼명 기준으로 데이터 색깔 구분해줌 -> 생략 시 네 그래프의 색이 모두 똑같이 나옴
           data=df,
           col_wrap=2, # col_wrap : 한 줄에 몇개의 그래프를 그릴지
           ci=None, #신뢰구간(confidence interval)
           palette="muted", #palette: 색상 컨셉 지정
           height=4,
           scatter_kws={"s": 100, "alpha": 0.7}); # scatter_kws : 점의 색깔, 투명도 등 속성 지정
           #s ; 사이즈 , alpha ; 투명도

plt.savefig('lm.png') # 파일로 저장
plt.show() # close()

"""## 3) Barplot
- 범주형 자료에 대한 카운팅, Category나 class에 대한 비교
- 순위형 자료에 대해 카운팅할 때
- 여러 범주형 변수에 대한 Overlay를 확인 가능

http://seaborn.pydata.org/examples/palette_choices.html
"""

import numpy as np
import seaborn as sns

# Generate some sequential data
# 범주형 자료는 수치로 게산 x
x = np.array(list("ABCDEFGHIJ"))
y1 = np.arange(1, 11)

print(x)
print(y1)

sns.barplot(x=x, y=y1, palette="rocket")

sns.barplot(x=x, y=y1, palette="rocket"
            ).axhline(6, color="g") #기준선 ax, hline ; horizonline 가로선(y=6) , color

sns.barplot(x=x, y=y1, palette="rocket"
            ).axvline(6, color="g") #vertical 세로선(x = 6)

# Set up the matplotlib figure
import random
#모델별로 seed를 여러개 심어줘야 하는 경우가 있음
rs = np.random.RandomState(8) #그런 경우 한번에 seed를 계속 불러 쓰기위한 함수를 사용

f, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(7, 5), sharex=True) # 3개의 서브플롯으로 된 도화지를 그리겠다
#sharex ; x축을 공유 -> 적지 않으면 x축이 그래프 개수만큼 표시됨

sns.barplot(x=x, y=y1, palette="rocket", ax=ax1) # ax=ax1 : 첫번째 그래프 의미
ax1.axhline(0, color="k", clip_on=False) # 수평선 그린다
ax1.set_ylabel("Sequential") # 서브플롯일 때 ylabel 지정해주는 옵션
# Center the data to make it diverging
y2 = y1 - 5.5
sns.barplot(x=x, y=y2, palette="vlag", ax=ax2)
ax2.axhline(0, color="k", clip_on=False)
ax2.set_ylabel("Diverging")

# Randomly reorder the data to make it qualitative
y3 = rs.choice(y1, len(y1), replace=False)
sns.barplot(x=x, y=y3, palette="deep", ax=ax3)
ax3.axhline(0, color="k", clip_on=False)
ax3.set_ylabel("Qualitative")

# Finalize the plot
sns.despine(bottom=True) # 축/테두리 제거
plt.setp(f.axes, yticks=[])
plt.tight_layout(h_pad=2)

# Set up the matplotlib figure
import random
#모델별로 seed를 여러개 심어줘야 하는 경우가 있음
rs = np.random.RandomState(8) #그런 경우 한번에 seed를 계속 불러 쓰기위한 함수를 사용

f, (ax1, ax2, ax3, ax4) = plt.subplots(4,1, figsize=(7, 5), sharex=True) # 3개의 서브플롯으로 된 도화지를 그리겠다
#sharex ; x축을 공유 -> 적지 않으면 x축이 그래프 개수만큼 표시됨


ax1 = plt.subplot2grid((3,2), (0, 0), rowspan=1, colspan=2)
ax2 = plt.subplot2grid((3,2), (1, 0), rowspan=1, colspan=2)
ax3 = plt.subplot2grid((3,2), (2, 0), rowspan=1, colspan=1)
ax4 = plt.subplot2grid((3,2), (2, 1), rowspan=1, colspan=1)


sns.barplot(x=x, y=y1, palette="rocket", ax=ax1) # ax=ax1 : 첫번째 그래프 의미
ax1.axhline(0, color="k", clip_on=False) # 수평선 그린다
ax1.set_ylabel("Sequential") # 서브플롯일 때 ylabel 지정해주는 옵션
# Center the data to make it diverging
y2 = y1 - 5.5
sns.barplot(x=x, y=y2, palette="vlag", ax=ax2)
ax2.axhline(0, color="k", clip_on=False)
ax2.set_ylabel("Diverging")

# Randomly reorder the data to make it qualitative
y3 = rs.choice(y1, len(y1), replace=False)
sns.barplot(x=x, y=y3, palette="deep", ax=ax3)
ax3.axhline(0, color="k", clip_on=False)
ax3.set_ylabel("Qualitative")

sns.barplot(x=x, y=y3, palette="deep", ax=ax4)
ax4.axhline(0, color="k", clip_on=False)
ax4.set_ylabel("Qualitative")

# Finalize the plot
sns.despine(bottom=True) # 축/테두리 제거
plt.setp(f.axes, yticks=[])
plt.tight_layout(h_pad=2)

# Set up the matplotlib figure
import random
#모델별로 seed를 여러개 심어줘야 하는 경우가 있음
rs = np.random.RandomState(8) #그런 경우 한번에 seed를 계속 불러 쓰기위한 함수를 사용

f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(7, 5), sharex=True) # 3개의 서브플롯으로 된 도화지를 그리겠다
#two-dimensional array of axes (2x2 in your case), hence you need to set this up as follows:


sns.barplot(x=x, y=y1, palette="rocket", ax=ax1) # ax=ax1 : 첫번째 그래프 의미
ax1.axhline(0, color="k", clip_on=False) # 수평선 그린다
ax1.set_ylabel("Sequential") # 서브플롯일 때 ylabel 지정해주는 옵션
# Center the data to make it diverging
y2 = y1 - 5.5
sns.barplot(x=x, y=y2, palette="vlag", ax=ax2)
ax2.axhline(0, color="k", clip_on=False)
ax2.set_ylabel("Diverging")

# Randomly reorder the data to make it qualitative
y3 = rs.choice(y1, len(y1), replace=False)
sns.barplot(x=x, y=y3, palette="deep", ax=ax3)
ax3.axhline(0, color="k", clip_on=False)
ax3.set_ylabel("Qualitative")

sns.barplot(x=x, y=y3, palette="deep", ax=ax4)
ax4.axhline(0, color="k", clip_on=False)
ax4.set_ylabel("Qualitative")

# Finalize the plot
sns.despine(bottom=True) # 축/테두리 제거
plt.setp(f.axes, yticks=[])
plt.tight_layout(h_pad=2)

"""---

#### 가. 서브플롯 그리기
- 전체도화지, (변수명1, 변수명2) = plt.subplots(세로개수, 가로개수)

- f, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(7, 5), sharex=True)
