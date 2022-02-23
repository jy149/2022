'''
클래스 상세 설명
- 클래스 변수 vs 인스턴스 변수
- 클래스 메소드 실습
- 네임스페이스 이해
'''
# Chapter02-02
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지 등
# 규모가 큰 프로젝트(프로그램) -> 과거에는 함수 중심의 코드였음(매개변수가존재) -> 데이터가 워낙 방대 -> 복잡해짐
# 클래스 중심 -> 데이터 중심 -> 객체로 관리

class Car():
    """
    Car Class
    Author : JinYoung
    Date: 2022.02.23
    사용법 __doc__ 로 호출가능
    """

    # 클래스 변수 (모든 인스턴스가 공유)
    car_count  = 0


    def __init__(self, company, details):
        self._company = company
        #self.car_count = 100000 # 클래스변수가 동일 이름으로 인스턴스 변수에 있으면 인스턴스 변수를 호출해준다.
        self._details = details
        Car.car_count += 1

    # 클래스 내부에 파이썬에서 상속받는 메소드를 가져옴
    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._details)

    # 위의 str과 비슷한 representation 메소드가 있음
    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)

    def __del__(self):
        print('del?')
        Car.car_count -= 1

    # 추가
    def detail_info(self):
        print('Current ID : {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('price')))


# Self 의미 -> class를 기반으로 생성된 인스턴스 값을 저장하기 위한 예약어
car1 = Car('Ferrari', {'color': 'White', 'horsepower': 400, 'price': 8000})
car2 = Car('Bmw',     {'color': 'Black', 'horsepower': 270, 'price': 5000})
car3 = Car('Audi',    {'color': 'Silver', 'horsepower': 300, 'price': 6000})

# ID 확인
print(id(car1))
print(id(car2))
print(id(car3))

print(car1._company == car2._company)
print(car1 is car2)

# dir & __dict__ 확인
# dir -> 해당 인스턴스가 가진 모든 attributes 를 리스트형식으로 보여줌
print(dir(car1))
print(dir(car2))

print()
# __dict__ -> 인스턴스 안에 있는 값을 정확히 보여주는거(딕셔너리형태)
print(car1.__dict__)
print(car2.__dict__)

# Doctring -> 클래스안에 큰따옴표로 주석 달아놓은 설명을 보여줌
print(Car.__doc__)
print()

# 실행
car1.detail_info()
Car.detail_info(car1)

car2.detail_info()
Car.detail_info(car2)

# 비교
print(car1.__class__, car2.__class__)
print(id(car1.__class__), id(car2.__class__),id(car3.__class__))

print()
# 에러
#Car.detail_info()


# 공유 확인
print(car1.car_count)
print(car2.car_count)
print(car1.__dict__)
print(car2.__dict__)
print(dir(car1))

# 접근
print(car1.car_count)
print(Car.car_count)

# 삭제 확인
del car2
print(car1.car_count)
print(Car.car_count)

# 인스턴스 네임스페이스에 없으면 상위에서 자동으로 검색한다
# 즉, 동일한 이름으로 변수 생성 가능(인스턴스 검색 후 -> 없으면 상위(클래스 변수, 부모 클래스 변수))




