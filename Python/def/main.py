# main.py

from if .sub import a, b, c, d

num1, num2 = map(int, input('숫자를 입력하세요 : ').split(' '))
operator = input('연산 기호를 입력하세요 : ')

def main():
    if operator == '+':
        print(a(num1, num2))
    elif operator == '-':
        print(b(num1, num2))
    elif operator == '*':
        print(c(num1, num2))
    elif operator == '//':
        print(d(num1, num2))
    else:
        print('error')

main()