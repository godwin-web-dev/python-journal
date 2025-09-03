def print_name(*args):
    for i in args:
        print(i)
student_name=["bhuvan",'rocky']
student_name.append("godwin")
print_name(*student_name)
# u can pass any number of the arguments using the args
#use the kwrgs when you want to pass a dictionary as arguments to the function

print("============================================================================================================")

def print_kwrgs(**kwrgs):
    for key,value in kwrgs.items():
        print(f'The price of {key} is ${value}')
pizza_menu = {
    "Margherita": 8.99,
    "Pepperoni": 10.99,
    "Hawaiian": 9.99,
    "Vegetarian": 9.49,
    "Meat Lovers": 12.99,
    "BBQ Chicken": 11.99,
    "Mushroom": 10.49,
    "Four Cheese": 11.49,
    "Seafood": 13.99,
    "Vegan": 10.99
}

print_kwrgs(**pizza_menu)







