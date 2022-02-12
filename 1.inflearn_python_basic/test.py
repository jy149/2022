# Chapter 7-1. 예외(Exception)

# 예외(Exception) 개념 및 처리
# 예외 종류
# 다양한 예외 재연
# 예외 처리 기본
# 예외 처리 패턴
# 예외 처리 실습

# 예외 종류
# SyntaxError, TypeError, NameError, ValueError, KeyError...
# 문법적으로는 예외가 없지만, 코드 실행 프로세스(단계)발생하는 예외도 중요
# 1. 예외는 반드시 처리해야한다.
# 2. 로그는 반드시 남겨야 한다.
# 3. 예외는 던져진다.
# 4. 예외 무시

# SyntaxError : 문법 오류
#print('error)
#print('error'))
# if True
#     pass

# NameError : 참조 없음
# a = 10
# b = 15
# print(c)

# ZeroDivisionError
#print(100 / 0)

# IndexError
x = [50, 70, 90]
# print(x[1])
# print(x[5])

# print(x.pop())
# print(x.pop())
# print(x.pop())
# print(x.pop())

# KeyError
# dic = dict(name = 'Lee', Age = 41, City = 'Busan')
# print(dic['hobby'])
# print(dic.get('name1'))

# 예외 없는 것을 가정하고 프로그램 작성 -> 이후에 런타임 예외 발생 시 예외 처리 권장(EAFP)

# Attribute Error : 모듈, 클래스에 있는 잘못된 속성 사용 예외
# # import time
# print(time.time2())

# ValueError
# x = [10, 50, 90]
# x.remove(50)
# print(x)
# x.remove(200)

# FileNotFoundError
# f = open('test.xlsx')

# TypeError : 자료형에 맞지 않는 연산을 수행 할 경우
# x = [1, 2]
# y = (1, 2)
# z = 'test'

# print(x + y)
# print(x + z)
# print(y + z)

# print(x + list(y))
# print(x + list(z))

# 예외 처리 기본
# try : 에러가 발생 할 가능성이 있는 코드
# except 에러명1 :
# except 에러명2 :
# else : try 블록의 에러가 없을 경우 실행
# finally : 항상 마지막에 실행.

name = ['Kim', 'Lee', 'Park']

# 예제 1
# try:
#     z = 'Kim' # 'Kim'이 아니라면, except에 ValueError가 뜨겠지
#     x = name.index(z)
#     print('{} Found it! {} in name'.format(z, x+1))
# except ValueError:
#     print('Not Found it! - Occured ValueError!')
# else:
#     print('Ok! else.')
# print()


# 예제 2
# try:
#     z = 'Kim' # 'Kim'이 아니라면, except에 ValueError가 뜨겠지
#     x = name.index(z)
#     print('{} Found it! {} in name'.format(z, x+1))
# except Exception: # 전체 error에 대해서 포괄적으로 쓸 때 Exception을 써주던가 아무것도 안써주던가(except:).
#     print('Not Found it! - Occured ValueError!')
# else:
#     print('Ok! else.')
# print()

# 예제3
# try:
#     z = 'Cho' # 'Kim'이 아니라면, except에 ValueError가 뜨겠지
#     x = name.index(z)
#     print('{} Found it! {} in name'.format(z, x+1))
# except Exception as e:
#     print(e)
#     print('Not Found it! - Occured ValueError!')
# else:
#     print('Ok! else.')
# finally:
#     print('Ok! finally!')
# print()

# 예제 4
# 예외 발생 : raise
# raise 키워드로 예외 직접 발생

try:
    a = 'Park'
    if a == 'Park2':
        print('OK! Pass!')
    else:
        raise ValueError
except ValueError:
    print('Occured! Exception!')
else:
    print('Ok! else!')