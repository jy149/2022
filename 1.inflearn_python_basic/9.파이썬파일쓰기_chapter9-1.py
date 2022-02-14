# Chapter 9-1. File Write
# 파일 읽기 및 쓰기

# 읽기 모드: r, 쓰기 모드: w, 추가 모드: a, 텍스트 모드: t, 바이너리 모드: b
# 상대 경로('../', './'), 절대 경로('C:\Django\example..')

# 파일 읽기(Read)
# 예제 1

#f = open(r'C:\Users\user\Desktop\2022\1.inflearn_python_basic\resource\it_news.txt')
f = open('./resource/it_news.txt', 'rt', encoding = 'UTF-8')

# 속성 확인
print(dir(f))
# 인코딩 확인
print(f.encoding)
# 파일 이름
print(f.name)
# 모드 확인
print(f.mode)

cts = f.read()
print(cts)
# 반드시 close
f.close()
print()

# 예제 2
with open('./resource/it_news.txt', 'rt', encoding = 'UTF-8') as f:
    c = f.read()
    print(c)
    print(iter(c))
    print(list(c))
print()

# 예제 3
# read(): 전체 읽기, read(10): 10 Byte 만 읽어옴
with open('./resource/it_news.txt', 'rt', encoding = 'UTF-8') as f:
    c = f.read(20)
    print(c)
    c = f.read(20)
    print(c)
    c = f.read(20)
    print(c) # 마지막에 어디까지 읽었는지 커서처럼 기억하고있음

    f.seek(0,0) # 다시 처음으로 돌아옴
    c = f.read(20)
    print(c)
print()

# 예제 4
# readline: 한 줄씩 읽어옴
with open('./resource/it_news.txt', 'rt', encoding = 'UTF-8') as f:
    line = f.readline()
    print(line)
    line = f.readline()
    print(line)
print()

# 예제 5
# readlines : 전체를 읽은 후 라인 단위 리스트로 저장!!!!
with open('./resource/it_news.txt', 'rt', encoding = 'UTF-8') as f:
    cts = f.readlines()
    print(cts)
    print()
    for c in cts:
        print(c, end='')
print()

# 파일 쓰기(write)
# 예제 1
with open('./resource/contents1.txt', 'wt') as f:
    f.write('I Love Python\n')

# 예제 2 : a를 쓰면 내용 추가됌
with open('./resource/contents1.txt', 'at') as f:
    f.write('I Love Python\n')

# 예제 3
# writelines : 리스트 -> 파일로 쓸 수 있음
with open('./resource/contents2.txt', 'w') as f:
    list = ['Orange\n', 'Apple\n', 'Banana\n', 'Melon\n']
    f.writelines(list)

# 예제 4
with open('./resource/contents2.txt', 'a') as f:
    print('Test Text Write!', file=f)
    print('Test Text Write!', file=f)
    print('Test Text Write!', file=f)

