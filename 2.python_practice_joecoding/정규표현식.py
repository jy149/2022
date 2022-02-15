# 주민등록번호 뒷자리 * 문자 변경
data = '''
park 921117-1020202
kim 982218-2029391
'''

result = []
for line in data.split('\n'):
    word_result = []
    for word in line.split(" "):
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            word = word[:6]+'-'+'*******'
        word_result.append(word)
    result.append(" ".join(word_result))
print("\n".join(result))

# 정규표현식으로 표현하면?
import re
pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******", data))

# 정규표현식은?
# 문자열의 규칙을 찾아서 일치하는 것을 뭐로 바꿔라~~
# 문자가 규칙에 매치되는지 검사하는 수식이 있음
'''
---------------------------------------------------------------------------------
문자 클래스 []
[abc]

- [] 사이의 문자들과 매치
- "a"는 정규식과 일치하는 문자인 "a"가 있으므로 매치
- "before"는 정규식과 일치하는 문자인 "b"가 있으므로 매치
- "dude"는 정규식과 일치하는 문자인 a, b, c 중 어느 하나도 포함하고 있지 않으므로 매칭 x
- 하이픈을 사용하여 From-To 표현 가능 
    - Ex) [a-c] = [abc], [0-5] = [12345]

---------------------------------------------------------------------------------
Dot(.)
a.b

- 줄바꿈(\n)을 제외한 모든 문자와 매치
- "aab"는 가운데 문자 "a"가 모든 문자를 의미하는 '.'과 일치하므로 정규식과 매치
- "a0b"는 가운데 문자 "0"가 모든 문자를 의미하는 '.'과 일치하므로 정규식과 매치
- "abc"는 "a"문자와 "b"문자 사이에 어떤 문자라도 하나는 있어야 하는 이 정규식과 일치하지 않으므로 매칭 X

---------------------------------------------------------------------------------
반복(*)
ca*t
- "ct"는 "a"가 0번 반복되어 매치
- "cat"는 "a"가 0번 이상 반복되어 매치(1번 반복)
= "caaaat"는 "a"가 0번 이상 반복되어 매치(4번반복)

반복(+) 
ca+t <0번반복은 매칭 X>
- "ct"는 "a"가 0번 반복되어 매칭 X
- "cat"는 "a"가 0번 이상 반복되어 매치(1번 반복)
= "caaaat"는 "a"가 0번 이상 반복되어 매치(4번반복)

반복({m, n}, ?)
ca{2}t
- "cat"는 "a"가 1번만 반복되어 매칭 X
- "caat"는 "a"가 두번 반복되어 매치

ca{2,5}t <a가 2이상 5이하만 매칭>
- "cat"는 "a"가 1번만 반복되어 매칭 X
- "caat"는 "a"가 2번 반복되어 매치
- "caaaaat"는 "a"가 5번 반복되어 매치

ab?c <b가 0번 혹은 1번사용된것을 매칭> -> ?는 {0,1}과 같은 의미로 보면 된다.
- "abc"는 "b"가 1번 사용되어 매치
- "ac"는 "b"가 0번 사용되어 매치
'''

# 정규표현식을 지원하는 re 모듈
import re
p = re.compile('ab*')

# 패턴객체를 이용하는 네 가지 방법
# Match
# Search
# Findall
# Finditer

# 1. Match
import re
p = re.compile('[a-z]+') # a부터 z까지문자열 나온것이 1번이상 반복된것을 찾는 식
m = p.match('python')
# m = p.match('3python') # 매치가 되지 않는것 -> none 표현
print(m)

# 2. Search
import re
p = re.compile('[a-z]+')
# s = p.search('python')
s = p.search('3python') # search의 경우 match와 다르게 검색하는 느낌이라서 전부 일치하지 않더라도 일치하는 부분만 찾아서 보여줌
print(s)

# 3. findall
import re
p = re.compile('[a-z]+')
fa = p.findall('life is too short') # 일치하는 str을 list로 return해준다
print(fa)

# 4. finditer
import re
p = re.compile('[a-z]+')
fi = p.finditer('life is too short') # for문을 통해서 하나씩 출력 가능
for i in fi:
    print(i)

'''
match 객체의 메서드1
method / 목적
1) group() : 매치된 문자열을 리턴한다.
2) start() : 매치된 문자열의 시작 위치를 리턴한다.
3) end() : 매치된 문자열의 끝 위치를 리턴한다.
4) span() : 매치된 문자열의 (시작,끝)에 해당되는 튜플을 리턴한다.
'''
import re
p = re.compile('[a-z]+')
m = p.match('python')
print(m.group())
print(m.start())
print(m.end())
print(m.span())


# 컴파일 옵션
# 1) DOTALL, S
# 이렇게 그냥 쓰면 . 부분에 줄바꿈(\n)문자 인식 안하게 됌
import re
p = re.compile('a.b')
m = p.match('a\nb')
print(m)

# 하지만 DOTALL 옵션을 준다면? -> 매칭가능(dot문자가 줄바꿈도 포함하도록)
import re
p = re.compile('a.b', re.DOTALL)
# p = re.compile('a.b', re.S)
m = p.match('a\nb')
print(m)

# 2) IGNORECASE, I -> 대소문자 무시하고 매칭
import re
p = re.compile('[a-z]')
print(p.match('python'))
print(p.match('Python')) # none
print(p.match('PYTHON')) # none

import re
p = re.compile('[a-z]', re.I) # 대소문자 무시하고 매칭
print(p.match('python'))
print(p.match('Python'))
print(p.match('PYTHON'))
print()

# 3) MULTILINE, M
import re
p = re.compile("^python\s\w+") # ^ : 맨앞에 python이라는 문자가 나오고,
                               # \s: 다음으로 공백문자가 나오고
                               # \w+: 문자가 반복되야함
data = '''python one
life is too short
python two
you need python
python three
'''
print(p.findall(data))

import re
p = re.compile("^python\s\w+", re.M) # 멀티라인옵션줘서 세개가잡힘, 즉 뒤의 줄도 새로운줄의 맨 처음으로 인식하게됌
data = '''python one
life is too short
python two
you need python
python three
'''
print(p.findall(data))

# 4) VERBOSE, X
import re
charref = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')
charref = re.compile(r'''
&[#]
(
    0[0-7]+
    |[0-9]+
    |x[0-9a-fA-F]+
)
;
''', re.VERBOSE) # 긴 표현식을 나눠줄 수 있음

# 백슬래시 문제
'''
\section

p = re.compile('\\section')
p = re.compile('\\\\section')
p = re.compile(r'\\section')
'''

# 강력한 정규표현식
# 메타문자 |
# -> compile 시 or의 뜻으로 앞의꺼 또는 뒤에꺼를 의미
import re
p = re.compile('Crow|Servo')
m = p.match('CrowHello')
print(m)

# 메타문자 ^
import re
print(re.search('^Life', 'Life is too short'))
print(re.search('^Life', 'My Life'))