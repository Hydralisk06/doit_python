# 04 데이터 프레임의 세계로!

# 데이터 프레임 만들기
df_midterm = pd.DataFrame({'english': [90, 80, 60, 70],
                           'math':    [50, 60, 100, 20],
                           'nclass':  [1, 1, 2, 2]})
# 외부 파일 불러오기
# 엑셀 파일 불러오기
df_exam = pd.read_excel('excel_exam.xlsx')
# CSV 파일 불러오기
df_csv_exam = pd.read_csv('exam.csv')
# CSV 파일로 저장하기
df_midterm.to_csv('output_newdata.csv')



# 05 데이터 분석 기초!

#1. 패키지 로드
import pandas as pd
import numpy as np

#2. 데이터 불러오기
mpg = pd.read_csv('mpg.csv')

#3 데이터 파악하기
mpg.head()          # 데이터 앞부분
mpg.tail()          # 데이터 뒷부분
mpg.shape           # 행, 열 수
mpg.info()          # 속성
mpg.describe()      # 요약 통계량

#4. 변수명 바꾸기
mpg = mpg.rename(columns = {'manufacturer' : 'company'}

#5. 파생변수 만들기
mpg['total'] = (mpg['cty'] + mpg['hwy'])/2                      # 변수 조합
mpg['test'] = np.where(mpg['total'] >= 20, 'pass', 'fail')      # 조건문 활용

#6. 빈도 확인하기
count_test = mpg['test'].value_counts()     # 빈도표 만들기
count_test.plot.bar(rot = 0)                # 빈도 막대 그래프 만들기
