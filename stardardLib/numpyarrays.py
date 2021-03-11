import numpy as np
from numpy.core.defchararray import array
from numpy.core.fromnumeric import shape
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


import numpy as np

stdin)

Download
2 4
1 2 3 4
1 2 3 4
5 6 7 7
5 6 7 7

N, M = map(int, input().split())

A, B = input(), input()


A = np.array(A.split(), dtype='int' )
B = np.array(B.split(), dtype='int')

A.shape = dims 
B.shape = dims 


print(np.add(A, B))
print(np.subtract(A, B))
print(np.multiply(A, B))
print(np.floor_divide(A, B))
print(np.mod(A, B))
print(np.power(A, B))


a, b = (np.array([input().split() for _ in range(N)], dtype=int) for _ in range(2))

import numpy as np
n, m = map(int, input().split())

a, b = (np.array([input().split() for _ in range(n)], dtype=int) for _ in range(2))

print(a+b, a-b, a*b, a//b, a%b, a**b, sep='\n')