'''
파이썬 시퀀스 실습
- 튜플(Tuple)고급 상숑
- Mutable(가변)
- Immutable(불변)
- Sort vs Sorted 실습
'''
# Chatper 04-02
# 시퀀스형
# 컨테이너(Container: 서로 다른 자료형[list, tuple, collections.deque])
# 플랫(Flat: 한 개의 자료형 만 담을 수 있음[str, bytes, bytearray, array.array, memoryview])
# 가변형자료(List, bytearray, array.array, memoryview, deque)
# 불변형자료(tuple, str, bytes)
# 리스트 및 튜플 고급

# Tuple Advanced
# Unpacking

# b, a = a, b
print(divmod(100, 9))
print(divmod(*(100, 9)))
print(*(divmod(100,9)))

print()
print()

x, y, *rest = range(10)
print(x, y, rest)
x, y, *rest = range(2)
print(x, y, rest)
x, y, *rest = 1, 2, 3, 4, 5
print(x, y, rest)

print()
print()

# Mutable(가변형) vs Immutable(불변형)
l = (15, 20, 25)
m = [15, 20, 25]

print(l, id(l))
print(m, id(m))

l = l * 2
m = m * 2

print(l, id(l))
print(m, id(m))

l *= 2
m *= 2
print(l, id(l))
print(m, id(m))

print()
print()

# sort vs sorted
# reverse, key=Len, key=str.Lower, key=func....

# sorted: 정렬 후 새로운 객체로 반환한다.(원본 수정 X)
f_list = ['orange', 'apple', 'mango', 'papaya', 'lemon', 'strawberry', 'coconut']
print('sorted - ', sorted(f_list))
print('sorted - ', sorted(f_list, reverse=True))
print('sorted - ', sorted(f_list, key = len)) # 글자길이 수대로 정렬
print('sorted - ', sorted(f_list, key = lambda x: x[-1])) # 끝의 글자를 기준으로 정렬
print('sorted - ', sorted(f_list, key = lambda x: x[-1], reverse = True))

print('sorted - raw', f_list)
print()
# sort: 정렬 후 객체를 직접 변경한다(원본이 수정됨)
# 반환 값 확인(None)
print('sort - ', f_list.sort(), f_list)
print('sort - ', f_list.sort(reverse=True), f_list)
print('sort - ', f_list.sort(key=len), f_list)
print('sort - ', f_list.sort(key=lambda x: x[-1]), f_list)
print('sort - ', f_list.sort(key=lambda x: x[-1], reverse= True), f_list)

# List vs Array 적합 한 사용법 설명
# 리스트 기반 : 융통성!(다양한 데이터타입을 담을 수 있으니까), 다양한 자료형, 범용적 사용(속도도 빠를듯)
# 숫자 기반(array 사용) : 배열(리스트와 거의 호환)








