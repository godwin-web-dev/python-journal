print("list comprehension ")

# squares of num using list comprehension 
square_num=[x*x for x in range(1,10)]
print("Squared num ",square_num) #[1, 4, 9, 16, 25, 36, 49, 64, 81]
print("======================================================================================")
#print even number between the range
even_num=[x for x in range(1,5) if x%2==0]
print("Even number ",even_num)
print("======================================================================================")
# print odd number between the range
odd_num=[x for x in range(1,10) if x%2!=0]
print("odd numbers ",odd_num)
print("======================================================================================")

marks = [57, 84, 23, 91, 46, 68, 77, 32, 15, 99]
# checking whether the student are pass/fail
passed_student=[x for x in marks if x>70 ]
print(passed_student) #[84, 91, 77, 99]

# if the student marks is less than 70 then print as the Fail

print_failed_student=[x if x>70  else "Failed" for x in marks]
print("failed students are ",print_failed_student)



