from models import Board


def play():
    board = Board()
    print("Tic Tac Toe")
    print("X starts.")
    get_turn_input(board, 1)


def get_turn_input(board, player):
    print(board.board)
    row = int(input("Row (1 - 3): "))
    if row < 1 or row > 3:
        print("Invalid input, try again.")
        row = int(input("Row (1 - 3): "))
    col = int(input("Column (1 - 3): "))
    if col < 1 or col > 3:
        print("Invalid input, try again.")
        row = int(input("Row (1 - 3): "))
    if player == 1:
        if board.positions[row-1][col-1] == " ":
            board.place_x(row, col)
            check_win(board)
            return get_turn_input(board, 2)
        else:
            print("This place is already taken, please try again:")
            return get_turn_input(board, 1)
    if player == 2:
        if board.positions[row - 1][col - 1] == " ":
            board.place_o(row, col)
            check_win(board)
            return get_turn_input(board, 1)
        else:
            print("This place is already taken, please try again:")
            return get_turn_input(board, 2)


def check_win(board: Board):
    mtx = board.positions
    all_positions = []
    for row in mtx:
        for mark in row:
            all_positions.append(mark)
    for row in mtx:
        if row[0] == row[1] == row[2] != " ":
            print(board.board)
            print(f"{row[0]} wins!")
            return play_again()
    for n in range(3):
        col = [row[n] for row in mtx]
        if col[0] == col[1] == col[2] != " ":
            print(board.board)
            print(f"{col[0]} wins!")
            return play_again()
    if mtx[0][0] == mtx[1][1] == mtx[2][2] != " ":
        print(board.board)
        print(f"{mtx[0][0]} wins!")
        return play_again()
    if mtx[2][0] == mtx[1][1] == mtx[0][2] != " ":
        print(board.board)
        print(f"{mtx[2][0]} wins!")
        return play_again()
    if " " not in all_positions:
        print(board.board)
        print("It's a draw!")
        return play_again()


def play_again():
    print("Do you want to play another game?")
    user_input = input("y or n: ")
    if user_input == "y":
        play()
    else:
        exit(0)
