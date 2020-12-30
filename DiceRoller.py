import random


def dice(num):
    print("-----------")
    if num == 1:
        print("|         |")
        print("|    0    |")
        print("|         |")
    if num == 2:
        print("| 0       |")
        print("|         |")
        print("|       0 |")
    if num == 3:
        print("| 0       |")
        print("|    0    |")
        print("|       0 |")
    if num == 4:
        print("| 0     0 |")
        print("|         |")
        print("| 0     0 |")
    if num == 5:
        print("| 0     0 |")
        print("|    0    |")
        print("| 0     0 |")
    if num == 6:
        print("| 0     0 |")
        print("| 0     0 |")
        print("| 0     0 |")
    print("-----------")


def play():
    try:
        choice = int(input("How many die do you want to roll?"))
        total = 0
        for i in range(choice):
            die = random.randint(1, 6)
            dice(die)
            total += die
        print(f"Your total roll is: {total}")
    except ValueError:
        print("Please type a valid integer")
        play()


play()
