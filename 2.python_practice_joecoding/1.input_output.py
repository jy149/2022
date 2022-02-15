'''
<함수>
def 함수명(매개변수):
    <수행할 문장1>
    <수행할 문장2>
    ...
    return 리턴 값
'''

def sum(a, b):
    result = a + b
    return result
print(sum(1,2))

def sum(a, b):
    print("%d, %d의 합은 %d 입니다." % (a,b ,a+b))
sum(1,2)

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

mylist = [1, 2, 3]
mylist.append(4)
print(mylist)
print(type(mylist.pop()))
print(mylist)

# 입력값이없는경우
def say():
    return 'Hi'
print(say())

# 여러개 입력값
def sum_many(*args): # 어떤값이 들어오든 다 더해주고 싶음
    sum = 0
    for i in args:
        sum = sum + i
    return sum
print(sum_many(1,2,3))

# 키워드 파라미터
def print_kwargs(**kwargs):
    for k in kwargs.keys():
        if(k == "name"):
            print("당신의 이름은 :" + k)
print_kwargs(name='int', b=2)

# 여러개 사용하고 골라서 뽑아쓰기
def sum_and_mul(a,b):
    return a+b, a*b, a-b
print(sum_and_mul(1,2)[1])


def say_myself(name, old, man=True):
    print("나의 이름은 %s 입니다" % name)
    print("나의 나이는 %d 입니다" % old)
    if man:
        print("남자입니다")
    else:
        print("여자입니다")

say_myself('jinyoung', 16)

# 함수안에 허용된 변수의 선언범위
a = 1
def vartest():
    global a
    a = a + 1
vartest()
print(a)

# lambda
def add(a, b):
    return a+b

add2 = lambda a,b: a+b
print(add2(1,2))

mylist = [lambda x,y: x+y, lambda x,y : x*y]
print(mylist[1](3,4))

# a = input()
# print(a)

f = open("test.txt","w", encoding='utf-8')
for i in range(1,11):
    data = "{}번째 줄입니다.\n".format(i)
    f.write(data)
f.close()

f = open("test.txt","r", encoding='utf-8')
line = f.readline()
print(line)
f.close()

f = open("test.txt","r", encoding='utf-8')
while True:
    line = f.readline()
    if not line:
        break
    print(line)
f.close()

f = open("test.txt","r", encoding='utf-8')
lines = f.readlines()
for line in lines:
    # print(line, end="")
    print(line.strip("\n"))
f.close()

f = open("test.txt","r", encoding='utf-8')
data = f.read()
print(data)
f.close()

f = open("test.txt","a", encoding='utf-8')
for i in range(11, 20):
    data = "{}번째 줄입니다.\n".format(i)
    f.write(data)
f.close()

with open("foo.txt", "w") as f:
    f.write("Life is too short, you need python")

