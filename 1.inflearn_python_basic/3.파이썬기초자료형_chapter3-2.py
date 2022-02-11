# Chapter 3-2.문자형
'''
문자형 사용법
- 문자형 중요성
- 문자형 출력
- 이스케이프
- 멀티라인
- 문자형 연산
- 문자형 형 변환
- 인덱싱
- 문자열 함수
- 슬라이싱
'''

# 문자열 생성
str1 = "I am Python"
str2 = 'Python'
str3 = """How are you"""
str4 = '''Thank you!'''

print(type(str1), type(str2), type(str3), type(str4))
print(len(str1), len(str2), len(str3), len(str4))
print()

# 빈 문자열
str1_t1 = ''
str2_t2 = str()

print(type(str1_t1), len(str1_t1))
print(type(str2_t2), len(str2_t2))
print()

# 이스케이프 문자 사용
# I'm a Boy
print("I'm Boy")
# print('I'm boy') 에러가 뜸
print('I\'m boy')
print('I\\m boy')

print('a \t b')
print('a \nb')
print('a \"\" b')

escape_str1 = "Do you have a \"retro games\"?"
print(escape_str1)
escape_str2 = 'What\'s on TV?'
print(escape_str2)
print()

# 탭, 줄 바꿈
t_s1 = "Click \t Start!"
t_s2 = "New Line \n Check!"

print(t_s1)
print(t_s2)
print()

# Raw String 출력
raw_s = r'D:\python\test'
print(raw_s)
print()

# 멀티라인 입력
# 역슬래시 사용!
multi_str = \
"""
문자열
멀티라인 입력
테스트
"""
print(multi_str)
print()

# 문자열 연산
str_o1 = "python"
str_o2 = "Apple"
str_o3 = "How are you doing"
str_o4 = "Seoul Daejeon Busan Jinju"

print(str_o1 * 3)
print(str_o1 + str_o2)
print('y' in str_o1)
print('n' in str_o1)
print('P' not in str_o2) #대문자라서 없음
print()

# 문자열 형 변환
print(str(66), type(str(66)))
print(str(10.1))
print(str(True), type(str(True)))
print()

# 문자열 함수 (upper, isalnum, startswith, count, endswithm isalpha...)
print("Capitalize: ", str_o1.capitalize()) # 첫번째 문자를 대문자로 바꿈
print("endswith?: ", str_o2.endswith("!")) # 끝 문자를 확인하는거
print("replace", str_o1.replace("thon", 'Good')) # 'thon'을 찾아서 'good'으로 변경시켜줌
print("sorted: ", sorted(str_o1)) # 리스트형태로 반환하는데 순서를 정렬해줌
print("split: ", str_o4.split(" ")) # split 함수 안의 문자를 이용하여 특정 단어단위 분리하여 리스트 변환
print()

# 반복(시퀀스)
im_str = "Good Boy!"
print(dir(im_str)) # __iter__

# 출력
for i in im_str:
    print(i)
print()

# 슬라이싱
str_s1 = "Nice Python"
print(len(str_s1))

# 슬라이싱 연습
print(str_s1[0:3])
print([i for i in range(0,11)])
print(str_s1[5:10])
print(str_s1[5:])
print(str_s1[:len(str_s1)]) # str_s1[:11]
print(str_s1[:len(str_s1) - 1])
print(str_s1[1:9:2]) # 두칸씩 건너띄어서 가져오기
print(str_s1[-5:])
print(str_s1[1:-2])
print(str_s1[::2])
print(str_s1[::-1])

# 아스키 코드(또는 유닌코드)
a = 'z'
print(ord(a)) # 아스키코드로
print(chr(122)) # 문자로



























