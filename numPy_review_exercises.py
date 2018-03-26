from numpy import array
from numpy import arange
from numpy import hstack
from numpy import dot
from numpy import vstack

first_matrix = arange(3, 12)

first_matrix = first_matrix.reshape(3, 3)

print(first_matrix)

print(first_matrix.min())
print(first_matrix.max())

second_matrix = (first_matrix ** 2)

print(second_matrix)

third_matrix = (vstack([first_matrix, second_matrix]))

print(third_matrix)

print(dot(third_matrix, first_matrix))

print(third_matrix.reshape(3,3,2))
