import threading
import time

# 시작 시간 기록
start_time = time.time()

# 합을 저장할 변수
sum_of_numbers = 0

# 스레드 함수: 주어진 범위의 숫자 합 계산
def calculate_sum(start, end):
    global sum_of_numbers
    temp_sum = 0
    for i in range(start, end + 1):
        temp_sum += i
    sum_of_numbers += temp_sum

# 스레드 1: 1부터 50000000까지 계산
thread1 = threading.Thread(target=calculate_sum, args=(1, 50000000))

# 스레드 2: 50000001부터 100000000까지 계산
thread2 = threading.Thread(target=calculate_sum, args=(50000001, 100000000))

# 스레드 시작
thread1.start()
thread2.start()

# 스레드가 완료될 때까지 대기
thread1.join()
thread2.join()

# 끝 시간 기록
end_time = time.time()

# 실행 시간 계산
execution_time = end_time - start_time

# 결과 출력
print("1부터 100000000까지의 합:", sum_of_numbers)
print("실행 시간:", execution_time, "초")