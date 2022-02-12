# 모듈 사용 실습
import sys
print(sys.path)
print(type(sys.path))
# 모듈경로삽입
# 영구적으로 사용하려면 python path, 즉 환경변수에 영구적으로 등록해두어야함
sys.path.append(r'C:\Users\user\Desktop\2022\1.inflearn_python_basic\math')
print(sys.path)

import test_module

# 모듈 사용
print(test_module.power(10,3))



