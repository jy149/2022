# Chapter 3-5.딕셔너리(Dictionary)
'''
딕셔너리(Dictionary)사용법
- 딕셔너리 선언
- 딕셔너리 특징
- 딕셔너리 수정
- 딕셔너리 함수
- 딕셔너리 중요성
'''
# 범용적으로 가장 많이 사용(JSON)
# 딕셔너리 자료형(순서X, 키 중복 X, 수정O, 삭제O)

# 선언
a = {'Name': 'Kim', 'phone': '0103337777', 'birth': '921117'}
b = {0: 'Hello Python'}
c = {'arr': [1, 2, 3, 4]}
d = {
    'Name': 'Niceman',
    'city': 'Seoul',
    'Age' : 31,
    'Grade': 'A',
    'Status': True
}
e = dict([
    ('Name', 'Niceman'),
    ('city', 'Seoul'),
    ('Age' , 31),
    ('Grade', 'A'),
    ('Status', True)
])

f = dict(
    Name= 'Niceman',
    City= 'Seoul',
    Age= 31,
    Grade= 'A',
    Status= True
)

print('a - ', type(a), a)
print('a - ', type(b), b)
print('a - ', type(c), c)
print('a - ', type(d), d)
print('a - ', type(e), e)
print('a - ', type(f), f)
print()

# 출력
print('a- ', a['Name']) # key가 존재하지 않으면 error 발생
print('a- ', a.get('Name')) # key가 존재하지 않으면 None 처리
print('b- ', b[0])
print('b- ', b.get(0))
print('f- ', f.get('City'))
print('f- ', f.get('Age'))

# 딕셔너리 추가
a['adress'] = 'seoul' # 만약 키값을 똑같이하면 값이 수정됌
print('a- ', a)
a['rank'] = [1, 2, 3]
print('a- ', a)

# 딕셔너리 길이
print('a- ', len(a))
print('a- ', len(b))
print('a- ', len(c))
print('a- ', len(d))
print('a- ', len(e))
print('a- ', len(f))
print()

# dict_keys, dict_values, dict_items : 반복문(__iter__)에서 사용 가능
print('a- ', a.keys())
print('b- ', b.keys())
print('c- ', c.keys())
print('d- ', d.keys())
print('e- ', e.keys())
print('f- ', f.keys())
print()

print('a- ', list(a.keys()))
print('b- ', list(b.keys()))
print()

print('a- ', a.values())
print('b- ', b.values())
print('c- ', c.values())

print('a- ', list(a.values()))
print('b- ', list(b.values()))
print()

print('a- ', a.items())
print('b- ', b.items())
print('c- ', c.items())
print('a- ', list(a.items()))
print('b- ', list(b.items()))
print()

print('a- ', a.pop('Name'))
print('a- ', a)

print('c- ', c.pop('arr'))
print('c- ', c)

print()

print('f- ', f.popitem())
print('f- ', f)
print('f- ', f.popitem())
print('f- ', f)
print('f- ', f.popitem())
print('f- ', f)
print('f- ', f.popitem())
print('f- ', f)
print('f- ', f.popitem())
print('f- ', f)
print()

print('a -', 'birth' in a)
print('d -', 'city' in d)

# 수정
a['test']= 'test_dict'
print('a- ',a)

a['adress'] = 'dj'
print('a- ', a)

a.update(birth='910904')
print('a- ', a)

temp = {'adress': 'Busan'}
a.update(temp)
print('a- ', a)




