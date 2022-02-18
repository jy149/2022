# 이 리스트를 처음부터 끝까지 순회하는 메서드 traverse() 완성시키기
# traverse()는 리스틀 리턴
# LinkedList에 들어있는 L이 43 -> 85 -> 76 이라면
# 올바른 리턴값은 [43, 85, 76] 이다.
class Node:
    def __init__(self, item):
        self.data = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None

    def getAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None
        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1
        return curr

    def traverse(self):
        answer = []
        curr = self.head
        while curr != None:
            answer.append(curr.data)
            curr = curr.next
        return answer


# 이 solution 함수는 그대로 두어야 합니다.
def solution(x):
    return 0