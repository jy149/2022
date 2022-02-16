'''
리스트 L, 찾고자하는 x,
x 와 같은 값을 가지는 원소의 인덱스 리턴, 존재하지 않을 경우 -1 리턴
L은 자연수 원소, 크기순으로 정렬되어있음, 동일 원소 두번 이상 없음
'''
L = [2, 5, 7, 9, 11]
def solution(L,x):
    lower = 0
    upper = len(L) - 1
    idx = -1
    while lower <= upper:
        mid = int((lower + upper) // 2) # index 값
        if L[mid] == x:
            idx = mid
            break
        elif x < L[mid]:
            upper = mid - 1
        elif x > L[mid]:
            lower = mid + 1
    return idx
print(solution(L,9))