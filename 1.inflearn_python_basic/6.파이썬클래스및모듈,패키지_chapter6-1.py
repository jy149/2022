# Chapter 6-1. Class
'''
클래스 개념
- OOP란?(객체지향프로그램)
- 클래스, 인스턴스
- Self 개념
- 인스턴스 메소드
- 클래스, 인스턴스변수
'''
# OOP(객체 지향 프로그래밍), Self, 인스턴스 메소드, 인스턴스 변수
# 클래스 and 인스턴스 차이 이해
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 접근 가능, 공유
# 인스턴스 변수 : 객체마다 별도 존재

# 예제1
class Dog2: # object를 상속받음
    # 클래스 속성을 지정해줌
    species = 'first_dog'

    # 초기화/인스턴스 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 클래스 정보
print(Dog2)

# 인스턴스화
a = Dog2('mikky', 2)
b = Dog2('baby', 3)
# c = Dog('baby', 3) # 값은 같아도 전혀 다른 객체로 간주(id()를 활용하여 확인)

# 비교
print(a == b, id(a), id(b))

# 네임 스페이스
print('dog2 ', a.__dict__)
print('dog2 ', b.__dict__)

# 인스턴스 속성 확인
print('{} is {} and {} is {}'.format(a.name, a.age, b.name, b.age))

if a.species == 'first_dog':
    print('{0} is a {1}'.format(a.name, a.species))

# 하나의 값을 공유하고 있다..!
# * 객체지향의 핵심적인 부분은 공유하는 부분인 변수와
# * 각각의 공간에 할당한 인스턴스 변수가 있다는 것..!
print(Dog2.species)
print(a.species)
print(b.species)
print()

# 예제 2
# self의 이해
class SelfTest:
    def func1():
        print('Func1 called')
    def func2(self):
        print(id(self))
        print('Func2 called')
f = SelfTest()

# print(dir(f))
print(id(f))
# f.func1() 예외
print(id(f))
f.func2()
SelfTest.func1()
# SelfTest.func2() 예외
SelfTest.func2(f)
print()

# 예제 3
# 클래스 변수, 인스턴스 변수
class Warehouse:
    # 클래스 변수
    stock_num = 0 # 재고

    def __init__(self, name):
        # 인스턴스 변수
        self.name = name
        Warehouse.stock_num += 1

    def __del__(self):
        Warehouse.stock_num -= 1

user1 = Warehouse('Lee')
user2 = Warehouse('Cho')

print(Warehouse.stock_num)
# Warehouse.stock_num = 50
print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print('before>',Warehouse.__dict__)
print('>>>>', user1.stock_num) # 위의 __dict__에는 안나오지만 공유되는 변수이기때문에 없으면 class에서 찾아서 표현해줌

del user1
print('after>',Warehouse.__dict__)
print()

# 예제 4
class Dog: # object를 상속받음
    # 클래스 속성을 지정해줌
    species = 'first_dog'

    # 초기화/인스턴스 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return '{} is {} years old'.format(self.name, self.age)

    def speak(self, sound):
        return "{} says {}!".format(self.name, sound)

# 인스턴스 생성
c = Dog('july', 4)
d = Dog('Marry', 10)
# 메소드 호출
print(c.info())
print(d.info())
print(c.speak('Wal Wal'))
print(d.speak('Mung Mung'))






























