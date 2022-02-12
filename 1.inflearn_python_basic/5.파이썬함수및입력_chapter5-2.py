# Chapter 5-2. 사용자입력(input)
'''
Input 사용법
- 사용자 입력
- 형 변환 입력
- 입출력 실습
'''

# 예제 1
name = input("Enter Your Name")
grade = input("Enter Your Grade")
company = input("Enter Your Company Name")

print(name, grade, company)

# 예제 2
number = input('Enter number : ')
name = input('Enter name : ')

print("type of number: ", type(31))
print("type of name: ", type(name))

# 예제 3
first_number = int(input("Enter number1: "))
second_number = int(input("Enter number2: "))

total = first_number + second_number
print("first_number + second_number: ", total)


# 예제 4
float_number = float(input("Enter a float number: "))
print("input float : ", float_number)
print("input type : ", type(float_number))

# 예제 5
print("FirstName - {0}, LastName = {1}".format(input("Enter first name"), input("Enter last name")))












