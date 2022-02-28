'''
병행성(Concurrency)
- 흐름제어, 병행성 처리
- 메인루틴 <-> 서브루틴
- 쓰레드 차이 설명
- 제네레이터 -> 코루틴 설명
'''
# Chapter-06-03
# 병행성(Concurrency) : 한 컴퓨터가 여러 일을 동시에 수행 -> 단일 프로그램안에서 여러 일을 쉽게 해결할 때 사용
# 병렬성(ParalleLism) : 여러 컴퓨터가 여러 작업을 동시에 수행 -> 속도!

# 코루틴 : 단일(싱글) 스레드, 스택을 기반으로 동작하는 비동기 작업
# 쓰레드 : OS에서 관리, CPU 코어에서 실시간, 시분할 비동기 작업 -> 멀티쓰레드

# yield, send : 메인 루틴 <-> 서브 루틴 서로 상호작용을 하게함.
# 코루틴을 제어할 때 yield/send 를 사용, 상태를 저장, 양방향 전송

# 서브루틴 (흐름제어): 메인루틴에서 호출 -> 서브루틴에서 수행
# 코루틴 (동시성 프로그래밍) : 루틴을 실행 중에 정지 -> 이후에 재 실행(시점을 저장하고있으니까)

# 따라서 코루틴은 쓰레드에 비해서 오버헤드가 감소한다.
# 쓰레드 : 싱글쓰레드 -> 멀티쓰레드 -> 코딩하기가 복잡(메모리 공유때문에 값들의 동기화, 씽크로나이즈) / 공유되는 자원떄문에 교착상태발생
# 그리고 쓰레드는 "컨텍스트 스위칭 비용이 발생"(쓰레드끼리의 전환), 자원의 소비 가능성이 증가한다.

# python 3.5이상에서 def -> async, yield -> await 로 바꿔서 사용 가능



# 코루틴 Ex1
def coroutine1():
    print('>>> coroutine started.')
    i = yield
    print('>>> coroutine received : {}'.format(i))

# 메인 루틴
# 제네레이터 선언
cr1 = coroutine1()

print(cr1, type(cr1))

# yield 지점까지 서브루틴을 수행하는 부분
# next(cr1)
# next(cr1)

# send()에 아무값을 넣지 않으면 기본 전달 값은 None
# cr1.send()

# 값 전송
# send() 명령어를 통해서 메인루틴으로부터 서브루틴으로 데이터를 전송가능
# cr1.send(100)


# 잘못된 사용
'''send로 무조건 보낼 수는 없고,
next()함수를 먼저 사용하여 코루틴을 열어주고
해당 지점에서 send명령어를 사용해야한다'''
# cr2 = coroutine1()
# cr2.send(100)


# 코루틴 Ex2
# GEN_CREATED   : 처음 대기 상태
# GEN_RUNNING   : 실행 상태
# GEN_SUSPENDED : yield 대기 상태
# GEN_CLOSED    : 실행 완료 상태

def coroutine2(x):
    print('>>> coroutine started : {}'.format(x))
    y = yield x
    print('>>> coroutine received : {}'.format(y))
    z = yield x + y
    print('>>> coroutine received : {}'.format(z))



# 상태값 확인
from inspect import getgeneratorstate

cr3 = coroutine2(10)
print(getgeneratorstate(cr3))

print(next(cr3)) # 현재는 yield x 대기 상태임, y값을 받기위한 대기 상태
print(getgeneratorstate(cr3))

cr3.send(100) # y값으로 100을 받음 # 값을 보려면 print해봐야함

print()
print()

# Coroutine Ex3
# StopIteration 자동 처리(3.5이상버전 -> await으로 처리 가능)
# 중첩 코루틴 처리

def generator1():
    for x in 'AB':
        yield x
    for y in range(1,4):
        yield y

t1 = generator1()
print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))
# print(next(t1))

t2 = generator1()
print(list(t2)) # generator를 list로 형변환하면 알아서 list로 반환해줌

print()
print()

# yield from은 iterable한 것을 순차적으로 반환, / 위의 generator1 과 같은 코드
def generator2():
    yield from 'AB'
    yield from range(1,4)

t3 = generator2()
print(next(t3))
print(next(t3))
print(next(t3))
print(next(t3))
print(next(t3))
# print(next(t3))






















