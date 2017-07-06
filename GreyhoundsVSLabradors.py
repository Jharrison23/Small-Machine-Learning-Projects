# An even more narrow classification between two similar things. 

# importing plot and rand. 
import numpy as np
import matplotlib.pyplot as plt

# Population - 500 dogs each breed
greyhounds = 500
labs = 500

# Height of each dog + random deviation
grey_height = 28 + 4 * np.random.randn(greyhounds)
lab_height = 24 + 4 * np.random.randn(labs)

plt.hist([grey_height, lab_height], stacked=True, color=['r','b'])
