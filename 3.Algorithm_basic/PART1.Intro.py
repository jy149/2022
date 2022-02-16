# 문자열(str)
a = "This is a string"
# 리스트(list)
b = [5, 9, 2, 7]
# 사전(dict)
c = {'a': 6, "bc": 4}
# 순서쌍(tuple), 집합(set)...

'''
자료구조(data structures)?
'''
import time
n = int(input("Number of elements: "))
haystack = [k for k in range(n)]
print("Searching fo the maximum value...")

ts = time.time()
maximum = max(haystack)
elapsed = time.time() - ts

print("Maximum element = %d, Elapsed time = %.2f" %(maximum, elapsed))


'''
풀어야 하는 문제는 무엇인가
-> 내가 이용하려는 자료구조는 어떠한 형태를 가질 것인가에 대한 생각을 해야함

알고리즘(algorithm)이란?
- 어떤 문제를 해결하기 위한 자료구조와 연산 방법에 대한 선택.
'''

