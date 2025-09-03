num_list=[9, 38, 83, 10, 28, 14, 33, 5, 82, 43]
# map function 
#syntax map(function, iterable)

def print_square(x):
    return x*x
print_square_num=list(map(print_square,num_list)) 
print(print_square_num) #[81, 1444, 6889, 100, 784, 196, 1089, 25, 6724, 1849]


# above code can also be written using the lamda function 
find_square=lambda x:x*x
print_sqaure=list(map(find_square,num_list))
print(print_sqaure)# [81, 1444, 6889, 100, 784, 196, 1089, 25, 6724, 1849]



print('===============================================================================================')
#filter method 
num_list1=[2,4,4,5,5,5,2,1,6,6,8]
def num_greater(x):
    return x>5
print_num_greater=list(filter(num_greater,num_list1))
print("number greater than 5 ",print_num_greater) # [6, 6, 8]

def filter_values(x):
    return x%2==0
find_even_num_list=list(filter(filter_values,num_list1)) #[2, 4, 4, 2, 6, 6, 8]
print(find_even_num_list)


# =================================================================================================================================
# above two codes can be written using lamda function
find_greater=lambda x:x>5
output=list(filter(find_greater,num_list1))
print("output",output) #[6, 6, 8]

#printing oddnumbers in the list
find_odd_num=list(filter(lambda x:x%2!=0 ,num_list1))
print(find_odd_num) # [5, 5, 5, 1]

print("==========================================================================================")

# reduce is a higher order function which applied to the sequence/iterable such as the list and returns a single values
# it is not directly a part of the python to use this reduce we need to import it from the funtools 
from functools import reduce
number_list=[1,2,3,4,5,6,7,8,9,10]
def sum_of_values(x,y):
    return x+y
reduce_exa=reduce(sum_of_values,number_list)
print(reduce_exa)