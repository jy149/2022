# Chapter 3-6.집합(Sets)
'''
집합(Sets)
- 집합선언
- 집합특징
- 집합추가
- 집합관련함수
'''
# 집합(Set) 특징
# 집합(Set) 자료형(순서X, 중복X)

# 선언
a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6])
d = set([1, 2, 'Pen', 'Cap', 'Plate'])
e = {'foo', 'bar', 'baz', 'foo', 'qux'}
f = {42, 'foo', (1, 2, 3), 3.141592}

print('a- ', type(a), a)
print('b- ', type(b), b)
print('c- ', type(c), c)
print('d- ', type(d), d)
print('e- ', type(e), e)
print('f- ', type(f), f)
print()

# 튜플 변환(set -> tuple)
t = tuple(b)
print('t- ', type(t), t)
print('t- ', t[0], t[1:3])
print()

# 리스트 변환(set -> list)
l = list(c)
l2 = list(e)
print('l- ', l)
print('l2- ', l2)
print()

# 길이
print(len(a))
print(len(b))
print(len(c))
print(len(d))
print(len(e))
print(len(f))
print()

# 집합 자료형 활용
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6])

print('s1 & s2 : ', s1 & s2)
print('s1 & s2 : ', s1.intersection(s2))

print('s1 | s2 : ', s1 | s2)
print('s1 | s2 : ', s1.union(s2))

print('s1 - s2 : ', s1 - s2)
print('s1 - s2 : ', s1.difference(s2))
print()

# 중복 원소 확인
print('s1 & s2 : ', s1.isdisjoint(s2))

# 부분 집합 확인
print('s1 & s2 : ', s1.issubset(s2))
print('s1 & s2 : ', s2.issubset(s1))
print('s1 & s2 : ', s1.issuperset(s2))
print()

# 추가 & 제거
s1 = set([1, 2, 3, 4])
# list에서는 append, insert,,,, 접근

s1.add(5)
print('s1- ', s1)

s1.remove(2)
print('s1- ', s1)  # remove로 없는 원소를 지우려면 error 발생

s1.discard(3)
print('s1 - ', s1) # discard로 없는 원소를 지우려해도 에러 발생 없음

s1.clear()
print('s1 - ', s1)

# **** list 도 clear로 삭제 가능
a = [1, 2, 3]
a.clear()
print(a)























