#Decorator are the function which extends the behavior of the other function without modifying the base function

def Toppings(toppings):
    def decoratorfun(func):
        def wrapper():
            if toppings=="peperoni":
                print("Added Pepperoni")
            elif toppings=="onions":
                print("Added Onions")
            elif toppings=="mushrooms":
                print("Added mushroom")
            elif toppings=="olives":
                print("Added Olives")
            elif toppings=="pepper":
                print("Added Pepper")
            else:
                print("Default toppings")
            func()
        return wrapper
    return decoratorfun

@Toppings("onions")
@Toppings("peperoni")
@Toppings("pepper")
def pizza():
    print("Chicken pizza")
pizza()