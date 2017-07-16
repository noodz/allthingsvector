#Poole, 1.1 Exercises

#v2
import matplotlib.pyplot as plt
import numpy as np


#1, Draw the following vectors in std. position, in R^2: [5,-2],[-3,-2]


def cartesian(vectors):
    u,v = vectors.T.shape
    print(u,v)
    
    
    for i,l in enumerate(range(0,v)):
        fig, ax = plt.subplots(figsize=(10,10))
        for spine in ['left', 'bottom']:
            ax.spines[spine].set_position('zero')
        for spine in ['right','top']:
            ax.spines[spine].set_color('none')
        ax.grid()#grid doesnt show up, find out why; because i had axis = 10 inside the bracket and as soon as the i removed it, it was fixed.
        ax.set_title('Vectors & Vector ops')
        ax.set_xlabel('x')#needs to be at the end
        ax.set_ylabel('y')#needs to be at the end
        plt.xlim (-10,10)
        plt.ylim (-10,10)
        ax.set_xticks(np.arange(-10,12,2))
        ax.set_yticks(np.arange(-10,12,2))
        ax.arrow(0,0,vectors[i,0],vectors[i,1],head_width = 0.5, head_length = 0.5, color ='r')
        #problem was i would call plt.arrow but i set my plt.subplot to be fig, ax so i was calling an entrirely different function
        plt.show()
    
vectors = np.array([[5,-2], [-3,-2]])
print(vectors[0,:])
cartesian(vectors)
