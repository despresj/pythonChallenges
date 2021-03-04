import numpy as np
from numpy.core.fromnumeric import argmax, argmin

"""
[[1,  6, 11],
 [2,  7, 12],
 [3,  8, 13],
 [4,  9, 14],
 [5, 10, 15]]

"""

np.arange(1, 16).reshape(3,5).T
a = np.arange(25).reshape(5, 5)

b = a.T[0]
b

"""
Harder one: Generate a 10 x 3 array of random numbers 
(in range [0,1]). For each row, pick the number closest to 0.5.
Use abs and argsort to find the column j closest for each row.
Use fancy indexing to extract the numbers. (Hint: a[i,j] – the
array i must contain the row numbers corresponding to stuff in j.)
"""

np.random(1, 0)

arr = np.random.uniform(0, 1, 30).reshape(10, 3)

b = np.argmin(abs(a - .5), axis=1).choose(a.T)

a = np.random.rand(10,3)
b = np.argmin(abs(a - .5), axis=1).choose(a.T)



#%%
from scipy import misc
face = misc.face(gray=True) 
face

import matplotlib.pyplot as plt
face = misc.face(gray=True)
plt.imshow(face)    
plt.imshow(face, cmap=plt.cm.gray)   