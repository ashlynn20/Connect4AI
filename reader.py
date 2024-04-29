import numpy as np

def file_reader(pattern):
    data = np.loadtxt('connectData.data', delimiter=',', dtype=str)
    features = data[:, :-1]  
    labels = data[:, -1] 
    print("Features:")
    print(features)
    print("Labels:")
    print(labels)
    
    for i in range(len(features)):
        if np.array_equal(features[i], pattern):
            #could throw in condition here that determines f it's a win and rewards based on it
            print("found")

file_reader()