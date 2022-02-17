# 재귀적 알고리즘 응용
# factorial algorithm
from math import factorial as f
def combi(n,m):
    return f(n) / f(m) * (f(m) * f(n-m))

# 조합의 수 계산
def combi(n, m):
    if n == m:
        return 1
    elif m == 0:
        return 1
    else:
        return combi(n-1,m) + combi(n-1, m-1)

# 피보나치수열 - 재귀적방법으로 풀면??
def fibo(n):
    if n <= 1:
        return n
    return fibo(n-1) + fibo(n-2)

print(fibo(15))

# 피보나시 함수 time 비교 (rec vs iter)
import time
def rec(n):
    if n <= 1:
        return n
    else:
        return rec(n-1) + rec(n-2)

def iter(n):
    if n <= 1:
        return n
    else:
        i = 2
        t0 = 0
        t1 = 1
        while i <= n:
            t0, t1 = t1, t0+t1
            i += 1
        return t1

while True:
    nbr = int(input("Enter a number: "))
    if nbr == -1:
        break
    ts = time.time()
    fibo = iter(nbr)
    ts = time.time() - ts
    print("Iterative version: %d (%.3f)" % (fibo, ts))

    ts = time.time()
    fibo = rec(nbr)
    ts = time.time() - ts
    print("Recursive version: %d (%.3f)" % (fibo, ts))

# 연습문제 재귀적 이진탐색
'''
def binsearch(L, x, lower, upper):
    if ----:
        return -1
    mid = (lower + upper) // 2
    if x == L(mid):
        return mid
    elif x < L[mid]:
        return -----
    else:
        return -----
'''