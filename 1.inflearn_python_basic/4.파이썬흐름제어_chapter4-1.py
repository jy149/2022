# Chapter 4-1.IF
'''
IF 구문 실습
- 관계 연산자 실습
- 논리 연산자 실습
- 일반 조건문
- 다중 조건문
- 중첩 조건문
'''

# 기본 형식
print(type(True))   # 0 이 아닌 수, 문자:'abc'... , 리스트:[1,2,3,4], (1,2,3,4...)...
print(type(False)) # 0, "", [], (), {} .... 공통적으로 비어있으면 False
print()

# 예1
if True:
    print('Good')
if False:
    print('Good')
print()

# 예2
if False:
    print('Bad!')
else:
    print('Good!')
print()

# 관계 연산자
# >, >=, <, <=, ==, !=
x, y = 15, 10

# 양 변이 같을 경우 참
print(x == y)
# 양 변이 다를 경우 참
print(x != y)
# 왼쪽이 클 때 참
print(x > y)
# 왼쪽이 크거나 같을 때 참
print(x >= y)
# 오른쪽이 클 때 참
print(x < y)
# 오른쪽이 크거나 같을 때 참
print(x <= y)

print()

# 예3
city = ""
if city:
    print("You are in: ", city)
else:
    print("Plz enter your city")
print()
# 예 4
city2 = "Seoul"
if city2:
    print("You are in: ", city2)
else:
    print("Plz enter your city")
print()
# 논리 연산자
# and ,or, not

a = 75
b = 40
c = 10

print('and:', a > b and b > c) # a > b > c
print('or:', a > b or b > c) # 둘 중에 하나
print('not:', not a > b) # 반대로출력
print('not:', not b > c)
print(not True)
print(not False)
print()

# 산술, 관계, 논리 우선순위
# 산술 > 관계 > 논리 순서이다.
print('e1 : ', 3+12 > 7+3)
print('e2 : ', 5+10*3 > 7+3*20)
print('e3 : ', 5+10 > 3 and 7+3 == 10)
print('e4 : ', 5 + 10 > 0 and not 7 + 3 == 10)
print('e4 : ', 5 + 10 < 0 or 7 + 3 == 10)
print()

# 예 4
score1 = 90
score2 = 'A'

# 복수의 조건이 모두 참일 경우에 실행
if score1 >= 90 and score2 == 'A':
    print('Pass')
else:
    print('Fail')
print()

# 예 5
id1 = 'vip'
id2 = 'admin'
grade = 'platinum'

if id1 == 'vip' or id2 == 'admin':
    print('관리자 입장')

if id2 == 'admin' and grade == 'platinum':
    print('최상위 관리자')
print()

# 예 6
# 다중 조건문
num = 90
if num >= 90:
    print('Grade : A')
elif num >= 80:
    print('Grade : B')
elif num >= 70:
    print('Grade : C')
else:
    print('과락')
print()

# 예 7
# 중첩 조건문
grade = 'A'
total = 95
if grade == 'A':
    if total >= 90:
        print('장학금 100%')
    elif total >= 80:
        print('장학금 80%')
    else:
        print('장학금 50%')
else:
    print('장학금 없음')
print()

# 예 8
# in, not in
q = [10, 20, 30]
w = [70, 80, 90, 100]
e = {"name" : "Lee", "city" : "Seoul", "grade" : "A"}
r = (10, 12, 14)

print(15 in q)
print(90 in w)
print(12 not in r)
print("name" in e)
print("Seoul" in e.values())





























