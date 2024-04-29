import numpy as np

def file_reader():
    data = np.loadtxt('con.data', delimiter=',', dtype=str)
    features = data[:, :-1]  
    labels = data[:, -1] 
    print("Features:")
    print(features)
    print("Labels:")
    print(labels)
    win_count = 0

    for i in range(len(labels)):
        if labels[i] == 'win':
            win_count += 1
    
    print(win_count)

file_reader()