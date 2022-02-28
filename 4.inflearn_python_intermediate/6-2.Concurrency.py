'''
병행성(Concurrency)
- 제네레이터 실습
- Yield 실습
- Itertools 실습
'''
# Chapter-06-02
# 병행성(Concurrency) : 한 컴퓨터가 여러 일을 동시에 수행 -> 단일 프로그램안에서 여러 일을 쉽게 해결할 때 사용
# 병렬성(ParalleLism) : 여러 컴퓨터가 여러 작업을 동시에 수행 -> 속도!

# Generator Ex1
def generator_ex1():
    print('Start')
    yield 'A Point'
    print('Continue')
    yield 'B Point'
    print('End')

temp = iter(generator_ex1())
# print(temp)
# print(next(temp))
# print(next(temp))
# print(next(temp))

for v in generator_ex1():
    pass
    # print(v)

# Generator Ex2
temp2 = [x * 3 for x in generator_ex1()]
temp3 = (x * 3 for x in generator_ex1()) # Generator Comprehension

# print(temp2)
# print(temp3)

for i in temp2:
    print(i)

for i in temp3:
    print(i)

print()
print()

# Generator Ex3(중요 함수)
# count, takewhile, filterfalse, accumulate, chain, product, groupby...

import itertools
# itertools.count(start, jumppoint): 무한대의 수 만들기
gen1 = itertools.count(1, 2.5)

# itertools.takewhile(조건함수, count): 조건 걸기
gen2 = itertools.takewhile(lambda n : n < 1000, itertools.count(1, 2.5))
for v in gen2:
    pass
    # print(v)

print()
print()

# itertools.filterfalse: 필터에 반대되는 역할 하기
gen3 = itertools.filterfalse(lambda n : n < 3, [1, 2, 3, 4, 5])
for v in gen3:
    print(v)

# itertools.accumulate()누적 합계
gen4 = itertools.accumulate([x for x in range(1, 101)])

for v in gen4:
    print(v)

# 연결1 - 서로다른 이터레이블한 객체를 묶어 표현 (broadcasting써도..)
gen5 = itertools.chain('ABCDE', range(1, 11))
print(list(gen5))

# 연결2 - 쌍으로 tuple형 반환
gen6 = itertools.chain(enumerate('ABCDEF'))
print(list(gen6))

# 개별 - 개별 tuple로 분리해서 반환
gen7 = itertools.product('ABCDE')
print(list(gen7))

# 개별2 - 쌍을 매겨줌
gen8 = itertools.product('ABCDE', repeat = 2)
a = list(gen8)
print(a)
print(len(a))

# 그룹화
gen9 = itertools.groupby('AAABBCCCCCCDDDDDEEE')
# print(list(gen9))
for chr, group in gen9:
    print(chr,': ', list(group))










