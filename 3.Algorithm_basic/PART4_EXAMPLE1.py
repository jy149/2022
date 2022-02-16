'''
인자로 0 or 양의정수인 x 가 주어짐,
피보나치순열의 해당값 구해서 반환
1) 재귀적방법
2) iter 방법
'''

def solution(x):
    a = [i for i in range(x+1)]
    for i in range(1, len(a)):
        a[0] = 0
        a[1] = 1
        a[i] = a[i-1] + a[i-2]
    return a[-1]
print(solution(15))

def reculsive(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return reculsive(x-1) + reculsive(x-2)

print(reculsive(15))

def iter(x):
    f0 = 0
    f1 = 1
    n = 0
    if x >= 2:
        while n < x-1:
            f2 = f0 + f1
            f0 = f1
            f1 = f2
            n += 1
        return f2
    elif x == 1:
        return f1
    else:
        return f0
print(iter(15))