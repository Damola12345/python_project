# python program
# building basic calculator

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
opera = input('Enter operator: ')

if opera == '+':
    print('The addition is', num1+num2)
elif opera == '-':
    print('The subtraction is', num1-num2)
elif opera == '*':
    print('The multiplication is', num1*num2)
elif opera == '/':
    print('The division is', num1/num2)
else:
    print('Invalid operator')

