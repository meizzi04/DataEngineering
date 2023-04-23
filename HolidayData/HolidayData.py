# 라이브러리
import os
import glob
import pandas as pd

# 파일 경로에 .csv 파일 불러오기
path = r'./'
folders = glob.glob(path + "/*.csv")
folders

## holiday data를 읽어서 df로 변경하는 code ##
# 데이터프레임 병합
df_holiday = pd.DataFrame()  # 공휴일 데이터
df_isHolidays = pd.DataFrame()  # 공휴일 여부
df_result = pd.DataFrame()  # 결과

# 공휴일 데이터 읽어오기
for files in folders:
    print(files)
    df = pd.read_csv(files, encoding='cp949')
    df_holiday = pd.concat([df, df_holiday], axis=1)

# 전체 데이터 읽어오기
dt = pd.read_csv('./result/total_data.csv', encoding='cp949')
# 날짜 칼럼만 추출
total_date = dt.iloc[:, [1]]

# 공휴일 데이터 출력
df_holiday.columns = ['date', 'week', 'note']

# 공휴일 여부 확인을 위해 리스트 변환
holidays = df_holiday.date.to_list()
isHolidays = []

# 공휴일 여부 확인
for data in dt.values:
    split_date = data[1].split(" ")[0]
    isHoliday = split_date in holidays
    isHolidays.append(isHoliday)

df_isHolidays = pd.DataFrame(isHolidays)
df_isHolidays.columns = ['isHoliday']

df_result = pd.concat([total_date, df_isHolidays], axis=1)
df_result.columns = ['date', 'isHoliday']

df_result

# csv 파일 저장
df_result.to_csv('./result/result.csv', index=False)
