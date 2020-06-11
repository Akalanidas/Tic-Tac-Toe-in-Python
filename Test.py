Board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
win_condition = False
p1_condition = False
p2_condition = False


def print_Board():
    print(Board[0], Board[1], Board[2])
    print(Board[3], Board[4], Board[5])
    print(Board[6], Board[7], Board[8])


def p1_turn():
    print_Board()

    user_input = input("\nP1, please choose where to place your symbol: ")

    try:
        index = Board.index(user_input)
        Board[index] = "X"

    except:
        print("please choose an empty field.")
        p1_turn()


def p2_turn():
    print_Board()

    user_input = input("\nP2, please choose where to place your symbol: ")

    try:
        index = Board.index(user_input)
        Board[index] = "U"

    except:
        print("please choose an empty field.")

        p2_turn()


def p1_conditions():
    condition_1 = Board[0] == "X" and Board[1] == "X" and Board[2] == "X"
    condition_2 = Board[3] == "X" and Board[4] == "X" and Board[5] == "X"
    condition_3 = Board[6] == "X" and Board[7] == "X" and Board[8] == "X"

    condition_4 = Board[0] == "X" and Board[3] == "X" and Board[6] == "X"
    condition_5 = Board[1] == "X" and Board[4] == "X" and Board[7] == "X"
    condition_6 = Board[2] == "X" and Board[5] == "X" and Board[8] == "X"

    condition_7 = Board[0] == "X" and Board[4] == "X" and Board[8] == "X"
    condition_8 = Board[6] == "X" and Board[4] == "X" and Board[2] == "X"

    def winner():

        global p1_condition

        if condition_1:
            p1_condition = True

        elif condition_2:
            p1_condition = True

        elif condition_3:
            p1_condition = True

        elif condition_4:
            p1_condition = True

        elif condition_5:
            p1_condition = True

        elif condition_6:
            p1_condition = True

        elif condition_7:
            p1_condition = True

        elif condition_8:
            p1_condition = True

        else:
            p1_condition = False

    winner()


def p2_conditions():
    condition_1 = Board[0] == "U" and Board[1] == "U" and Board[2] == "U"
    condition_2 = Board[3] == "U" and Board[4] == "U" and Board[5] == "U"
    condition_3 = Board[6] == "U" and Board[7] == "U" and Board[8] == "U"

    condition_4 = Board[0] == "U" and Board[3] == "U" and Board[6] == "U"
    condition_5 = Board[1] == "U" and Board[4] == "U" and Board[7] == "U"
    condition_6 = Board[2] == "U" and Board[5] == "U" and Board[8] == "U"

    condition_7 = Board[0] == "U" and Board[4] == "U" and Board[8] == "U"
    condition_8 = Board[6] == "U" and Board[4] == "U" and Board[2] == "U"

    def winner():

        global p2_condition

        if condition_1:
            p2_condition = True

        elif condition_2:
            p2_condition = True

        elif condition_3:
            p2_condition = True

        elif condition_4:
            p2_condition = True

        elif condition_5:
            p2_condition = True

        elif condition_6:
            p2_condition = True

        elif condition_7:
            p2_condition = True

        elif condition_8:
            p2_condition = True

        else:
            p2_condition = False

    winner()


def check_win():
    global win_condition

    if p1_condition:
        print("p1 wins!")
        win_condition = True

    if p2_condition:
        print("p2 wins!")
        win_condition = True


def game():
    global win_condition
    global Board

    while not win_condition:
        p1_turn()
        p1_conditions()
        check_win()

        if p1_condition:
            break

        p2_turn()
        p2_conditions()
        check_win()

    if win_condition:
        game_restart = input("Do you want to play another round?\ny/n ")

        if game_restart == "y":
            win_condition = False
            Board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            game()


game()