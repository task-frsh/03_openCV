
# Folder
# ㄴtest
#   ㄴ20240904_11
#   ㄴ20240904_12...


import os
import datetime

basePath1 = 'test'
os.makedirs(basePath1, exist_ok=True)

# 현재시간 가져오기
now = datetime.datetime.now()

# 폴더명 형식 지정 : "20240904_11"  #연월일시까지만
# folderName = now.strftime("%Y%m%d_")

for hour in range(24):
    folderName = now.strftime("%Y%m%d_")
    folderName += str(hour).zfill(2) # hour를 두자리 숫자로 변환
    folderName = os.path.join(basePath1, folderName)
    os.makedirs(folderName, exist_ok=True)