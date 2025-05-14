# Write a function called calculate_average that takes a list of numbers as input and returns their average. If the list is empty, it should return 0.

def calculate_average(values):
    if len(values) == 0:
        return 0
    else:
        n = len(values)
        total = sum(values)
        return total/n

print(calculate_average([5, 10, 15, 20]))  # Should return 12.5
print(calculate_average([]))  # Should return 0

#---------------------------------------------------------------------------------------------------------------------
# Write a function called greet_user that takes a name and a greeting message. The greeting message should default to "Hello" if not provided.

def greet_user(name, greeting="hello"):
    return f"{greeting.capitalize()}, {name}!"

# Example usage:
print(greet_user("Alice"))  # Should return "Hello, Alice!"
print(greet_user("Bob", "Hi"))  # Should return "Hi, Bob!"

#----------------------------------------------------------------------------------------------------------------
# Create a function called calculate_total that calculates the total cost of items with a variable number of prices and an optional discount percentage.

def calculate_total(*num,discount = 0):
    tot = sum(num)
    if discount > 0:
        tot -= tot * (discount/100)
    return int(tot)


# Example usage:
print(calculate_total(10, 20, 30))  # Should return 60
print(calculate_total(10, 20, 30, discount=10))  # Should return 54 (10% off)


# -----------------------------------------------------------------------------------------------------------------
#Create a function called create_multiplier that takes a number and returns a function that multiplies any input by that number.
def create_multiplier(x):
    def multiply(y):
        return x*y
    return multiply

# Example usage:
double = create_multiplier(2)
triple = create_multiplier(3)
print(double(5))  # Should return 10
print(triple(5))  # Should return 15
