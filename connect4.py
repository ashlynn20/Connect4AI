
def connect_4():
    board = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
    for i in board:
        print(i)
    print('Enter column to add piece')
    position = int(input())
    board = add_piece(position, board)
    for i in board:
        print(i)

def add_piece(position, board):
    count = len(board) - 1
    while count > -1:
        if board[count][position] == 0:
            board[count][position] = 1
            break
        count -= 1
    return board
connect_4()