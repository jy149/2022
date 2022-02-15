# 파이썬 실력 키우기
# 파이썬 프로그래밍, 어떻게 시작해야 할까?
# 구구단프로그래밍
def GuGu(n):
    result = []
    i = 1
    while i < 10:
        result.append(n*i)
        i += 1
    return result
print(GuGu(2))

# 3과 5의 배수 합하기
result = 0
for n in range(1, 1000):
    if n % 3 == 0 and n % 5 == 0:
        result +=n
print(result)

# 게시판 페이징하기
def GetTotalPage(m, n):
    if m % n == 0:
        return m // n
    else:
        return (m // n) + 1
print(GetTotalPage(21, 10))

# 간단한 메모장 만들기 -> memo.py
# 탭을 4개의 공백으로 바꾸기







