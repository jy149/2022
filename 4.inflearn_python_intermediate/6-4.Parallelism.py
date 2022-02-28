'''
Futures (동시성)
- 비동기 작업 처리
- 파이썬 GIL 설명
- 동시성 처리 실습 예제
- Process, Thread 예제
'''
# Chapter-06-04
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
# concurrent.futures 사용법1 (map)
# concurrent.futures 사용법2 (wait, as_completed)

# GIL(global interpreter lock) :
# 두 개 이상의 스레드가 동시에 실행 될 때 하나의 자원을 엑세스 하는 경우 -> 문제점(이슈)방지를 위해서
# GIL이 실행된다. 즉, 리소스 전체에 LOCK이 걸린다. + Context Switch(문맥교환)

# GIL을 우회하는 방법
# 멀티 프로세싱 이용, or CPython 이용

import os
import time
from concurrent import futures

WORK_LIST = [100000, 1000000, 10000000, 100000000]

# 동시성 합계 계산 메인 함수
# 누적 합계 함수(Generator)

def sum_generator(n):
    return sum(n for n in range(1, n+1))

def main():
    # Worker Count
    worker = min(10, len(WORK_LIST))

    # 시작 시간
    start_tm = time.time()

    # 결과 건수
    # ThreadPoolExecutor
    # ProcessPoolExecutor
    with futures.ThreadPoolExecutor() as excutor:
        # map -> 작업 순서를 유지하고 즉시 실행한다!
        result = excutor.map(sum_generator, WORK_LIST)


    # 종료시간
    end_tm = time.time() - start_tm

    # 출력 포맷
    msg = '\n Result -> {} Time : {:.2f}s'
    # 최종 결과 출력
    print(msg.format(list(result), end_tm))


# 실행
if __name__ == '__main__':
    main()
