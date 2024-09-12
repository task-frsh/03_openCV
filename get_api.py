import requests
import pandas as pd
import ms_api

# API Key
apikey = ms_api.pd_apikey
# API 엔드포인트
url = 'https://apis.data.go.kr/1741000/RegistrationPopulationByRegion/getRegistrationPopulationByRegion?ServiceKey=jLUlozKiUVHszxwTnnHRjnn0pAeC8NF5dr06kS1hIwGyPFoq6OuwxSHXVYp1OBFta3InpZwkEEbP0NCQMLltLg%3D%3D&pageNo=1&numOfRows=100' 

# 요청 매개변수
params = {
    'ServiceKey': apikey,
    'pageNo': '1',  # 조회할 데이터 개수 설정
    'numOfRows': '10'       # 페이지 번호 설정
}

# API 요청
response = requests.get(url, params=params)

# 응답 확인
if response.status_code == 200:
    # XML 데이터 파싱
    data = response.text
    df = pd.read_xml(data)
    print(df)

else:
    print("Error:", response.status_code)