## 멀티 프로세스 안됨 ㅎ



import multiprocessing
import time

# 시작 시간 기록
start_time = time.time()

# 프로세스 함수: 주어진 범위의 숫자 합 계산
def calculate_sum(start, end, result_queue):
    temp_sum = 0
    for i in range(start, end + 1):
        temp_sum += i
    result_queue.put(temp_sum)  # 계산 결과를 큐에 저장

# 멀티프로세싱 큐 생성
result_queue = multiprocessing.Queue()

# 프로세스 1: 1부터 50000000까지 계산
process1 = multiprocessing.Process(target=calculate_sum, args=(1, 50000000, result_queue))

# 프로세스 2: 50000001부터 100000000까지 계산
process2 = multiprocessing.Process(target=calculate_sum, args=(50000001, 100000000, result_queue))

# 프로세스 시작
process1.start()
process2.start()

# 프로세스가 완료될 때까지 대기
process1.join()
process2.join()

# 계산 결과를 큐에서 가져오기
sum_part1 = result_queue.get()
sum_part2 = result_queue.get()

# 두 부분의 합 계산
sum_of_numbers = sum_part1 + sum_part2

# 끝 시간 기록
end_time = time.time()

# 실행 시간 계산
execution_time = end_time - start_time

# 결과 출력
print("1부터 100000000까지의 합:", sum_of_numbers)
print("실행 시간:", execution_time, "초")