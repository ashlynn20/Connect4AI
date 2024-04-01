import numpy as np

who_won = 'no one'

def connect_4():
    board = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
    count = -1

    for i in board:
        print(i)

    while(win(board) != True):
        count += 1
        if count % 2 == 0:
            print('Enter column to add piece')
            position = int(input())
            board = add_piece_player_one(position, board)
            for i in board:
                print(i)
        else:
            print('Enter column to add piece')
            position = int(input())
            board = add_piece_player_two(position, board)
            for i in board:
                print(i)
    
    print(who_won, 'won!')

def add_piece_player_one(position, board):
    count = len(board) - 1
    while count > -1:
        if board[count][position] == 0:
            board[count][position] = 1
            break
        count -= 1
    return board

def add_piece_player_two(position, board):
    count = len(board) - 1
    while count > -1:
        if board[count][position] == 0:
            board[count][position] = -1
            break
        count -= 1
    return board

def win(board):
    global who_won
    #horizontal win
    for x in board:
        player_pos = any([1, 1, 1, 1] == list(x) for x in zip(*[x[i:] for i in range(len([1, 1, 1, 1]))]))
        if player_pos == True:
            who_won = 'Player one'
            return True
        player_neg = any([-1, -1, -1, -1] == list(x) for x in zip(*[x[i:] for i in range(len([-1, -1, -1, -1]))]))
        if player_neg == True:
            who_won = 'Player two'
            return True
    #vertical win
    board = np.array(board)
    board = board.T
    for x in board:
        player_pos = any([1, 1, 1, 1] == list(x) for x in zip(*[x[i:] for i in range(len([1, 1, 1, 1]))]))
        if player_pos == True:
            who_won = 'Player one'
            return True
        player_neg = any([-1, -1, -1, -1] == list(x) for x in zip(*[x[i:] for i in range(len([-1, -1, -1, -1]))]))
        if player_neg == True:
            who_won = 'Player two'
            return True
        
    #diagonal win
    return False


connect_4()