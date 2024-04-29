import numpy as np

who_won = 'no one'
count = [0, 0, 0, 0, 0, 0, 0]

def connect_4():
    board = [['b', 'b', 'b', 'b', 'b', 'b', 'b'], ['b', 'b', 'b', 'b', 'b', 'b', 'b'], ['b', 'b', 'b', 'b', 'b', 'b', 'b'], ['b', 'b', 'b', 'b', 'b', 'b', 'b'], ['b', 'b', 'b', 'b', 'b', 'b', 'b'], ['b', 'b', 'b', 'b', 'b', 'b', 'b']]

    for i in board:
        print(i)
    moves = 0
    while(win(board) != True):
        if moves == 8:
            pattern = convert_to_gamestate(board)
            file_reader(pattern)
        decision(board, 'x')
        moves += 1
        if(win(board) == True):
            break
        decision(board, 'o')
        moves += 1

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
        if board[count][position] == 'b':
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
        player_neg_left_down = any(['o', 'o', 'o', 'o'] == list(x) for x in zip(*[x[i:] for i in range(len(['o', 'o', 'o', 'o']))]))
        if player_neg_left_down == True:
            who_won = 'Player two'
            return True
        y = np.diagonal(np.fliplr(board), offset=count)
        player_neg_left_down = any(['o', 'o', 'o', 'o'] == list(y) for y in zip(*[y[i:] for i in range(len(['o', 'o', 'o', 'o']))]))
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
        player_neg = any(['o', 'o', 'o', 'o'] == list(x) for x in zip(*[x[i:] for i in range(len(['o', 'o', 'o', 'o']))]))
        if player_neg == True:
            who_won = 'Player two'
            return True
    return False

def convert_to_gamestate(board):
    gamestate = []
    for row in board:
        for column in row:
            gamestate.append(column)

    return gamestate

def file_reader(pattern):
    data = np.loadtxt('connectData.data', delimiter=',', dtype=str)
    features = data[:, :-1]  
    labels = data[:, -1] 
    
    for i in range(len(features)):
        if np.array_equal(features[i], pattern):
            #could throw in condition here that determines f it's a win and rewards based on it
            print("found")

connect_4()