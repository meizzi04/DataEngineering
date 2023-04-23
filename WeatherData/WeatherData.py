# 라이브러리
import os
import glob
import pandas as pd

# 파일 경로에 .csv 파일 불러오기
path = r'./'
folders = glob.glob(path + "/*.csv")
folders

## weather data를 읽어서 df로 변경하는 code ##
# 데이터프레임 병합
df_weather = pd.DataFrame()

for files in folders:
    print(files)
    df = pd.read_csv(files)
    df_weather = pd.concat([df, df_weather], axis=1)

# 중복 열 제거
df_weather = df_weather.iloc[:8771, :]
df_weather = df_weather.loc[:, ~df_weather.T.duplicated()]

# 컬럼명 변경
df_weather = df_weather.drop(df_weather[[' format: day', 'hour']], axis=1)
df_weather.columns = ['temp', 'humid', 'precip', 'precip_form', 'windspd']

# 결측치 제거
df_weather = df_weather.dropna(axis=0)
df_weather = df_weather.reset_index(drop=True)

# 시간 데이터 생성
# .strftime('%Y-%m-%d-%H %d')
datetime = pd.date_range('2021-01-01', '2022-01-01', freq='H')
dt = pd.DataFrame(datetime)
dt = dt.iloc[:-1, :]
dt.columns = ['datetime']

# 시간 데이터 + 날짜 데이터 병합
df_weather = pd.concat([dt, df_weather], axis=1)
df_weather

df_weather['precip_form'].value_counts()

# csv 파일 저장
df_weather.to_csv('./result/result.csv', index=False)
