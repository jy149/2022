'''
파이썬 일급 함수(객체)
- 파이썬 함수 특징
- 익명함수(Lambda)
- Callable 설명
- Partial 사용법

-> 함수형 프로그래밍 사용 가능
'''

# Chapter05-01
# 일급함수(일급 객체)
# 파이썬 함수 특징
# 1.런타임 초기화
# 2.변수 할당 가능
# 3.함수를 다른 함수의 parameter로 전달 가능
# 4.함수를 결과로 반환(return)

# Factorial 함수만들기
# 함수 객체

def factorial(n):
    '''Factorial Function -> n : int'''
    if n == 1: # n < 2
        return 1
    return n * factorial(n-1)

class A:
    pass

print(factorial(5))
print(factorial.__doc__)
print(type(factorial), type(A))
print(set(sorted(dir(factorial))) - set(sorted(dir(A)))) # 함수만 가지고있는 속성
print(factorial.__name__)
print(factorial.__code__) # 파일 위치와 코드 내용

print()
print()

# 변수 할당 가능한지 증명
var_func = factorial
print(var_func)
print(var_func(10)) # 변수 할당하고 실행 가능
print(list(map(var_func, range(1, 11))))

# 함수를 인수로 전달 및 함수로 결과 반환가능한지? -> 고위함수(Higher-order function)
# ***************************중요***************************
# map, filter, reduce

print(list(map(var_func, filter(lambda x: x%2, range(1, 6)))))
print([var_func(i) for i in range(1, 6) if i % 2])

print()
print()

# reduce 함수
from functools import reduce
from operator import add

print(reduce(add, range(1,11))) # 인자 하나하나를 줄여가면서 add를 실행
print(sum(range(1,11)))

# 익명함수(Lambda)
# 가급적 주석 작성!
# 가급적 함수 작성
# 일반 함수 형태로 리팩토링 권장!

print(reduce(lambda x, t: x + t, range(1,11)))

print()
print()

# Callable : 호출 연산자 -> 메소드 형태로 호출 가능한 지 확인
# 호출 가능 확인
print(callable(str), callable(A), callable(list), callable(var_func), callable(factorial), callable(3.14)) # 상수는 함수형태로못부르지

print()
print()

# partial 사용법! -> 인수를 한쪽 고정 -> 주로 콜백 함수에 사용
from operator import mul
from functools import partial

print(mul(10,10))

# 앞의 10은 고정하고 뒤의 값만 바꾸고 싶다면?
# 인수 고정
five = partial(mul,5) # 5 * ?

# 고정 추가
six = partial(five,6)

print(five(10))

print(six()) # 이미 a:5 와 b:6 이 고정되었으니까.

print([five(i) for i in range(1,10)])
print(list(map(five, range(1,10))))










































