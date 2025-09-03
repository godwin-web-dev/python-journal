print("a">"a")
print("a">"Y") #returns true as the output and this comparsion will be based on the ASCII values 
# to find the ascii values of a number
print(ord("a")) #97
print(ord("Y")) #89
# so we will be getting the True because as per the ascii code of a and Y a is greater than Y
# ===========================================================================================
# order of the operation while using the and, or , not

# not preferece1 
# and preferece2
# or preferece 3

name=input("enter your name : ")
if(len(name)==6):
    print("Welcome to world of python")
else:
    print("Ok byeeeee")