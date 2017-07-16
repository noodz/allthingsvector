#solve systems of equations and graph the solution
import matplotlib.pyplot as plt
import numpy as np


def sofleq(example):
    x,y = example
    for i,l in enumerate(range(0,y)):
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
        ax.arrow(0,0,example[i,0],example[i,1],head_width =0.5, head_length = 0.5)
        plt.show()
        
x, y = np.array([[1,-1],[1,1]]), np.array([1,3])
example = np.linalg.solve(x,y)
print(x,y)
print(example)
sofleq(example)
