# Write a function that takes two numbers as input and divides them.
# Handle the ZeroDivisionError exception if the second number is 0.

def divide_numbers():
    try:
        a = int(input('Enter a numerator: '))
        b = int(input('Enter the denominator: '))
        
        div = a / b 
        return div 
    
    except (ZeroDivisionError, ValueError):
        print('Error: Cannot divide by zero or non-integer input.')

result = divide_numbers()
if result is not None:
    print(f'Result: {result}')