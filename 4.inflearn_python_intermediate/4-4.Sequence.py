'''
파이썬 시퀀스 실습
- 해시 테이블(Hashtable)
- Immutable Dict 생성
- 지능형 Set
- Set 선언 최적화
'''
# Chatper 04-03
# 시퀀스형
# 해시테이블(hashtable) -> 적은 리소스로 많은 데이터를 효율적으로 관리하기 위한 자료구조
# Dict -> Key 중복 허용 X, Set -> 중복을 허용 X
# Dict 및 Set 심화

# Immutable Dict

from types import MappingProxyType

d = {'key1': 'value1'}

# Read Only
d_frozen = MappingProxyType(d)

print(d, id(d))
print(d_frozen, id(d_frozen))

# 수정 불가
# d_frozen['key2'] = 'value2' # TypeError: 'mappingproxy' object does not support item assignment

# 수정 가능
d['key2'] = 'value2'
print(d)

print()
print()

# Set
s1 = {'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'}
s2 = set(['Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'])
s3 = {3}
s4 = set() # Not {}
s5 = frozenset({'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'})

s1.add('Mellon')
print(s1)

# 추가 불가
# s5.add('Mellon') # AttributeError: 'frozenset' object has no attribute 'add'

print(s1, type(s1))
print(s2, type(s2))
print(s3, type(s3))
print(s4, type(s4))
print(s5, type(s5))

# 선언 최적화
# 바이트 코드를 실행 -> 파이썬 인터프리터가 바이트코드 실행
from dis import dis # 바이트코드 생성 순서 볼 수있음

print('-----')
print(dis('{10}')) # 이게 조금 더 빠름
print('-----')
print(dis('set([10])'))

# 지능형 집합(Comprehending Set)

print('-----')
from unicodedata import name
print({name(chr(i), '') for i in range(0, 256)})



































