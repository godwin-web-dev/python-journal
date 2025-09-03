# working of the below code 
# first im finding the key and value of the particularstring using enumerate function
# if the value that iterate over the string is  present in the created dict and then i will increament the count each time by 1 for tracking purpose of the occurance
# so if the value is not present in the created dict then i will initiase its occurance with 1

new_string="Godwin"
new_empty_dict={}
for key,value in enumerate(new_string):
    print(key,value)
    if value in new_empty_dict:
        new_empty_dict[value]+=1
    else:
        new_empty_dict[value]=1
print("each occurance is as follow ",new_empty_dict)