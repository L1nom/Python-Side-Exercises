"""
Simple Python program to play hangman.
Player 1 wil input a word for player 2 to guess

"""


def hangman(word):
    wrong = 0
    stages = ["",
              "________         ",
              "|                ",
              "|       |        ",
              "|       0        ",
              "|      /|\       ",
              "|      / \       ",
              "|                "
              ]
    remainingLetters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman!")

    while wrong < len(stages) - 1:
        print("\n")
        char = input("Guess a letter in the word\n")
        if char in remainingLetters:
            cind = remainingLetters.index(char)
            board[cind] = char
            remainingLetters[cind] = "$"
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("You won the game!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong]))
        print("You lose! It was {}.".format(word))


wordToGuess = input("Player 1, input a word to guess!\n")
hangman(wordToGuess)