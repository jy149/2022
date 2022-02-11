'''
1-1. 파이썬 print 사용법(1-1)
- Separator
- End
- Python Format
'''

# 기본 출력
print('Python Start!')
print("Python Start!")
print('''Python Start!''')
print("""Python Start!""")
print()

# sparator 옵션
print('P', 'Y', 'T', 'H', 'O', 'N', sep=' ')
print('010','7777','1234',sep='-')
print('python','google.com',sep='@')
print()

# end 옵션
print('Welcome to', end=' ') # end옵션을이용하여 다음 print문을 제어 가능
print('IT News', end=' ')
print('Web Site')
print()

# file 옵션
import sys
print('Learn Python', file=sys.stdout) # file옵션은 파일읽기할때 씀 현재 내용을 외부 파일로쓸꺼다 이런거임
                                       # sys.stdout은 콘솔옵션을 말함
print()

# format 사용(d, s, f)
# d->digit(정수) s->string(문자열), f->float(소수)
# d : 3, s : 'python', f : 3.141592
print('%s %s' % ('one', 'two'))    # % 가 다리역할을 해줌
print('{} {}'.format('one','two')) # format함수를 사용함
print('{1} {0}'.format('one', 'two')) # 0번쨰가 one이고 1번째가 two임. 순서를 지정 가능
print()

# %s
print('%10s' % 'nice') # 10이의미하는것은 자릿수를 의마한다.
print('{:>10}'.format('nice')) # :>사용

print('%-10s' % 'nice') # 숫자에 음수가 오게되면 왼쪽부터 채우게 된다
print('{:10}'.format('nice')) # 부등호 없애면 왼쪽부터 채움

print('{:_>10}'.format('nice')) # 공백을 원하는 기호로 채우기 가능
print('{:@>10}'.format('nice')) # 공백을 원하는 기호로 채우기 가능
print('{:^10}'.format('nice')) # :^ 이거는 중앙정렬

print('%.5s' % ('pythonstudy')) # .5가 붙게되면 .뒤의 숫자만큼 절삭
print('{:10.5}'.format('pythonstudy')) # 공간은 10개를 갖되 5글자 절삭
print()

# %d
print('%d %d' % (1,2))
print('{} {}'.format(1,2))

print('%4d' % (42))
print('{:4d}'.format(42))
print()

# %f
print('%f' % 3.12312312)
print('%1.2f' % 3.12314648) # 정수부와 소수부 지정가능
print('{:1.2f}'.format(3.43151))

print('%06.2f' % (3.141592653589793)) # 6자리까지 나타내는데 공백자리는 0으로 채우게 된다
print('{:06.2f}'.format(3.141592653589793))
print()






































































































