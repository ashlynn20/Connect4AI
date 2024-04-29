import numpy as np

who_won = 'no one'
count = [0, 0, 0, 0, 0, 0, 0]

def connect_4():
    board = [['o', 'o', 'o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o', 'o', 'o']]

    for i in board:
        print(i)

    while(win(board) != True):
        decision(board, 'x')
        if(win(board) == True):
            break
        decision(board, 'b')
    
    #added to convert board to gamestate to test it works
    convert_to_gamestate(board)

    print(who_won, 'won!')

#doesn't handle non integer input
def decision(board, num):
    global count
    print('Enter column to add piece')
    position = int(input())
    if(position > 6 or position < 0):
        print('Please enter a column from 0 - 6')
        position = int(input())
    temp = position
    count[temp] += 1
    if(count[temp] > 6):
        while(count[position] > 6):
            print('Column full choose new column')
            position = int(input())
            if(position > 6 or position < 0):
                print('Please enter a column from 0 - 6')
                position = int(input())
        count[temp] -= 1
        count[position] += 1
    board = add_piece(position, board, num)
    for i in board:
        print(i)

def add_piece(position, board, num):
    count = len(board) - 1
    while count > -1:
        if board[count][position] == 'o':
            board[count][position] = num
            break
        count -= 1
    return board

def win(board):
    global who_won
    #horizontal win
    if True == horizontal_vertical(board):
        return True

    #vertical win
    board = np.array(board)
    board = board.T
    if True == horizontal_vertical(board):
        return True

    #diagonal win
    board = board.T
    count = -2
    while count <= 3:
        x = np.diagonal(board, offset=count)
        player_pos_left_down = any(['x', 'x', 'x', 'x'] == list(x) for x in zip(*[x[i:] for i in range(len(['x', 'x', 'x', 'x']))]))
        if player_pos_left_down == True:
            who_won = 'Player one'
            return True
        y = np.diagonal(np.fliplr(board), offset=count)
        player_pos_left_down = any(['x', 'x', 'x', 'x'] == list(y) for y in zip(*[y[i:] for i in range(len(['x', 'x', 'x', 'x']))]))
        if player_pos_left_down == True:
            who_won = 'Player one'
            return True
        x = np.diagonal(board, offset=count)
        player_neg_left_down = any(['b', 'b', 'b', 'b'] == list(x) for x in zip(*[x[i:] for i in range(len(['b', 'b', 'b', 'b']))]))
        if player_neg_left_down == True:
            who_won = 'Player two'
            return True
        y = np.diagonal(np.fliplr(board), offset=count)
        player_neg_left_down = any(['b', 'b', 'b', 'b'] == list(y) for y in zip(*[y[i:] for i in range(len(['b', 'b', 'b', 'b']))]))
        if player_neg_left_down == True:
            who_won = 'Player two'
            return True
        count += 1
    
    return False

def horizontal_vertical(board):
    global who_won
    for x in board:
        player_pos = any(['x', 'x', 'x', 'x'] == list(x) for x in zip(*[x[i:] for i in range(len(['x', 'x', 'x', 'x']))]))
        if player_pos == True:
            who_won = 'Player one'
            return True
        player_neg = any(['b', 'b', 'b', 'b'] == list(x) for x in zip(*[x[i:] for i in range(len(['b', 'b', 'b', 'b']))]))
        if player_neg == True:
            who_won = 'Player two'
            return True
    return False

def convert_to_gamestate(board):
    
    pass


connect_4()