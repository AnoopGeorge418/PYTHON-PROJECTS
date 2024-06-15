# Guest: Write a program that prompts the user for their name. When they
# respond, write their name to a file called guest.txt.

from pathlib import Path

name = input("Please enter your name: ")

file_path = Path("guest.txt")
with file_path.open(mode="a") as file:
    file.write(name)

print(f"Your name has been written to {file_path}")