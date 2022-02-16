L = [64, 72, 83, 72, 54]
x = 72
def solution(L, x):
    answer =[]
    for i, v in enumerate(L):
        if v == x:
            answer.append(i)
    if answer:
        return answer
    elif x not in L:
        answer.append(-1)
    return answer
print(solution(L,x))

