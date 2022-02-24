'''
Special Method 설명
- 파이썬 핵심 구조 설명
- 매직 메소드 실습
- 클래스 매직 메소드 실습
'''
# Chapter03-01
# Special Method(Magic Method)
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(Iterator), 함수(Functions), Class(클래스)
# 클래스안에 정의할 수 있는 특별한(Built-in) 메소드

# 기본형
print(int(10))
# 무심코 사용했던 data type이 class 인것을 알 수 있음
print(int)
print(float)

# 모든 속성 및 메소드 출력
print(dir(int))
print(dir(float))

n = 10
# 변수도 class 인것을 알 수 있음
print(type(n))

print(n + 100) # 아마 내부적으로 __add__가 호출되었겠지
print(n.__add__(100)) # 이렇게 해도 결과 값은 같게 나옴
#print(n.__doc__)
print(n.__bool__(), bool(n)) # 0이면 False, 10이기때문에 True
print(n * 100, n.__mul__(100)) # 곱하기는 내부적으로 __mul__ 로 호출 가능

print()
print()

# 클래스 예제1
class Fruit:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def __str__(self):
        return 'Fruit Class Info : {} , {}'.format(self._name, self._price)

    # Special Method
    def __add__(self, x):
        print('Called __add__')
        return self._price + x._price

    def __sub__(self, x):
        print('Called __sub__')
        return self._price - x._price

    def __le__(self, x):
        print('Called __le__')
        if self._price <= x._price:
            return True
        else:
            return False

    def __ge__(self, x):
        print('Called __ge__')
        if self._price >= x._price:
            return True
        else:
            return False


# 인스턴스 생성
s1 = Fruit('Orange', 7500)
s2 = Fruit('Banana', 3000)

# 매직 메소드를 몰랐다면.... 일반적인 계산
print(s1._price + s2._price)

# 하지만 __add__라는 매직 메소드를 구현해두었기 때문에 내부적으로 __add__메소드가 호출되어서 구현 가능
print(s1 + s2)

print(s1 - s2)
print(s2 - s1)
print(s1 >= s2)
print(s1 <= s2)
print(s1)
print(s2)














