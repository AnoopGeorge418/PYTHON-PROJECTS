# Create a new text file.
# Write some text to the file using Python.
# Open the file in a text editor to verify the content.

file = open('File1.txt', 'w')
file.write('Python is Easy and interesting to learn through as projects.')

file.close()

# reading created file
read_file = open('File1.txt', 'r')
print(read_file.read())

read_file.close()