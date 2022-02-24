'''
클래스 기반 개발 설명
- 절차 지향 vs 객체 지향
- 객체 지향 프로그래밍 장점
- 클래스 기반 코딩 실습
'''
# Chapter02-01
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지 등
# 규모가 큰 프로젝트(프로그램) -> 과거에는 함수 중심의 코드였음(매개변수가존재) -> 데이터가 워낙 방대 -> 복잡해짐
# 클래스 중심 -> 데이터 중심 -> 객체로 관리

# 차량 1
car_company_1 = 'Ferrari'
car_detail_1 = [
    {'color': 'White'},
    {'horsepower': 400},
    {'price': 8000}
]

# 차량 2
car_company_2 = 'Bmw'
car_detail_2 = [
    {'color': 'Black'},
    {'horsepower': 270},
    {'price': 5000}
]

# 차량 3
car_company_3 = 'Audi'
car_detail_3 = [
    {'color': 'Silver'},
    {'horsepower': 300},
    {'price': 6000}
]

# 리스트 구조
# 관리하기가 불편
# 인덱스 접근 시 실수 가능성, 삭제 불편
car_company_list = ['Ferrari', 'Bmw', 'Audi']
car_detail_list = [
    {'color': 'White', 'horsepower': 400, 'price': 8000},
    {'color': 'Black', 'horsepower': 270, 'price': 5000},
    {'color': 'Silver', 'horsepower': 300, 'price': 6000}
]

# 리스트에서 삭제하려면?
del car_company_list[1]
del car_detail_list[1]

# 출력
print(car_company_list)
print(car_detail_list)

print()
print()

# 딕셔너리 구조
# 코드 반복 지속, 중첩 문제(키), 키 조회 예외 처리 등
car_dicts = [
    {'car_company': 'Ferrari', 'car_detail': {'color': 'White', 'horsepower': 400, 'price': 8000}},
    {'car_company': 'Bmw', 'car_detail': {'color': 'Black', 'horsepower': 270, 'price': 5000}},
    {'car_company': 'Audi', 'car_detail': {'color': 'Silver', 'horsepower': 300, 'price': 6000}}
]

print(car_dicts)

# pop(key, 'default)
del car_dicts[1] # 이런식으로 지우거나 pop 이용
print(car_dicts)

print()
print()

# 클래스 구조
# 구조 설계 후 재사용성 증가, 코드 반복 최소화, 메소드 활용

class Car():
    def __init__(self, company, details):
        self.company = company
        self.details = details

    # 클래스 내부에 파이썬에서 상속받는 메소드를 가져옴
    def __str__(self):
        return 'str : {} - {}'.format(self.company, self.details)

    # 위의 str과 비슷한 representation 메소드가 있음
    def __repr__(self):
        return 'repr : {} - {}'.format(self.company, self.details)

car1 = Car('Ferrari', {'color': 'White', 'horsepower': 400, 'price': 8000})
car2 = Car('Bmw',     {'color': 'Black', 'horsepower': 270, 'price': 5000})
car3 = Car('Audi',    {'color': 'Silver', 'horsepower': 300, 'price': 6000})

print(car1)
print(car2)
print(car3)

# 속성정보: __dict__
print(car1.__dict__)
print(car2.__dict__)
print(car3.__dict__)

# 모든 메타 정보: dir
# print(dir(car1))

print()
print()

# 리스트 선언
car_list = []

car_list.append(car1)
car_list.append(car2)
car_list.append(car3)

# 명시적(__repr__)
print(car_list)

print()
print()

# 반복(__str__)
for x in car_list:
    print(x)











