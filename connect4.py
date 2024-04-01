import numpy as np

who_won = 'no one'

def connect_4():
    board = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]

    for i in board:
        print(i)

    while(win(board) != True):
        decision(board, 1)
        if(win(board) == True):
            break
        decision(board, -1)
    
    print(who_won, 'won!')

def decision(board, num):
    print('Enter column to add piece')
    position = int(input())
    board = add_piece(position, board, num)
    for i in board:
        print(i)

def add_piece(position, board, num):
    count = len(board) - 1
    while count > -1:
        if board[count][position] == 0:
            board[count][position] = num
            break
        count -= 1
    return board

def win(board):
    #horizontal win
    if True == horizontal_vertical(board):
        return True

    #vertical win
    board = np.array(board)
    board = board.T
    if True == horizontal_vertical(board):
        return True

    #diagonal win
    return False

def horizontal_vertical(board):
    global who_won
    for x in board:
        player_pos = any([1, 1, 1, 1] == list(x) for x in zip(*[x[i:] for i in range(len([1, 1, 1, 1]))]))
        if player_pos == True:
            who_won = 'Player one'
            return True
        player_neg = any([-1, -1, -1, -1] == list(x) for x in zip(*[x[i:] for i in range(len([-1, -1, -1, -1]))]))
        if player_neg == True:
            who_won = 'Player two'
            return True
    return False


connect_4()