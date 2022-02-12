# Chapter 6-3. Package
'''
모듈이 뭉쳐있는 폴더이다.
'''
# 파이썬 패키지
# 패키지 작성 및 사용법
# 파이썬은 패키지로 분할 된 개별적인 모듈로 구성
# __init__.py : python 3.3 부터는 없어도 패키지로 인식 -> 단, 하위 호환을 위해 작성 추천
# 상대경로 : ..(부모디렉토리로 이동) .(현재디렉토리 의미)

# 예제1
import sub.sub1.module1
import sub.sub2.module2

# 사용
sub.sub1.module1.mod1_test1()
sub.sub1.module1.mod1_test2()

sub.sub2.module2.mod2_test1()
sub.sub2.module2.mod2_test2()

print()
print()
print()

# 예제 2
from sub.sub1 import module1 as m1
from sub.sub2 import module2 as m2

m1.mod1_test1()
m1.mod1_test2()

m2.mod2_test1()
m2.mod2_test2()

print()
print()
print()

# 예제3
from sub.sub1 import *
from sub.sub2 import *

module1.mod1_test1()
module1.mod1_test2()

module2.mod2_test1()
module2.mod2_test2()
