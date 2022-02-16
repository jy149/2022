# 선형배열 (Linear Arrays)
# 배열(arrays) -> 같은 종류의 데이터가 여러개로 늘어서있음 -> 리스트(list)를 이용
L = ['Bob', 'Cat', 'Spam', 'Programmers']
print(L[1])
print(L[-2])

# 리스트(배열)연산
# 1)원소 덧붙이기
# 2)끝에서 꺼내기
L = ['Bob', 'Cat', 'Spam', 'Programmers']
L.append('New')
print(L)
L.pop()
print(L)

# 3) 원소 삽입하기 -> insert
# 4) 원소 삭제하기 -> del, remove, pop
L = [20, 37, 58, 72, 91]
L.insert(3,65)
print(L)
L.remove(L[2])
print(L)
del(L[2])
print(L)
print(L.pop(2))
print(L)

# 5)원소 탐색하기 -> index
L = ['Bob', 'Cat', 'Spam', 'Programmers']
print(L.index('Spam'))
print(L.index('Spam'))



