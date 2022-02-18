# 연결 리스트 연산 - 원소의 삽입
def insertAt(self, pos, newNode):
    prev = self.getAt(pos - 1)
    newNode.next = prev.next
    prev.next = newNode
    self.nodeCount += 1
# 삽입하려는 위치가 리스트 맨 앞일 때
# prev가 없음
# Head의 조정이 필요

# 삽입하려는 위치가 리스트의 맨 끝일 때
# Tail을 조정해야함

# 빈 리스트에 삽입할때는?
'''
def insertAt(self, pos, newNode):
    if pos < 1 or pos > self.nodeCount +1:
        return False

    # pos 가 1이라는 뜻은, 삽입되는 노드가 첫번째일경우
    if pos == 1:
        newNode.next = self.head
        self.head = newNode

    # 먼저 이전 노드를 정의하고,
    # 새로운 노드의 다음은 기존의 이전 노드의 다음을 명시해주고
    # 이전 노드의 다음이 새로운 노드라는것을 말해줌
    else:
        prev = self.getAt(pos -1)
        newNode.next = prev.next
        prev.next = newNode

    # pos가 지금 존재하는 모든 노드들 뒤, 맨 마지막에 삽입한다면 tail을 조정해준다.
    if pos == self.nodeCount +1:
        self.tail = newNode
    self.nodeCount += 1
    return True
'''
#----------------------------------------------------------------------#

# if prev == tail: 이런식으로 맨앞에서 찾아갈 필요없이해도 될듯
'''def insertAt(self, pos, newNode):
    if pos < 1 or pos > self.nodeCount +1:
        return False

    # pos 가 1이라는 뜻은, 삽입되는 노드가 첫번째일경우
    if pos == 1:
        newNode.next = self.head
        self.head = newNode
    else:
        if pos == self.nodeCount + 1:
            prev = self.tail
        else:
            prev = self.getAt(pos - 1)
        newNode.next = prev.next
        prev.next = newNode

    if pos == self.nodeCount + 1:
        self.tail = newNode
    self.nodeCount += 1
    return True

'''
#----------------------------------------------------------------------#

class Node:
    def __init__(self, item):
        self.data = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None

    def __repr__(self): # 문자열 return 을 위한 내장 함수
        if self.nodeCount == 0:
            return 'LinkedList: empty'

        s = ''
        curr = self.head
        while curr is not None:
            s += repr(curr.data)
            if curr.next is not None:
                s += ' -> '
            curr = curr.next
        return s

    def getAt(self, pos):
        if pos <= 0 or pos > self.nodeCount:
            return None
        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1
        return curr

    def inserAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False
        if pos == 1:
            newNode.next = self.head
            self.head = newNode
        else:
            if pos == self.nodeCount +1:
                 prev = self.tail
            else:
                prev = self.getAt(pos - 1)
            newNode.next = prev.next
            prev.next = newNode
        if pos == self.nodeCount + 1:
            self.tail = newNode
        self.nodeCount += 1
        return True

a = Node(67)
b = Node(34)
c = Node(28)
L = LinkedList()
print(L)
print(L.inserAt(1, a))
print(L)
print(L.inserAt(2, b))
print(L)
print(L.inserAt(1, c))
print(L)

print()
print()
print()


def getLength(self):
    return self.nodeCount


def traverse(self):
    result = []
    curr = self.head
    while curr is not None:
        result.append(curr.data)
        curr = curr.next
    return result


def concat(self, L):
    self.tail.next = L.head
    if L.tail:
        self.tail = L.tail
    self.nodeCount += L.nodeCount

