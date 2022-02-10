'''
1-2. 다양한 변수 선언법
- 변수 할당 설명
- Object Identity
- 변수 네이밍 규칙
- 예약어
'''

# 기본 선언
n = 700

# 출력
print(n)
print(type(n)) # type()은 자료형을 보여준다.

# 동시 선언
x = y = z = 700
print(x,y,z)

# 선언
var = 75

# 재선언
var = "Change Value"

# 출력
print(var)
print(type(var))

print()

# Object Reference
# 변수 값 할당 상태
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔 출력

# 예1)
print(300)
print(int(300))

# 예2)
# n -> 777
n = 777
print(n, type(n))
print()

m = n # m -> 777 <- n
print(m, n)
print(type(m), type(n))
print()

m = 400
print(m, n)
print(type(m), type(n))
print()

# id(idendtity)확인 : 객체의 고유값 확인
m = 800
n = 655

print(id(m))
print(id(n))
print(id(m) == id(n))
print()

# 같은 오브젝트 참조
m = 800
n = 800

print(id(m))
print(id(n))
print(id(m) == id(n))
print()

# 다양한 변수 선언
# Came Case : numberOfCollegeGraduates -> Method 선언시 사용
# Pascal Case : NumberOfCollegeGraduates -> Class 선언시 사용
# Snake Case : number_of_college_graduates

# 허용하는 변수 선언 법
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE_ = 8

# 특수문자 또는 숫자로 시작하는 변수는 안됌!!

# 예약어는 변수명으로 불가능
# python reserve word 라고 구글 검색하면 예약어 있음
"""
False	def	if	raise
None	del	import	return
True	elif	in	try
and	else	is	while
as	except	lambda	with
assert	finally	nonlocal	yield
break	for	not	
class	from	or	
continue	global	pass	
"""














