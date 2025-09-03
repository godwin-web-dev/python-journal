a=['apple','mango','orange','banana']
# append an element
print(a.append("pineapple")) #adds an element to the end of the list
print("List after appending an element ",a) # ['apple', 'mango', 'orange', 'banana', 'pineapple']

print("length of the list : ",len(a)) # length of the list is 5

# to find index of a list
# find the index of the list and subtract it by 1 u will get the index of the list
print('index of the list is as follow ',len(a)-1) # index is 4

#you can extend the list 
# print(a.append(10,20)) # this statement is wrong because using append u can only pass one argument at a time

# to combine two list 

print(a.extend([10,20,30,40,50]))
print(a) #['apple', 'mango', 'orange', 'banana', 'pineapple', 10, 20, 30, 40, 50]

# ================================================================================================
#to remove an element from the list 
print(a.pop())
print("List after popping out an element ",a) #  ['apple', 'mango', 'orange', 'banana', 'pineapple', 10, 20, 30, 40]  

# ====================================================================================
list1 = ['apple', 'banana', 'cherry', 'date', 'elderberry'] 
list2 = [1, 2, 3, 4, 5]
list3=list2

print("list1 ",list1)#list1  ['apple', 'banana', 'cherry', 'date', 'elderberry']
print("list2 ",list2) #list2  [1, 2, 3, 4, 5]
print("list3 ",list3) #list2  [1, 2, 3, 4, 5]
print("popping an element from the list3 ",list3.pop()) # 5 element is removed 
print("list3 after popping an element " ,list3) #  [1, 2, 3, 4]
print("checking the content of the list2 ",list2) # [1, 2, 3, 4]

'''
when you assign list3 = list2, both list3 and list2 refer to the same list object in memory. This means that any changes made to list3 will also be reflected in list2, and vice versa.
'''
# =======================================================================================

#to create a copyof an element

fruits = ['apple', 'banana', 'cherry', 'date', 'fig']
numbers = [10, 20, 30, 40, 50]
new_copy=fruits[:]
print(new_copy) #['apple', 'banana', 'cherry', 'date', 'fig']
print(new_copy.append("godwin"))
print("new copy contains ",new_copy) #['apple', 'banana', 'cherry', 'date', 'fig', 'godwin']
print('original list contains ',fruits) #['apple', 'banana', 'cherry', 'date', 'fig']
