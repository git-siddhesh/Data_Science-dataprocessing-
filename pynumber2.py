'''create a numpy array of  8x2 as having number  in each cell between 100 and 200 
   such that difference between each element is 5 
Note : The question is incompete according to me. It is not specified whether the difference between 
       two consecutive numbers or any two consecutive rows
          By clearifing the perfect question my solution will be change
'''


'''Currently I made an ndarray of 16 numbers having step size of 5 starting from 100 and of shape: 8x2''' 
import numpy as np 
a=np.arange(100,200,5)[:16]
a.reshape((8,2))

output: 
array([[100, 105],
       [110, 115],
       [120, 125],
       [130, 135],
       [140, 145],
       [150, 155],
       [160, 165],
       [170, 175]])
