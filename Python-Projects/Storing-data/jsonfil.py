from pathlib import Path
import json

numbers = [2, 3, 5, 7, 11, 13]

path = Path('numbers.json')
contents = json.dumps(numbers)
path.write_text(contents)

path = Path('numbers.json')
contents = path.read_text()
numbers = json.loads(contents)

print(numbers)

print('\n')

path = Path('num.csv')
num = input('Num: ')
contents = json.dumps(num)
path.write_text(contents)

print('\n')

path = Path('num.txt')
contents = path.read_text()
num = json.loads(contents)
print(num)