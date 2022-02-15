'''
클래스
모듈, 패키지
예외처리
내장/외장함수
'''
# 반복되는 변수&메서드(함수)를 미리 정해놓은 틀에 집어넣는거임
result = 0
def add(num):
    global result # 지역변수 영향주기위해서 global 변수 써줬음.
    result += num
    return result
print(add(3))
print(add(5))

# 만약 두 개의 계산기가 필요하다면..?
result1 = 0
result2 = 0

def add1(num):
    global result1
    result1 += num
    return result1

def add2(num):
    global result2
    result2 += num
    return result2

print(add1(3))
print(add1(5))

print(add2(1))
print(add2(4))

# 똑같은,, 반복되는 변수랑 메서드 위의 add1 이나 add2나 동일한 로직이 적용되기때문에
# 클래스를 만들어서 똑같이 생긴건 여러개의 인스턴스를 찍어내줄 수 있음

class Calculator:
    def __init__(self):
        self.result = 0
    def add(self, num):
        self.result += num
        return self.result
cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(5))

print(cal2.add(1))
print(cal2.add(4))

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>")

class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setdata(self,first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result

a = FourCal(4,5)
# a.setdata(4,2)
print(a.first)
print(a.second)

print(a.add())
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>")

class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

a = MoreFourCal(4, 2)
print(a.pow())

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>")

class Family:
    lastname = "김" # 클래스변수

Family.lastname = "박" # 설계도 자체를 바꾼거임.
print(Family.lastname)

a = Family()
b = Family()
print(a.lastname)
print(b.lastname)

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>")
from mod1 import add
print(add(10,20))

from mod1 import sub
print(sub(10,40))

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>")
import sys
sys.path.append("./subfolder")
from mod2 import add
print(add(10,20))

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>")
# 패키지란 모듈 여러개를 모아놓은 것이다.

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>")
# 예외처리
'''
try:
    # 오류가 발생할 수 있는 구문
except Exception as e:
    # 오류 발생
else:
    # 오류 발생하지 않음
finally:
    # 무조건 마지막에 실행
'''
try:
    4 / 0
except ZeroDivisionError as e:
    print(e)

print("Hi python!")

try:
    f = open('none', 'r')
except FileNotFoundError as e:
    print(str(e))
else:
    data = f.read()
    print(data)
    f.close()

f = open('foo.txt','r', encoding='utf-8')
try:
    data = f.read()
    print(data)
except Exception as e:
    print(e)
finally:
    f.close()

try:
    a = [1, 2]
    print(a[3])
    b = 4/0
    print(b)
except ZeroDivisionError:
    print("0으로 나눌수 없음")
except IndexError:
    print("인덱싱 에러")

try:
    f = open("없는파일",'r')
except Exception:
    pass

class Bird:
    def fly(self):
        raise Exception
class Eagle(Bird):
    def fly(self):
        print("very fast")
eagle = Eagle()
eagle.fly()


# 내장함수 (filter)
def positive(x):
    return x > 0

a = list(filter(positive, [1, -3, 0, 10, -109, 93]))
print(a)

# 내장함수 (map)
def two_times(x): return x*2
a = list(map(two_times, [1, 2, 3, 4]))
print(a)

a = list(map(lambda x:x*2, [1,2,3,4]))
print(a)

# 외장함수 sys, pickle, time, random,webbrowser...





