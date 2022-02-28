'''
Futures (동시성)
- Futures wait 예제
- Futures as_completed
- 동시 실행 결과 출력
- 동시성 처리 응용 예제 설명
'''
# Chapter-06-05
# 병행성(Concurrency) : 한 컴퓨터가 여러 일을 동시에 수행 -> 단일 프로그램안에서 여러 일을 쉽게 해결할 때 사용
# 병렬성(ParalleLism) : 여러 컴퓨터가 여러 작업을 동시에 수행 -> 속도!

# Futures 동시성

'''
동기? : A라는 작업이 실행 중이면 A가 끝나기전까지 다음인 B작업이 실행 되지 않음
비동기 : A, B, C 등 다양한 작업이 동시 실행가능
'''
# 비동기 작업 실행
# 지연시간(Block) CPU 및 리소스 낭비 방지 -> (File)Network Input/Output 관련 작업 -> 동시성 활용 권장!
# 비동기 작업과 적합한 프로그램일 경우 압도적으로 성능이 향상된다!

# 'futures' package : 비동기 실행을 위한 API를 고수준으로 작성 -> 사용하기 쉽도록 개선
# concurrent.futures
# 1. 멀티스레딩/멀티프로세싱 API가 통일됌 -> 매우 사용하기 쉽다.
# 2. 실행중인 작업 취소, 완료 여부 체크, 타임아웃 옵션, 콜백함수추가, 동기화 코드 매우 쉽게 작성 -> Promise 개념

# 2 가지 패턴 실습
# concurrent.futures map
# concurrent.futures wait, as_completed

# GIL(global interpreter lock) :
# 두 개 이상의 스레드가 동시에 실행 될 때 하나의 자원을 엑세스 하는 경우 -> 문제점(이슈)방지를 위해서
# GIL이 실행된다. 즉, 리소스 전체에 LOCK이 걸린다. + Context Switch(문맥교환)

# GIL을 우회하는 방법
# 멀티 프로세싱 이용, or CPython 이용

# 한시간이나 걸리는 애때문에 남은애들 작업이 지연된다면...? ㄴㄴ
# 반드시 여러개의 작업이 다 성공할거란 보장? ㄴㄴ..
# -> 이러한 세부적인 것들을 세밀하게 조정해줄 수 있어야 한다.


import os
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, wait, as_completed

WORK_LIST = [100000, 1000000, 10000000, 100000000]

# 동시성 합계 계산 메인 함수
# 누적 합계 함수(Generator)

def sum_generator(n):
    return sum(n for n in range(1, n+1))

# wait
# as_completed

def main():
    # Worker Count
    worker = min(10, len(WORK_LIST))

    # 시작 시간
    start_tm = time.time()

    # Futures를 받는 변수 선언
    futures_list = []

    # 결과 건수
    # ThreadPoolExecutor
    # ProcessPoolExecutor
    with ThreadPoolExecutor() as excutor:
        # map -> 작업 순서를 유지하고 즉시 실행한다!
        # result = excutor.map(sum_generator, WORK_LIST)
        for work in WORK_LIST:
            # future 반환.
            future = excutor.submit(sum_generator, work)
            # 스케쥴링
            futures_list.append(future)
            # 스케쥴링 확인
            print('Scheduled for {} : {}'.format(work, future))
            print()

        # ------------------- wait 결과 출력 -------------------
        # result = wait(futures_list, timeout = 3) # wait의 timeout에서 3초까지만 기다리고 나머지작업은 중단
        #
        # # 성공한것만 일단 보기
        # print('Completed Tasks : ' + str(result.done))
        # # 실패한것
        # print('Pending ones after waiting for 3seconds : ' + str(result.not_done))
        #
        # # 결과 값 출력
        # print([future.result() for future in result.done])

        # ------------------- as_completed 결과 출력 -------------------
        for future in as_completed(futures_list):
            result = future.result()
            done = future.done()
            cancelled = future.cancelled

            # future 결과 확인
            print('Future Result : {}, Done : {}'.format(result, done))
            print('Future Cancelled : {}'.format(cancelled))

    # 종료시간
    end_tm = time.time() - start_tm

    # 출력 포맷
    msg = '\n Time : {:.2f}s'
    # 최종 결과 출력
    print(msg.format(end_tm))


# 실행
if __name__ == '__main__':
    main()
