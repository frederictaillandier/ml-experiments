import matplotlib
matplotlib.use('TkAgg')

import numpy as np
from autils import *
import numpy as np
import matplotlib.pyplot as plt


def main():
       X = np.load('data/X.npy')
       X = X[0:1000]
       y = np.load('data/y.npy')
       y = y[0:1000]


       if X.size > 0: # Check if the array is not empty
            m, n = X.shape
            fig, axes = plt.subplots(8,8, figsize=(8,8))
            fig.tight_layout(pad=0.1)

            for i,ax in enumerate(axes.flat):
                # Select random indices
                random_index = np.random.randint(m)

                # Select rows corresponding to the random indices and
                # reshape the image
                X_random_reshaped = X[random_index].reshape((20,20)).T

                # Display the image
                ax.imshow(X_random_reshaped, cmap='gray')

                # Display the label above the image
                ax.set_title(y[random_index,0])
                ax.set_axis_off()
            plt.show()
       else:
           print("The NumPy array is empty.")
main()
