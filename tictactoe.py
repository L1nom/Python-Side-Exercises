def print_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])


def insert_board(player, position):
    if board[position - 1] == "-":
        board[position - 1] = player
        win_condition(player)
        change_player(player)
    else:
        print("Position already marked, choose somewhere else!")
        player_move(player)


def win_condition(player):
    if board[0] == board[1] == board[2] == player or board[3] == board[4] == board[5] == player or board[6] == board[7] == board[8] == player:
        print(f"Player {player} wins!")
        play_again()
    elif board[0] == board[3] == board[6] == player or board[1] == board[4] == board[7] == player or board[2] == board[5] == board[8] == player:
        print(f"Player {player} wins!")
        play_again()
    elif board[0] == board[4] == board[8] == player or board[2] == board[4] == board[6] == player:
        print(f"Player {player} wins!")
        play_again()
    else:
        change_player(player)


def game(player):
    global board
    board = ["-"] * 9
    player_move(player)


def player_move(player):
    try:
        print_board()
        position = int(input(f"{player}, choose your location 1-9\n"))
        insert_board(player, position)
    except IndexError:
        print("Invalid input location")
        player_move(player)
    except ValueError:
        print("Invalid input option")
        player_move(player)


def change_player(player):
    if player == "X":
        player_move("O")
    else:
        player_move("X")
    player_move(player)


def play_again():
    choice = input("Would you like to play again? Y/N").lower()
    if choice == "y":
        game("X")
    else:
        exit()


print("Player X is first")
game("X")