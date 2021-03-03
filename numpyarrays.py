import numpy as np
from numpy.core.defchararray import array
from numpy.lib.shape_base import array_split

a = np.array([1,2,3,4,5])

b = np.array([1,2,3,4,5],float)

def arrays(arr):
    arr = numpy.array(arr, float)
    return arr[::-1]

arrays(a)


def reshape(input_list):
    as_list = list(input_list.replace(" ", ''))
    my_arr = np.array(as_list, int)
    output = np.reshape(my_arr, (3,3))
    print(output)

input_list = input()
reshape(input_list)

input_list = input().split()


my_array = numpy.array(input_list)
print numpy.transpose(my_array)

def transposeNFlat(inputed):
    print(np.transpose(inputed))
    print(inputed.flatten())
    

def looper(start, stop, number):
    arr = np.linspace(start, stop, number)
    arr = list(arr)
    print(arr)
    
looper(1,5,1)
looper(1,5,2)
looper(1,5,3)
looper(1,5,4)
looper(1,5,5)


def zerosOnes(directions):
    dims = directions.split()
    dims = map(int, directions.split())
    dims = tuple(dims)
    print(np.zeros(dims, int))
    print(np.ones(dims, int))
    
directions = input()
zerosOnes(directions)



def concatenator(directions):
    
    directions = np.array(directions, int)

    arrsa = np.array([input().split()for x in range(directions[0])], int)
    arrsb = np.array([input().split()for x in range(directions[1])], int)

    print(np.concatenate((arrsa, arrsb), axis = 0))


directions = input().split()
concatenator(directions)


N, M = map(int, input().split())

import numpy as np

block1 = np.zeros((5,4))
block2 = np.ones((3,2))

# use array slicing

A = np.zeros((N,M)) 
B = np.identity(N)
A;B

print(A[0:N, 0:M] + B[0:N, 0:M])
