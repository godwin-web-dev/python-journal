from datetime import datetime
from math import pi
import math
import calendar
import platform
from functools import reduce

def show_datetime():
    print(datetime.now()) #2025-08-06 16:06:03.545469

def area_of_circle(radius):
    print("area of the circle")
    print(pi)  # Value of pi
    area = pi * radius * radius
    print(area) # output 3.8013271108436504
    print("===========================================================")

def reverse_name():
    firstName = input("enter your first name : ")
    lastName = input("enter your last name : ")
    fullName = firstName + " " + lastName
    print("original full name ", fullName)
    print("name in reverse ", fullName[::-1])

def input_to_list_tuple():
    user_input = input("enter any number in comma seperated: ")
    to_list = user_input.split(',')
    print("formed list is as follow : ", to_list)
    to_tuple = tuple(to_list)
    print("formed tuple is as follows : ", to_tuple)

def show_colors():
    color_list = ["Red", "Green", "White", "Black"]
    first_color = color_list[0]
    last_color = color_list[-1]
    print(f"first color is {first_color} and last color is {last_color}")

def show_abs_value():
    print(abs(10))

def print_calendar(year, width=2):
    print(calendar.calendar(year, width))

def volume_of_sphere(radius):
    print(4/3*pi*radius*radius)

def diff_from_17(number):
    diff=number-17
    if diff>17:
        print(abs(diff)*2)
    else:
        print(abs(diff))

def num_within(n):
    print(abs(1000-n)<=100 or abs(2000-n)<=100)

def tripple_sum_calc(x,y,z):
    sum_of_vals=x+y+z
    if(x==y==z):
        print(sum_of_vals*3)
    else:
        print(sum_of_vals)

def print_odd_even(n):
    if n%2==0:
        print(f"{n} is even")
    else:
        print(f"{n} is odd")

def count_occur_4():
    nums=[1,2,3,4,4,4,4,5,6,4,10]
    count=0
    for i in nums:
        if i==4:
            count+=1
    print("occurance of the 4 is ",count)

def find_vowels(letter):
    vowels=["a","e","i","o","u"]
    if letter in vowels:
        print(f"{letter} exist in the vowel")
    else:
        print(f"{letter} does not exist in the vowel")

def val_present_in_list(num):
    nums_list= [1, 5, 8, 3] 
    if num in nums_list:
        return True
    else:
        return False

def squarenum():
    output=[x for x in range(1,237) if x%2==0]
    print(output)

def unique_color():
    color_list_1 = set(["White", "Black", "Red"])
    color_list_2 = set(["Red", "Green"])
    print(color_list_1 - color_list_2)
# output: {'White', 'Black'}

def area_of_triangle(base,height):
    area=1/2*base*height
    print(area)

def hcf_of_two_num(a,b):
    if a>b:
        minimum=b
        print("minimum is as follow ",minimum)
    else:
        minimum=a
        print("minimum is as follow ",minimum)
    for i in range(1,minimum+1):
        print("i contains ",i)
        if a%i==0 and b%i==0:
            hcf=i
    print("hcf ",hcf)

def condtional_sum(x,y):
    sum=x+y
    if sum in range(15,20):
        print(20)
    else:
        print(sum)
def equity(x,y):
    sum=x+y
    diff=x-y
    if x==y or abs(sum)==5 or abs(diff)==5:
        return True
    else:
        return False
    
def find_datatype(num,datatype):
    print(f"Data type of this {num} is ",isinstance(num,datatype))

def format_output(x,y):
    result=x*x+y*y+2*x*y
    # (4 + 3) ^ 2) = 49
    print(f"({x}+{y}^2)={result}".format(x,y,result))

def find_sqrt(n):
    print(math.sqrt(n))

def find_distance_between(x1,y1,x2,y2):
    dis=(x2-x1)**2+(y2-y1)**2
    distance=math.sqrt(abs((dis)))
    print("distance between two point ",distance)

def find_system_info():
    print(platform.uname())

def print_sum_n(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
    print(sum)

def print_sum_using_reduce():
    num_list=[2,4,6,8,10]
    calc_sum=lambda x,y:x+y
    print(reduce(calc_sum,num_list))

def find_ascii_val(n):
    print(f"ascii value of {n} is ",ord(n))

def swap_two_num(x,y):
    x,y=y,x
    print("after swapping ",x,y)
    


if __name__ == "__main__":
    # show_datetime()
    # area_of_circle(1.1)
    # reverse_name()
    # input_to_list_tuple()
    # volume_of_sphere(6)
    # diff_from_17(18)
    # num_within(1000)#True
    # tripple_sum_calc(2,2,2)
    # print_odd_even(33)
    # count_occur_4()
    # find_vowels("g")
    # print(val_present_in_list(3))
    # print_even_num_till_237()
    # squarenum()
    # unique_color()
    # area_of_triangle(2,4)
    # hcf_of_two_num(2,4)
    # condtional_sum(18,2)
    # print(equity(27,53))
    # find_datatype(2,float)
    # format_output(4,3)
    # find_sqrt(5)
    # find_distance_between(3,4,7,1)
    # find_system_info()
    # print_sum_n(100)
    # print_sum_using_reduce()
    # find_ascii_val("a")
    swap_two_num(2,3)