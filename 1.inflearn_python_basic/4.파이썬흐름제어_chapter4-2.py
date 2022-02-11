# Chapter 4-2.For 구문
'''
For 흐름제어 실습
- 반복문 중요성
- 기본 For 사용
- For 문 패턴 실습
- For-Else 구문
'''
# 코딩의 핵심
# for in <collection>
#     <Loop body>
for v1 in range(10):
    print('v1 is :', v1)
print()

for v2 in range(1, 11):
    print('v2 is :',v2)
print()

for v3 in range(1,11,2):
    print('v3 is :',v3)
print()

# 1 ~ 1000 의 합
sum1 = 0
for v in range(1, 1001):
    sum1 += v
print('1~1001 Sum:',sum1)
print()

print('1 ~ 1000 Sum:', sum(range(1,1001)))
print(type(range(1,11)))

print('1 ~ 1000 4의 배수의 합', sum(range(4,1001,4)))
print()

# Iterables 자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전(dictionary)
# iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip

# 예제1
names = ['Kim', 'Park', 'Cho', 'Lee', 'Choi', 'Yoo']

for name in names:
    print('You are : ', name)
print()

# 예제2
lotto_numbers = [11, 19, 21, 28, 36, 37]

for n in lotto_numbers:
    print("Current number : ", n)
print()

# 예제3
word = "Beautiful"

for s in word:
    print('word : ', s)
print()

# 예제4
my_info = {
    "name" : "Lee",
    "age" : 33,
    "City" : "Seoul"
}

for k in my_info:
    print("key : ", k)

for v in my_info.values():
    print('value :', v)
print()

# 예제5
name = 'FineAppLE'
for n in name:
    if n.isupper():
        print(n)
    else:
        print(n.upper())
print()

# break 문
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]
for num in numbers:
    if num == 34:
        print('Found : 34!')
        break
    else:
        print('Not Found : ', num)
print()

# continue
lt = ["1", 2, 5, True, 4.3, complex(4)]
for i in lt:
    if type(i) is bool:
        continue
    print("current type :", i, type(i))
    print("multiply by 2 : ", i * 3)
print()

# for - else
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 49:
        print("Found : 49!")
        break
else:
    print("Not Found : 49")
print()

# 구구단 출력
for i in range(2, 10):
    for j in range(1,10):
        print('{:4d}'.format(i*j), end=' ')
    print()
print()

# 변환 예제
name2 = 'Aceman'
print('Reversed', reversed(name2))
print('List', list(reversed(name2)))
print('Tuple', tuple(reversed(name2)))
print('Set', set(reversed(name2))) # 순서가 없음, 중복허용 X










