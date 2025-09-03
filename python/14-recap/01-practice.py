from collections import Counter
# sorting the number 
def sorting_list(my_list):
    for i in range(0,len(my_list)):
        for j in range(i,len(my_list)):
            if(my_list[i]>my_list[j]):
                my_list[i],my_list[j]=my_list[j],my_list[i]
    print("sorted list is ",my_list)

# finding the largest and smallest number in the list
def find_largest_smallest(my_list):
    largest_num=my_list[0]
    smallest_num=my_list[0]
    for i in my_list:
        if i>largest_num:
            largest_num=i
        else:
            smallest_num=i
    print("largest ",largest_num)
    print("smallest ",smallest_num)

# find occurance of each element in list
def count_occurance(my_list):
    my_dict={}
    for key,value in enumerate(my_list):
        if value in my_dict:
            my_dict[value]+=1
        else:
            my_dict[value]=1
    print(my_dict)

# find occurance of each element in list ~ counter
def count_occurance_using_counter(my_list):
    print(dict(Counter(my_list)))

# find palindrome of the word
def palindrome(my_word):
    reversed_string=''
    for char in my_word:
        reversed_string=char+reversed_string
    if(reversed_string==my_word):
        print(f'{reversed_string} is palindrome')
    else:
        print(f'{reversed_string} is not palindrome')

# merge two list without using concatenation and extend
def merge_two_list():
    list1=[1,2,3,4]
    list2=[10,20,30,40]
    merged_list=[]
    for i in list1:
        merged_list.append(i)
    for j in list2:
        merged_list.append(j)
    print("merged list is ",merged_list)

# count vowel and conso in the string

def count_vowel(my_string):
    vowel_count=0
    conso_count=0
    for i in my_string:
        print(i)
        if i in "aeiou":
            vowel_count+=1
        else:
            conso_count+=1
    print("vowel count is ",vowel_count)
    print("conso count is ",conso_count)

def converting_string_to_upper_lower(my_string):
    to_upper=my_string.upper()
    to_lower=my_string.lower()
    print("lower => ",to_lower)
    print("upper => ",to_upper)
    
# converting string to upper without using inbuit functions  
# note to convert lower to higher then do current value of ascii -32 so 97-32=65 if we convert that ascii to char using chr then we will get A
# print(ord("a"))
# to convert from lower to higher do +32 instead of -32
def convert_str_lower(my_string):
    for i in my_string:
        ascii_value=ord(i)+32
        find_corresponding_char=chr(ascii_value)
        print(find_corresponding_char,end='')
    print()

def convert_str_upper(my_string):
    for i in my_string:
        if "a" <= i <= "z":
            print(chr(ord(i) - 32), end='')
        else:
            print(i, end='')
    print()  

# reverse a number
def print_rev(n):
    reverse_num=0
    while n>0:
        remainder=n%10
        rev=reverse_num*10+remainder
        print(rev,end='')
        n//=10

 
if __name__ == "__main__":
    my_list=[10,20,3,2,2,3,1,2,5]
    sorting_list(my_list)
    find_largest_smallest(my_list)
    count_occurance(my_list)
    count_occurance_using_counter(my_list)

    palindrome("madam")
    palindrome("godwin")

    merge_two_list()
    count_vowel("belloooo")
    converting_string_to_upper_lower("godwin")
    convert_str_lower("ANIMAL")
    convert_str_upper("CLover")
    print_rev(12345)
