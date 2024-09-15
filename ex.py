import requests


request_url = "http://apis.data.go.kr/1741000/RegistrationPopulationByRegion/getRegistrationPopulationByRegion"
service_key = "jLUlozKiUVHszxwTnnHRjnn0pAeC8NF5dr06kS1hIwGyPFoq6OuwxSHXVYp1OBFta3InpZwkEEbP0NCQMLltLg=="  


params = {
    "serviceKey": service_key,  
    "pageNo": 1,  
    "numOfRows": 10,  
    "type": "json" 
}


response = requests.get(request_url, params=params)


if response.status_code == 200:
    data = response.json() 
    print(data)
else:
    print(f"API 요청 실패: {response.status_code}")