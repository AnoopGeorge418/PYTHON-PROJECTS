# Create a text file with some content.
# Open the file in Python and read its contents.
# Print the contents to the console.

file = open('File.txt', 'r')
print(file.read())

file.close()