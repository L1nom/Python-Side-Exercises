"""
Write a function called fizz_buzz
If the number is divisible by 3, output fizz
If the number is divisible by 5, output buzz
If the number is divisible by both, print both
Else, return the original number back
"""


def fizz_buzz(num):
    for i in range(1, num + 1):
        output = ""
        if i % 3 == 0:
            output += "Fizz"
        if i % 5 == 0:
            output += "Buzz"
        if output == "":
            output = i
        print(output)


try:
    num = int(input("Please enter a number\n"))
    fizz_buzz(num)
except ValueError:
    print("Please input a integer number\n")
