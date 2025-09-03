# ===========================
# Loops in Python
# ===========================

# The for loop in Python is used to iterate over a sequence (such as a list, tuple, string, or range).
# Syntax for range: range(start, end, step)
# - start: starting value (inclusive)
# - end: ending value (exclusive)
# - step: increment (default is 1)

# Example 1: Print numbers from 0 to 9
for i in range(10):
    print(i)

# Example 2: Print numbers from 1 to 9
print("Printing numbers from 1 to 9:")
for i in range(1, 10):
    print(i)

# Example 3: Print numbers in reverse from 5 to 0
print("Printing numbers in reverse from 5 to 0:")
for i in range(5, -1, -1):
    print(i)

# ==============================================================================
# to iterate over the list
print()
print("iterrate over the list ")
a=[10,20,30,40,50]
for i in a:
    print(i)

# ===============================================================================

print()
print("another way to iterate over the list using the len ")
for i in range(len(a)):
    print(a[i])

# ===============================================================================
print()
print("enumerate method")
# List of 5 Marvel characters
marvel_characters = ['Iron Man', 'Captain America', 'Thor', 'Hulk', 'Black Widow']
print("Marvel characters:",marvel_characters)

for index,element in enumerate(marvel_characters):
    print(index,element)

# ================================================================================
print()
print("To print the index and element while iterating over the list")

list_of_fruits=['apple','apple','mango',"mango","mango",'banana']
counter=0
for i in range(len(list_of_fruits)):
    print(i,list_of_fruits[i])
    counter+=1

# output
# To print the index and element while iterating over the list
# 0 apple
# 1 apple
# 2 mango
# 3 mango
# 4 mango
# 5 banana
# ================================================================================
print()
print("Another method to print index without using counter variable")

for index,element in enumerate(list_of_fruits):
    print(index,element)

# output 
# Another method to print index without using counter variable
# 0 apple
# 1 apple
# 2 mango
# 3 mango
# 4 mango
# 5 banana

