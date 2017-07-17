#solve systems of equations and graph the solution
#Work in progress, stuck at 'numpy.float64' object cannot be interpreted as an integer' from the y value in line 24 to being used in line 8
import matplotlib.pyplot as plt
import numpy as np


import matplotlib.pyplot as plt
import numpy as np


def sofleq(example):
    
    for i,l in enumerate(x,y):
        fig,ax = plt.subplots(figsize=(10,10))
        plt.xlim (-10,10)
        plt.ylim (-10,10)
        ax.set_xticks(np.arange(-10,12,2))
        ax.set_yticks(np.arange(-10,12,2))
        for spine in ['left', 'bottom']:
            ax.spines[spine].set_position('zero')
        for spine in ['right','top']:
            ax.spines[spine].set_color('none')
        ax.grid(axis=10)
        ax.set_title('Vectors & Vector ops')
        ax.arrow(0,0,x[i,0],y[i,1],head_width =0.5, head_length = 0.5)
        plt.show()
        
u, v = np.array([[1,-1],[1,1]]), np.array([1,3])
x, y = np.linalg.solve(u,v)
print(u,v)
print(x,y)
sofleq(example)
