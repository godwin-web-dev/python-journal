# Demonstration of Global and Local Scope in Python

x = 25
z = 100

print("I'm from global scope:", x)

def print_local_scope():
    x = 10  # Local variable
    global z  # Refers to the global variable z
    z = 1000  # Modifies the global variable z
    y = "godwin"  # Local variable
    print("I'm from the local scope:", x, y)

# Trying to access y from outside the function will cause an error
# print("y from above function:", y)  # NameError: name 'y' is not defined

print("Trying to access z outside the function:", z)

# Initially, z is 100. Inside the function, we use the global keyword to modify z.
# After calling the function, z will be updated globally.
print_local_scope()

print("Value of z after calling the function:", z)