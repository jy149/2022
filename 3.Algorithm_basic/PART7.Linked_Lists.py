# 연결리스트(Linked Lists): 처음 배웠던 선형배열과 유사하게 생김.
'''
추상적 자료구조(Abstract Data Structures)?
Data
- 정수, 문자열, 레코드 ....

A set of operations
- 삽입, 삭제, 순회...
- 정렬, 탐색 ...

기본적인 연결 리스트
67 -> 34 -> 58
각 데이터들이 순서를 이루어 늘어서 있는데
앞에있는것이 뒤에있는 것을 가리키도록 나타나있는 것이 연결리스트이다.
각각의 아이템이 담겨있는 것을 Node 라고 부른다. 해당 Node 는 data뿐만아니라 Link(next)도 가지고 있음
data 가 정수인 67일뿐 아니라 문자열, 레코드, 또다른 연결 리스트 등이 될 수 있다.

우리가 리스트의 맨 앞인 Head를 알고 있어야 한다(여기서는 67)
또한 맨 끝 Node 를 tail(58)이라고 말해준다.
그리고 연결리스트에 노드가 몇개있는지 기록해두면 좋다.

연결리스트의 추상적자료구조를 위해서 두개의 클래스를 만들어야함
1) 하나의 Node
class Node:
    def __init__(self,item):
        self.data = item
        self.next = None

2) 링크list
class LinkedList:
    def __init__(self):
        self.nodeCount=0
        self.head = None
        self.tail = None

연산 정의
1. 특정 원소 참조(k번째)
2. 리스트 순회
3. 길이 얻어내기
4. 원소 삽입
5. 원소 삭제
6. 두 리스트 합치기

특정 원소를 참조하는 코드를 짜보자.
단순한 연결리스트 67 -> 34 -> 58 이렇게 연결되는 리스트일때(node:3, head:67, tail:58),
인덱스 시작은 1부터 하는 거로 지정하자(나중에 인덱스 0 은 다른 목적으로 이용하기 위함)
'''

# 특정 원소 참조
def getAt(self, pos):
    if pos <= 0 or pos > self.nodeCount:
        return None
    i = 1
    curr = self.head
    while i < pos:
        curr = curr.next
        i += 1
    return curr

# 연결리스트 순회?? -> 이러면 안됌, 두번쨰를 찾을때 또다시 1로가야하고,, 이러니까 다음다음다음을 찾아가는 식으로 코드구현하도록,!
def traverse(self):
    answer = []
    i = 1
    while i <= self.nodeCount:
        answer.append(self.getAt(i))
    return answer