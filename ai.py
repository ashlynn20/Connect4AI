import numpy as np

current_board_state = []
action = np.array([0,1,2,3,4,5,6])
state = np.zeros((6,7))
qTable = []

alpha = 0 ##learning rate
gamma = 0 ## discount factor
epsilon = 0 #exploration vs exploitation
num_games = 0


def qLearning_equation():
    return

def epsilon_greedy_algorithm():
    return

def input():
    return 1


def file_reader():
    data = np.loadtxt('connectData.data', delimiter=',', dtype=str)
    features = data[:, :-1]  
    labels = data[:, -1] 
    
    for i in range(len(features)):
        reward = 0
        if labels[i] == 'win':
            reward = 1
        else:
            reward = -1
        qTable.append([features[i],reward])


file_reader()
print(qTable)
        
        
print(action)
print(state)