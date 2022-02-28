'''
병행성(Concurrency)
- 병행성, 흐름제어 설명
- 이터레이터(Iterator)
- 제네레이터(Generator)
- __iter__, __next__
- 클래스 기반 제네레이터 구현
'''
# Chapter-06-01
# 병행성(Concurrency)
# 이터레이터, 제네레이터
# Iterator, Generator

# 파이썬 반복 가능한 타입
# collections, text file, List, Dict, Set, Tuple, unpacking, *args... : Iterable 하다.

# 반복 가능한 이유? 내부적으로 iter(x)라는 함수가 호출이 됨
t = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for c in t:
    pass
    # print(c)

# while
w = iter(t)


while True:
    try:
        print(next(w))
    except StopIteration:
        break
print()

# 반복형 확인
print(dir(t))
print(hasattr(t, '__iter__'))
from collections import abc
print(isinstance(t, abc.Iterable))

print()
print()

# next
class WordSpliter:
    def __init__(self, text):
        self._idx = 0
        self._text = text.split(' ')

    def __next__(self):
        print('Called __next__')
        try:
            word = str(self._idx + 1) + '_' + self._text[self._idx]
        except IndexError:
            raise StopIteration('Stopped Iteration. ^-^')
        self._idx += 1
        return word

    def __repr__(self):
        return 'WordSplit(%s)' % (self._text)

wi = WordSpliter('Do today what you could do tommorrow')
print(wi)
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
# print(next(wi))

print()
print()

# Generator 패턴
# 1. 지능형 리스트, 딕셔너리, 집합 -> 데이터의 양 증가 , 증가 이후 메모리 사용량 증가 -> 제네레이터 사용 권장!!
# 2. 단위 실행 가능한 코루틴(Corotine) 구현과 연동된다.
# 3. 작은 메모리 조각을 사용한다..

class WordSplitGenerator:
    def __init__(self, text):
        self._text = text.split(' ')

    def __iter__(self):
        for word in self._text:
            yield word # 제네레이터
        return

    def __repr__(self):
        return 'WordSplitGenerator(%s)' % (self._text)

wg = WordSplitGenerator('Do today what you could do tommorrow')

wt = iter(wg)
print(wt, wg)
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
# print(next(wt))

print()
print()
















