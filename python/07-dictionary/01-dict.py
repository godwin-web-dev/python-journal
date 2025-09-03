new_dict={"Math":90,"social":90}
print(type(new_dict))
new_dict['science']=80
print(new_dict)

# adding the elements to the dictionary
new_dict["chemistry"]=90
print("after adding element => ",new_dict)

# ===============================================================

# iterating over the dict

for i in new_dict.items():
    print(i)

# iterating over the dict using key and values 
for key,value in new_dict.items():
    print(key,value)
# output
# Math 90
# social 90
# science 80
# chemistry 90
print("======================================================")

# removing an element from the dict
new_dict.pop('social')
print("dict after popping an item ",new_dict)
# output
# {'Math': 90, 'science': 80, 'chemistry': 90}

print("=======================================================")
#removing a last item from the dict
new_dict.popitem()
print("dict after popping last item ",new_dict)
# output
# {'Math': 90, 'science': 80}

print("=======================================================")

# To check whether a key exist in the dict
print("check if math is present in new_dict","Math" in new_dict)
print("=======================================================")

# methods in the dict
print(new_dict.get('Math')) #returns the value corresponding to that particular key

# to override the existing values in the dic
key_to_modify=new_dict["science"]=95
print('modified value is as follow ',key_to_modify)
print("dict after modification ",new_dict) # {'Math': 90, 'science': 95}

print("=======================================================")
# to delete the key 
del new_dict["Math"]
print("Deleted 'Math' from dict. Current dict:", new_dict)
print("=======================================================")

# to give the default values for the list of keys
keys=["science",'chemistry','maths','social']
defaultValues="75"
default_values_dict=dict.fromkeys(keys,defaultValues)
print("dict after adding the default values to the key ",default_values_dict) # {'science': '75', 'chemistry': '75', 'maths': '75', 'social': '75'}
# =========================================================================================================================


