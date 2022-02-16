# recursive algorithm (재귀알고리즘)
# recursive functions : 재귀함수 -> 하나의 함수에서 자신을 다시 호출하여 작업을 수행.
# 이진트리(binary trees)

# 보다 간단한 예로 자연수의 합 구하기
# 문제 : 1 부터 n 까지의 모든 자연수의 합을 구하시오
def sum(n):
    print(n)
    if n <= 1:
        return n
    else:
        return n + sum(n-1)
a = int(input("Number: "))
print(sum(a))

# 재귀 알고리즘 사용시에는 종결조건을 확실히 할것..!

# 반복(iterative version)으로 쓰면?
def sum2(n):
    s = 0
    while n >= 0:
        s+= n
        n-=1
    return s
s = int(input("Number: "))
print(sum(s))

# 재귀 알고리즘 추가 예제 -> n factorial 을 구하는 알고리즘이겠지..!
def what(n):
    if n <= 1:
        return 1
    else:
        return n * what(n-1)

# 연습문제는 피보나치(Fibonacci)순열 -> iter + recul
# f_0 = 0
# f_1 = 1
# f_2 = 0+1
