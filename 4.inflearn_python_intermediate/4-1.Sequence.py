# What is python sequence?
# Sequence 타입 뿐만 아니라 파이썬의 다양한 자료구조에 대해서도 설명
'''
파이썬 시퀀스형
- 파이썬 데이터 타입 상세 분류
- 지능형 리스트, 튜플, 딕셔너리
- Array 실습
- 지능형 리스트 주의할 점
'''
# Chatper 04-01
# 시퀀스형
# 컨테이너(Container: 서로 다른 자료형[list, tuple, collections.deque])
# 플랫(Flat: 한 개의 자료형 만 담을 수 있음[str, bytes, bytearray, array.array, memoryview])
# 가변형자료(List, bytearray, array.array, memoryview, deque)
# 불변형자료(tuple, str, bytes)
# 리스트 및 튜플 고급

# 지능형 리스트(Comprehending Lists)
chars = '+_)(*&^%$#@!)'
#chars[2] = 'h' # TypeError: 'str' object does not support item assignment. 불변형이다.
code_list1 = []

# 유니코드 리스트
for s in chars:
    code_list1.append(ord(s))
print(code_list1)

# Comprehending Lists
code_list2 = [ord(s) for s in chars]
print(code_list2)

# Comprehending Lists + Map, Filter
code_list3 = [ord(s) for s in chars if ord(s) > 40]
print(code_list3)

code_list4 = list(filter(lambda x: x>40, map(ord,chars)))
print(code_list4)

print()

# 전체 출력
print(code_list1)
print(code_list2)
print(code_list3)
print(code_list4)
print([chr(s) for s in code_list1])
print([chr(s) for s in code_list2])
print([chr(s) for s in code_list3])
print([chr(s) for s in code_list4])

print()

# Generator 생성
import array

# Generator : 한 번에 한 개의 항목을 생성(메모리 유지 X)
tuple_g = (ord(s) for s in chars)
array_g = array.array('I', (ord(s) for s in chars))

print(tuple_g) # generator 은 아직 값은 생성안했고 첫번째값을 준비해둔거임!! 부릉부릉상태
print(type(tuple_g))

# next 함수를 이용해서 하나씩 반환해줌
print(next(tuple_g))
print(next(tuple_g))

print(array_g)
print(type(array_g))
print(array_g.tolist()) # .tolist(): array를 list로 반환

print()
print()

# Generator 예제
print(('%s' % c + '-' + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 21)))

for s in ('%s' % c + '-' + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 21)):
    print(s)

print()
print()
# 깊은 복사(deep copy) vs 얕은 복사(shallow copy)
# 리스트 주의
marks1 = [['~'] * 3 for _ in range(4)]
marks2 = [['~'] * 3] * 4

print(marks1)
print(marks2)

# 만약 수정시..?
marks1[0][1] = 'X'
print(marks1)

marks2[0][1] = 'X'
print(marks2)

# 증명
print([id(i) for i in marks1])
print([id(i) for i in marks2])
# 단순히 *4 로 원본을 복사했을 경우 동일한 id 로 생성되는 것이 보임
# 따라서 리스트를 만들고 복사할때는 조심해서 만들어줘야함




















