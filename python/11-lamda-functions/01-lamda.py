# lamda function are anonyms function which does not require the tradional function syntax like this 
def square_num(x):
    print(x*x)
square_num(2) # output 4

# the above function can be also written as 
square_number=lambda x:x*x
print(square_number(4)) #16

# lamda function are used in the place where a function can be written as the one liner and if the loc of the code is more then follow the traditioanl function method syntax

print_odd_num=lambda x:x%2!=0
print(print_odd_num(3)) #returns true 

# find average of the num
find_avg=lambda x,y:(x+y)/2
print("Average of two number is ",find_avg(10,5)) # Average of two number is  7.5
