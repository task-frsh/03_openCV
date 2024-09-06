import time

# 시작 시간 기록
start_time = time.time()

# 1부터 100000000까지의 합 계산
sum_of_numbers = sum(range(1, 100000001))

# 끝 시간 기록
end_time = time.time()

# 실행 시간 계산
execution_time = end_time - start_time

# 결과 출력
print("1부터 100000000까지의 합:", sum_of_numbers)
print("실행 시간:", execution_time, "초")