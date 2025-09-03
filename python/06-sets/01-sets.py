#set is an unordered collection of the unique elements
#set does not maintain any specifc order due to which we cannot find the index of the set 
#set are used to find unique elements, find untion, intersection, differnce betweent the two set

my_set_element={1,2,33,44,534}

# to print the type of the set 
print(type(my_set_element)) #<class 'set'>  
my_set_element.add(312)
print("set after adding an element ",my_set_element) #{1, 2, 33, 534, 312, 44}

print("==================================================================================")

#ways to convert the list into the set

num_list = [5, 12, 23, 12, 45, 56, 67, 23, 89, 5]
print("number list ", num_list)
converted_list_to_set=set(num_list)# [5, 12, 23, 12, 45, 56, 67, 23, 89, 5]
print(converted_list_to_set) #{67, 5, 12, 45, 23, 56, 89}

print("==================================================================================")

# adding an item to the set
converted_list_to_set.add(1000)
print(converted_list_to_set)#{67, 5, 1000, 12, 45, 23, 56, 89}

print("==================================================================================")
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

#union between the two set
print("union =>  ",set_a | set_b) #{1, 2, 3, 4, 5, 6, 7, 8}

#intersection between the two set
print("intersection => ",set_a & set_b) #{4, 5}

#differnce between the two set
print("difference => ",set_a -set_b  )



