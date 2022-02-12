# Chapter 6-2. 모듈(Module)
'''
연관 관계가 있는 변수, 함수, 클래스 등을 모아둔 것이 모듈이다.
# Module: 파이썬 구성 요소 등을 모아놓은 파일.
'''
def add(x, y):
    return x + y

def substract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def power(x, y):
    return x ** y

# __name__ 사용
if __name__ == '__main__':
    print('-' * 15)
    print('called! inner!')
    print(add(5, 5))
    print(substract(15, 5))
    print(multiply(5, 5))
    print(divide(10, 2))
    print(power(5, 3))
    print('-' * 15)

