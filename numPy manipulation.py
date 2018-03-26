from numpy import arange
from numpy import array
from numpy import random
from numpy import dot
from numpy import vstack, hstack

matrix = array([[1,2,3], [4,5,6], [7,8,9]])
print(matrix)

print(matrix[0][1]) #also can use matrix[0,1]

#array is different form a list because it can only hold similar entries (for instance, all nubers) whereas we could throw any sort of objects together into a list


matrix2 = [
    [[1,2,3], [4,5,6]],
    [[7,8,9], [10,11,12]],
    [[14,15,16], [17,18,19]]
]
print(matrix2[0],[1],[2])

matrix = array([[1,2,3], [4,5,6], [7,8,9]])
print(matrix*2)

second_matrix = array([[5,4,3], [7,6,5], [9,8,7]])
print(second_matrix-matrix)
#using the arrary function you can simply perform matrix arithmetic

print(second_matrix * matrix)

print(dot(second_matrix, matrix))

print(vstack([matrix, second_matrix]))

print(hstack([matrix, second_matrix]))

print(matrix.shape) # a tuple of the axis lengths (3 x 3)

print(matrix.diagonal()) # array of the main diagonal entries

print(matrix.flatten()) # a flat array of all entries

print(matrix.transpose()) # mirror-image along the diagonal

print(matrix.min()) # the minimum entry

print(matrix.max()) # the maximum entry

print(matrix.mean()) # the average value of all entries

print(matrix.sum()) # the total of all entries

print(matrix.reshape(9,1))

matrix = arange(1,10) #an array of numbers 1 through 9

print(matrix)

matrix = matrix.reshape(3,3)

print(matrix)

array_3d = arange(1,13)
array_3d = array_3d.reshape(3,2,2)

print(random.random([3,3]))
