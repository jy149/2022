# 배열을 정렬하고 searching하기
# 정해진 규칙에 따라서 늘여놓는 방법
'''
1) sorted()
- 내장함수
2) sort()
- 리스트의 메서드, 변경된 리스트를 정렬
'''
L = [3, 8, 2, 7, 6, 10, 9]
L2 = sorted(L)
print(L2)
print(L)

L.sort() # L 리스트 자체가 변화하게된다.
print(L)

# 정렬의 순서를 반대로
# reverse = True
# L2 = sorted(L, reverse = True)
# L.sort(reverse = True)

# 문자열의 경우 정렬순서는 '알파벳'순서이다.
# 만약 문자열 길이 순서로 정렬하려면.? -> 정렬에 이용하는 키(key)를 지정

L = ['abcd', 'xyz', 'spam']
L2 = sorted(L, key = lambda x : len(x))
print(L)
print(L2)

# 정렬의 키를 지정하는 또다른 예
L = [{'name': 'John','score': 83}, {'name':'Paul','score':92}]
L.sort(key= lambda x: x['name'])
print(L)
L.sort(key= lambda x: x['score'], reverse = True)
print(L)

# 탐색
# 1) 선형탐색(Linear Search)
L = [3, 8, 2, 7, 6, 10, 9]
def linear_search(L,x):
    i = 0
    while i < len(L) and L[i] != x:
        i += 1
    if i < len(L):
        return i
    else:
        return -1
print(linear_search(L,6))
print(L.index(6))

# 2) 이진탐색(Binary Search) - 탐색하려는 리스트가 정렬되어있는 경우에만 적용 가능
'''
lower = 0
upper = len(L) - 1
idx = -1

while lower <= upper:
    middle = (lower + upper) // 2
    if L[middle] == target:
        ....
    elif L[middle] < target:
        lower = ...
    else:
        upper = ...
'''

