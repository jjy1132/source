#명령 프롬포트에서 pip install openpyxl를 설치
from openpyxl import load_workbook
import pandas as pd

#엑셀파일 경로를 설정하고 데이터만 가져오도록 설정
load_wb = load_workbook("C:/source/test/grade_card.xlsx",data_only=True)

#엑셀파일의 여러 시트중 하나를 선택
load_ws = load_wb['Sheet1']

all_values = []

#가져온 데이터를 리스트로 만듬
for row in load_ws.rows:
    row_value = []
    for cell in row:
        row_value.append(cell.value)
    all_values.append(row_value)

#가져온 데이터중 컬럼명 부분을 제거
del all_values[0]

#리스트형으로 출력하기 위해 리스트 선언 및 총합과 평균값 선언 및 초기화
total_avg = []
total = 0
avg = 0

#국어, 영어, 수학 과목 총합과 평균 구하기
for each_value in all_values:
    for value in each_value[2:]:
        total += int(value) #데이터형식이 문자열로 되어있으므로 int로 형 변환
    avg = round(total/3,2) # 소숫점 2자리까지만 나오도록 반올림
    total_avg = [each_value[0],each_value[1],total,avg]
    
    #print(total_avg)
    
#한 명당 총합과 평균값을 구하고 초기화
    #total = 0

total_avg = pd.DataFrame(total_avg)
total_avg.to_excel(excel_writer='test.xlsx')
