# Chapter 8-1. 내장함수(Built-in Functions)

# 자주 사용하는 함수 위주로 실습
# 사용하다 보면 자연스럽게 숙달 가능
# str(), int(), tuple() ,, 형변환은 이미 학습했음

# 절대값 : abs()
print(abs(-3))

# all, any : iterable 요소 검사(참/거짓)
print(all([1,2.2,''])) # and 조건
print(any([1,2.2,''])) # or 조건

# chr : 아스키코드 -> 문자로 돌려줌
# ord : 문자 -> 아스키코드로 돌려줌
print(chr(103))
print(ord('g'))

# enumerate : 인덱스 + Iterable한 객체 생성
for i, name in enumerate(['abc', 'bcd', 'efg']):
    print(i, name)

# filter : 반복가능한 객체 요소를 지정한 함수 조건에 맞는 값 추출
def conv_pos(x):
    return abs(x) > 2
print(list(filter(conv_pos, [1, -3, 0, -5, 6])))

print(list(filter(lambda x : abs(x) > 2, [1, -3, 0, -5, 6])))

# id : 객체의 주소값(레퍼런스) 반환
print(id(int(5)))
print(id(4))

# Len : 요소의 길이 반환
print(len('abcdefg'))
print(len([1, 2, 3, 4, 5, 6, 7]))

# max, min : 최대값, 최소값
print(max([1, 2, 3]))
print(max('python study'))

print(min([1, 2, 3]))
print(min('python study'))

# map : 반복가능한 객체 요소를 지정한 함수 실행 후에 추출해서 결과로 되돌려줌
def conv_abs(x):
    return abs(x)

print(list(map(conv_abs, [-3, 2, 0, -5, 6])))
print(list(map(lambda x : abs(x),[-3, 2, 0, -5, 6] )))

# pow : 제곱값을 반환한다.
print(pow(2, 10))

# range : 반복가능한 객체를 반환한다.
print(list(range(1, 10)))
print(list(i for i in range(0, 11)))

# round : 반올림
print(round(6.5781, 2))
print(round(5.5))

# sorted : 반복가능한 객체(Iterable)
print(sorted([6, 7, 4, 3, 2, 1]))
print(sorted([6, 7, 4, 3, 2, 1], reverse = True))

print(sorted(['p', 'y', 't', 'h', 'o', 'n']))

# sum : 반복가능한 객체(Iterable) 합 반환
print(sum([6, 7, 8, 9, 10]))
print(sum(range(1, 101)))

# type : 자료형 확인
print(type(3))
print(type('a'))
print(type({'1': '2'}))
print(type((3,)))
print(type([]))
print(type(set()))

# zip : 반복 가능한 객체(Iterable)의 요소를 묶어서 반환한다.
print(list(zip([10, 20, 30], [40, 50, 60])))
print(list(zip([10, 20, 30], [40, 50]))) # 짝이 있는것만 반환한다..

print(type(list(zip([10, 20, 30], [40, 50, 60]))[0])) # zip함수는 tuple로만들어서 반환한다.














