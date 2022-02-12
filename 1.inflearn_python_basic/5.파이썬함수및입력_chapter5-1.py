# Chapter 5-1. 함수(Function)
'''
파이썬 함수 사용법
- 함수 중요성
- 함수 선언 및 사용
- 다양한 리턴 사용
- 중첩 함수
- 함수 Hint
- 기타 사용법
- 람다(Lambda)개념
'''
# 파이썬 함수 및 중요성
# 파이썬 함수식 및 람다(Lambda)

# 함수 정의 방법
# def function_name(parameter):
#     code

# 예제1
def first_func(w):
    print("Hello, ", w)

word = "Goodboy"

first_func(word)
print()

# 예제2
def return_func(w):
    value = "Hello, " + str(w)
    return value

x = return_func('Goodboy2')
print(x)
print()

# 예제3(다중반환)
def func_mul(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return y1, y2, y3
x, y, z = func_mul(10)
print(x, y, z)
print()

# 튜플 리턴
def func_mul2(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return (y1, y2, y3)
q = func_mul2(20)
print(type(q),q, list(q))
print()

# 리스트 리턴
def func_mul3(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return [y1, y2, y3]
p = func_mul3(30)
print(type(p), p, set(p))
print()

# 딕셔너리 리턴
def func_mul4(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return {'v1': y1, 'v2': y2, 'v3': y3}
d = func_mul4(30)
print(type(d), d, d.get('v2'), d.items(), d.keys(), d.values())
print()

# 중요
# *args, **kwargs

# *args(언팩킹) -> * 하나는 튜플
def args_func(*args):  #매개 변수 명 자유
    for i, v in enumerate(args):
        print('Result : {}'.format(i), v)
    print('------')

args_func('Lee')
args_func('Lee', 'Park')
args_func('Lee', 'Park', 'Kim')
args_func('Lee', 'Park', 'Kim', 76)
print()

# **kwargs(언팩킹) -> ** 두개는 딕셔너리
def kwarg_func(**kwargs):    #매개 변수 명 자유
    for v in kwargs.keys():
        print("{}".format(v), kwargs[v])
    print('-----')

kwarg_func(name1 = 'Lee')
kwarg_func(name1 = 'Lee', name2 = 'Park')
kwarg_func(name1 = 'Lee', name2 = 'Park', name3 = 'Joe')
kwarg_func(name1 = 'Lee', name2 = 'Park', name3 = 'Joe', sendSMS= True)
kwarg_func(name1 = 'Lee', name2 = 'Park', name3 = 'Joe', sendSMS= False)
print()

# 전체 혼합
# 인수의 갯수에 구애받지 않고 함수를 다양하게 사용할 수 있게 해주는 것이 *, ** 가 붙은 언팩킹
def example(args_1, args_2, *args, **kwargs):
    print(args_1, args_2, args, kwargs)

example(10, 20, 'Lee', 'Kim', 'Park', 'Choi', age1=20, age2=30, age3=40)
print()

# 중첩함수
def nested_func(num):
    def func_in_func(num):
        print(num)
    print('In func')
    func_in_func(num + 100)

nested_func(100)
# 함수안의 함수 func_in_func()을 호출하면 에러가 뜬다,, nested_func()이라는 부모함수가 호출되어야 자식함수가 호출 될 수 있다.
# 실행불가
# func_in_func(1000)
print()


# 람다식 예제
# 람다식 장점 : 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행 함수(Heap 초기화) -> 메모리 초기화
# 남발 시 가독성 오히려 감소

# def mul_func(x, y):
#    return x * y

# lambda x,y: x*y

# 일반적함수 -> 변수할당
def mul_func(x, y):
    return x * y

q = mul_func(10, 50)
mul_func_var = mul_func
print(mul_func_var(20,50))

# 람다함수 -> 할당
lambda_mul_func = lambda x, y: x*y
print(lambda_mul_func(50,50))

def func_final(x, y, func):
    print(x * y * func(100, 100))
func_final(10, 20, lambda x,y: x*y)
























