import numpy as np
                        # 0,1,2,3,4,5,6
new_numpy_array=np.array([1,2,3,4,5,6,7])
print(new_numpy_array) #[1 2 3 4 5 6 7]
print(type(new_numpy_array))

# slice operator on numpy
print(new_numpy_array[1]) # 2
print(new_numpy_array[3:]) # 4 5 6 7
print(new_numpy_array[3:6])

# assignment operator on numpy array
new_numpy_array[3]=100
print("new_numpy_array ",new_numpy_array) #[  1   2   3 100   5   6   7]

# to create a multidimementional array using numpy
multi_array=np.array([[1,2,3],
                      [4,5,6],
                      [7,8,9]])
print("multi dimentsional array => ",multi_array)

# accessing the elements in multi dimensional array
print("Element at index [0][0]:",multi_array[0][0])
print("Element at index [0][1]:",multi_array[0][1])
print("Element at index [0][2]:",multi_array[0][2])

print("Element at index [1][0]:",multi_array[1][0])
print("Element at index [1][1]:",multi_array[1][1])
print("Element at index [1][2]:",multi_array[1][2])

print("Element at index [2][0]:",multi_array[2][0])
print("Element at index [2][1]:",multi_array[2][1])
print("Element at index [2][2]:",multi_array[2][2])


# to print shape of the multidimensional array
print("shape of an array ",multi_array.shape) #(3,3) 3 rows and 3 columns

# to print dimenstion of an array using ndim
# ndim basically calculates the level of nesting of the array let us say in our code we have two level of the nesting so the output is 2
print("dimensions of an array is ",multi_array.ndim) # 2

