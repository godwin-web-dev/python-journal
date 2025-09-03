num_list=[1,2,3,4,5,6,7,8,9,10]
print("print num from 2 to the end ",num_list[2:]) #[3, 4, 5, 6, 7, 8, 9, 10]

#print num from 1 to the end and each step with 2
print(num_list[::2]) #[1, 3, 5, 7, 9]

#to print the numbers in reverse
print(num_list[::-1]) #[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

#to print the numbers inbetween the 3 to 9
# it will not incude the start index and goes till the endindex
print(num_list[3:9]) #[4, 5, 6, 7, 8, 9]

# when we provide onbly the end index it will startfrom the 0 index to the last index specified
print(num_list[:5]) #[1, 2, 3, 4, 5] 

# -----------------------------------------------------------------------------------------------------------------------------
print()
print()
print("slice operator in the string")
print()

# to reverse a string
my_str="hello world"
print(my_str[::-1]) # dlrow olleh

# index =[  0   ,  1   ,    2   ,    3   ]
my_list=['apple','mango','orange','banana']
print(my_list[0:len(my_list)]) 
# prints complete list 
# output
# ['apple', 'mango', 'orange', 'banana']

print(my_list[0:2]) #['apple', 'mango']
print(my_list[1:2]) #['mango']

