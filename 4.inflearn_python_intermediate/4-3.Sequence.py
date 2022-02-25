'''
파이썬 시퀀스 실습
- 해시 테이블(Hashtable)
- Dict 생성 고급 예제
- Setdefault 사용법
-> 오픈소스 같은거 보면 튜플을 많이 사용함, key를 하나로 통합하면서 Dict형식으로 갖춰야 하는 때에 패턴을 알면 손쉬워짐
'''
# Chatper 04-03
# 시퀀스형
# 컨테이너(Container: 서로 다른 자료형[list, tuple, collections.deque])
# 플랫(Flat: 한 개의 자료형 만 담을 수 있음[str, bytes, bytearray, array.array, memoryview])
# 가변형자료(List, bytearray, array.array, memoryview, deque)
# 불변형자료(tuple, str, bytes)

# 해시테이블
# Key에 Value를 저장하는 구조를 의미.
# 파이썬 dict 해쉬 테이블 예
# 해쉬 왜쓸까? Key 값의 연산 결과에 따라 직접 접근이 가능한 구조라는 것.
# key 값을 해싱 함수를 통해 -> 해쉬 주소 값이 나옴 -> key에 대한 value의 위치를 알 수 있음

# Dict 구조
#print(__builtins__.__dict__)

# Hash 값 확인
t1 = (10, 20, (30, 40, 50))
t2 = (10, 20, [30, 40, 50])

print(hash(t1))
# print(hash(t2)) 해쉬함수에 사용되려면 불변형 자료만 가능하다(t2는 리스트가 속함)

print()
print()

# Dict Setdefault 함수 예제
source = (('k1', 'val1'),
          ('k1', 'val2'),
          ('k2', 'val3'),
          ('k2', 'val4'),
          ('k2', 'val5'))

new_dict1 = {}
new_dict2 = {}

# No use Setdefault
for k, v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else:
        new_dict1[k] = [v]

print(new_dict1)

# Use Setdefault
for k, v in source:
    new_dict2.setdefault(k, []).append(v)

print(new_dict2)

# 주의
new_dict3 = {k: v for k, v in source}
print(new_dict3)











