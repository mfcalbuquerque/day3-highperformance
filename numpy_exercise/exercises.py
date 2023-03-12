#!/usr/bin/env python3

import numpy as np


# a
print("a)")
zeros = np.zeros(10)
zeros[4] = 1
print(zeros)


# b
print("\nb)")
vec = np.arange(10, 50)
print(vec)

#c
print("\nc)")
vec_rev = vec[::-1]
print(vec_rev)

#d
print("\nd)")
mat = np.array(np.arange(9)).reshape(3,3)
print(mat)

#e
print("\ne)")
myarray = np.array([1,2,0,0,4,0])
nonzero = myarray != 0
list_of_nonzero = myarray[nonzero]
indices = [list(myarray).index(x) for x in list_of_nonzero]
print("Indices list: ", indices)

#f
print("\nf)")
random_array = np.random.randint(0,100, size=30)
print("The mean value of the 30-long array is: ",random_array.mean())

#g
print("\ng)")
array_2d = np.zeros((5,5))
array_2d[::4] = 1
array_2d[:,::4] = 1
print(array_2d)

#h
print("\nh)")
checkerboard = np.zeros((8,8))
checkerboard[::2][:, ::2] = 1
checkerboard[1::2][:, 1::2] = 1 
print(checkerboard)

#i
print("\ni)")
initial_comp = np.array([[1,0],[0,1]])
full_comp = np.tile(initial_comp, (4,4))
print(full_comp)

#j
print("\nj)")
z = np.arange(11)
z[4:8] *= -1
print(z)

#k
print("\nk)")
sort_nums = np.random.random(10)
sort_nums.sort()
print(sort_nums)

#l
print("\nl)")
A = np.random.randint(0,2,5)
B = np.random.randint(0,2,5)
equal = A == B
if np.all(equal):
    print("Both random arrays are the same.")
else:
    print("They are not the same.")
print(equal)

#m
print("\nm)")
arr_type = np.arange(10, dtype=np.int32)
print("Original type: ",arr_type.dtype)
arr_type = arr_type.astype(np.float32)
print("New type: ", arr_type.dtype)

#n
print("\nn)")
A = np.arange(9).reshape(3,3)
B = A + 1
C = np.dot(A,B)
D = C.diagonal()
print("Diagonal from the matrix multiplication A.B is: ", list(D))
