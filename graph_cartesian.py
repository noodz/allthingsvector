#Poole, 1.1 Exercises

#v2
import matplotlib.pyplot as plt
import numpy as np


#1, Draw the following vectors in std. position, in R^2: [5,-2],[-3,-2]


def graph_cartesian(vectors, graph_ticks=(-10, 12, 2), arrow_width=0.5, 
                    graph_title="Vectors & Vector ops", position='zero', color='none'):
    '''
    Creates one graph per 2d vector inside a numpy array
    '''
    u, v = vectors.T.shape
    number_of_graphs = v
    print(u, v)
    
    for i in range(number_of_graphs): # don't need enumerate in this case, just adds noise
        max_number = max(10, abs(vectors[i, 0]), abs(vectors[i, 1])) # if the max view is greater than ten, use that to set paramerters
        min_number = min(-10, vectors[i, 0], vectors[i, 1])
        fig, ax = plt.subplots(figsize=(max_number, max_number))
        
        for spine in ['left', 'bottom']:
            ax.spines[spine].set_position(position)
        for spine in ['right','top']:
            ax.spines[spine].set_color(color)
            
        ax.grid() # grid doesnt show up, find out why; because i had axis = 10 inside the bracket and as soon as the i removed it, it was fixed.
        ax.set_title(graph_title)
        ax.set_xlabel('x') # needs to be at the end
        ax.set_ylabel('y') # needs to be at the end
        
        plt.xlim(min_number, max_number) # if we graph a number bigger than abs(10) it will now display properly
        plt.ylim(min_number, max_number)
        
        ax.set_xticks(np.arange(*graph_ticks)) # not sure why the * works but it does
        ax.set_yticks(np.arange(*graph_ticks))
        
        ax.arrow(0, 0, vectors[i, 0], vectors[i, 1], head_width = arrow_width, head_length = arrow_width, color ='r')
        #problem was i would call plt.arrow but i set my plt.subplot to be fig, ax so i was calling an entrirely different function
        plt.show()
        
#vectors = np.array([[5,-2], [-3,-2]])
#print(vectors[0,:])
#graph_cartesian(vectors)
