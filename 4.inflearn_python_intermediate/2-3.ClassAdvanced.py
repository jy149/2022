'''
클래스 기반 메소드 심화
- class Method
- Instance Method
- Static Method
- 3가지 메소드 활용 실습
'''
# Chapter02-03
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지 등
# 규모가 큰 프로젝트(프로그램) -> 과거에는 함수 중심의 코드였음(매개변수가존재) -> 데이터가 워낙 방대 -> 복잡해짐
# 클래스 중심 -> 데이터 중심 -> 객체로 관리

class Car():
    """
    Car Class
    Author : JinYoung
    Date: 2022.02.23
    사용법 __doc__ 로 호출가능
    Description : Class, Static, Instance Method
    """

    # 클래스 변수 (모든 인스턴스가 공유)
    price_per_raise = 1.0

    def __init__(self, company, details):
        self._company = company
        self._details = details

    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)

    # 지금까지 사용해 왔던 self를 받는 함수가 Instance Method이다.
    # Self: 객체의 고유한 속성 값을 사용한다.
    def detail_info(self):
        print('Current ID : {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('price')))

    # Instance Method generate
    def get_price(self):
        return 'Before Car Price -> company: {}, price: {}'.format(self._company, self._details.get('price'))

    # Instance Method generate
    def get_price_culc(self):
        return 'After Car Price -> company: {}, price: {}'.format(self._company, self._details.get('price') * Car.price_per_raise)

    # Class Method 활용
    @classmethod
    def raise_price(cls, per):
        if per <= 1:
            print('Please Enter 1 Or More')
            return
        cls.price_per_raise = per
        print('Succeed! price increased.')

    # Static Method
    @staticmethod
    def is_bmw(inst):
        if inst._company == 'Bmw':
            return 'OK! This car is {}'.format(inst._company)
        return 'Sorry. This car is not Bmw.'



# Self 의미 -> class를 기반으로 생성된 인스턴스 값을 저장하기 위한 예약어
car1 = Car('Ferrari', {'color': 'White', 'horsepower': 400, 'price': 8000})
car2 = Car('Bmw',     {'color': 'Black', 'horsepower': 270, 'price': 5000})

# 전체 정보 확인
car1.detail_info()
car2.detail_info()

# 가격 정보 확인(인스턴스 직접 접근 -> 직접접근은 좋지 않은 방법이다.. Instance Method 만드는게 좋음)
print(car1._details.get('price'))
print(car2._details['price'])

# 가격정보(Instance Method) 인상 전
print(car1.get_price())
print(car2.get_price())

# 가격정보(Instance Method) 인상 후 [클래스 메소드 미사용]
Car.price_per_raise = 1.4

# 가격정보(인상 후)
print(car1.get_price_culc())
print(car2.get_price_culc())

# [Class Method 사용]
Car.raise_price(1.6)

# 가격정보(인상 후)
print(car1.get_price_culc())
print(car2.get_price_culc())


print()

# Static Method(인스턴스로 호출)
print(car1.is_bmw(car1))
print(car2.is_bmw(car2))

# Static Method(클래스로 호출)
print(Car.is_bmw(car1))
print(Car.is_bmw(car2))