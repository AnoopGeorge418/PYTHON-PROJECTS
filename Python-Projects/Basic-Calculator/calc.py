import sys

def Simple_Calculator():
    try:
        while True:
            num1 = int(input('Enter a number: '))
            operations = ['+', '-', '*', '/', '**']
            operation = input(f'Choose the operation you want to perform {operations}: ')
            num2 = int(input('Enter another number: '))
            
            if operation == '+':
                addition(num1, num2)
            elif operation == '-':
                subtraction(num1, num2)
            elif operation == '*':
                multiplication(num1, num2)
            elif operation == '/':
                division(num1, num2)
            elif operation == '**':
                power(num1, num2)
            else:
                print(f'This operation is not yet available select from {operations}')
            
            try_again = input('Do you want to perform another calculation? (y/n): ').lower()
            if try_again != 'y':
                print('Exiting from calculator')
                break
            
    except ValueError:
        print('Please Enter a number')
    except (KeyboardInterrupt, EOFError):
        print('Exiting from calculator')


def addition(a, b):
    print(f'Answer: {a + b}')

def subtraction(a, b):
    print(f'Answer: {a - b}')

def multiplication(a, b):
    print(f'Answer: {a * b}')

def division(a, b):
    if b == 0:
        print('Not Divisible by 0')
    else:
        print(f'Answer: {a / b}')
    
def power(a, b):
    print(f'Answer: {a ** b}')

def main():
    Simple_Calculator()
        
if __name__ == '__main__':
    main()