############################################
# 폴더 생성                                #
# 현재 폴더 아래에 test폴더 생성            #
# test폴더 아래에 날짜_시간 폴더 생성       #
###########################################
# 
# Folder
# ㄴtest
#   ㄴ20240903


import os, datetime

basePath1 = 'test'
os.makedirs(basePath1, exist_ok=False)

# 현재시간 가져오기
now = datetime.datetime.now()

# 폴더명 형식 지정 : "20240904_11"  #연월일시까지만
# folderName = now.strftime("%Y%m%d_")

for hour in range(24):
    folderName = now.strftime("%Y%m%d_")
    folderName = folderName + str(hour)
    forderName = os.path.join(basePath1, folderName)
    os.makedirs(folderName, exist_ok=True)