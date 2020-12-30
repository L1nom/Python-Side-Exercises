"""
program that takes user input to print
ascending or descending stars of their
desired size
"""


def ascending(rows):
    output = ""
    i = 0
    while i <= rows:
        output += i * "*" + "\n"
        i += 1
    return output


def descending(rows):
    output = ""
    i = rows
    while i >= 0:
        output += i * "*" + "\n"
        i -= 1
    return output


try:
    n = int(input("Enter a number\n"))
    s = int(input("Type 1 for ascending stars or 2 for descending stars\n"))
    if s == 1:
        print(ascending(n))
    else:
        print(descending(n))
except ValueError:
    print("Please enter a whole number")

