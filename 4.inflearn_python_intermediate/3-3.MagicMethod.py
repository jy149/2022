'''
파이썬 데이터 모델 추상화
- 데이터 모델 설계
- NamedTuple 설명 -> Tuple은 한번 입력하면 수정이 안되지, unique 한 값, 변경되지 않아야 할 값을 저장하는데 좋음
- Model Unpacking
- 네임드 튜플 실습 코딩
'''
# Chapter03-03
# Special Method(Magic Method)
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(Iterator), 함수(Functions), Class(클래스)
# 클래스안에 정의할 수 있는 특별한(Built-in) 메소드

# 객체 -> 파이썬의 데이터를 추상화 한다.
# 모든 객체 -> id, type -> value

# 일반적인 튜플
pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

# 루트를 씌워주는 함수 sqrt
from math import sqrt

l_leng1 = sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)
print(l_leng1)

# 네임드 튜플 사용 -> 튜플인데 딕셔너리(key,index)의 형태를 가지고 있음

from collections import namedtuple

# 네임드 튜플 선언
Point = namedtuple('Point', 'x y')

pt3 = Point(1.0, 5.0)
pt4 = Point(2.5, 1.5)

# print(pt3)
# print(pt3[0])
# print(pt3[1])
# print(pt4)

l_leng2 = sqrt((pt3.x - pt4.x) ** 2 + (pt3.y - pt4.y) ** 2)
print(l_leng2)

# 네임드 튜플 선언 방법
Point1 = namedtuple('Point1', ['x', 'y'])
Point2 = namedtuple('Point2', 'x, y')
Point3 = namedtuple('Point3', 'x y')
Point4 = namedtuple('Point4', 'x y x class', rename= True) # Key값에 중복되거나 예약어가 사용될 경우 rename 옵션사용(default : False)

# 출력
print(Point1, Point2, Point3, Point4)

# Dict to Unpacking
temp_dict = {'x':75, 'y': 55}

# 객체생성
p1 = Point1(x= 10, y= 35)
p2 = Point2(20, 40)
p3 = Point3(45, y=20)
p4 = Point4(10, 20, 30, 40)

p5 = Point1(**temp_dict)

print()

print(p1)
print(p2)
print(p3)

#rename 테스트
print(p4) # rename 옵션 활용한 결과 _2, _3 으로 key값의 이름이 변경된것을 알 수 있음

# Unpacking Test
print(p5)

# 사용
print(p1[0] + p2[1])
print(p1.x + p2.y)

x, y = p3
print(x, y)



# 네임드 튜플 메소드
temp = [52, 38]

# _make() : 리스트를 네임드튜플로 변경
p4 = Point1._make(temp)
print(p4)

# _fields : 필드 네임 확인
print(p1._fields, p2._fields, p3._fields)

# _asdict() : OrderedDict 반환
print(p1._asdict())
print(p4._asdict())


# 실 사용 실습
# 각 반에 20명의 학생이 있고, 4개의 반(A, B, C, D)
# 그럼 B반의 14번학생, D반의 19번학생.. 만들기 가능

Classes = namedtuple('Classes', ['rank', 'number'])

# 그룹 리스트 선언
numbers = [str(n) for n in range(1,21)]
ranks = 'A B C D'.split()

# List Comprehension
students = [Classes(rank, number) for rank in ranks for number in numbers]
print(len(students))
print(students)


# 추천
students2 = [Classes(rank, number)
             for rank in 'A B C D'.split()
             for number in [str(n) for n in range(1,21)]
             ]
print(len(students2))
print(students2)

# 출력
for s in students2:
    print(s)
























